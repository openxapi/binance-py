"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import base64
import hashlib
import hmac
import io
import os
import re
import urllib.parse
from typing import Any, Dict, Optional, Union, Tuple, Callable, List

from Crypto.PublicKey import RSA, ECC
from Crypto.Signature import pkcs1_15, eddsa
from Crypto.Hash import SHA256
from Crypto.IO import PEM
from Crypto.Util.asn1 import DerSequence
from Crypto.PublicKey.ECC import EccKey
from Crypto.PublicKey.RSA import RsaKey


class KeyType:
    HMAC = "HMAC"
    RSA = "RSA"
    ED25519 = "ED25519"

class BinanceAuth:
    """
    Handles authentication for Binance API requests using API Key and either
    Secret Key (HMAC) or Private Key (RSA/ED25519).

    :param api_key: Your Binance API Key.
    :param secret_key: Your Binance Secret Key (for HMAC signing). Mutually exclusive with private_key_path/private_key_pem.
    :param private_key_path: Path to your PEM-encoded private key file (for RSA/ED25519 signing). Mutually exclusive with secret_key/private_key_pem.
    :param private_key_pem: String containing the PEM-encoded private key (for RSA/ED25519 signing). Mutually exclusive with secret_key/private_key_path.
    :param passphrase: Passphrase to decrypt the private key, if it's encrypted.
    """
    def __init__(
        self,
        api_key: str,
        secret_key: Optional[str] = None,
        private_key_path: Optional[str] = None,
        private_key_pem: Optional[str] = None,
        passphrase: Optional[str] = None,
    ):
        if not api_key:
            raise ValueError("API Key is required.")

        self.api_key = api_key
        self.secret_key: Optional[str] = None
        self.private_key: Optional[Union[RsaKey, EccKey]] = None
        self.key_type: Optional[str] = None
        self.passphrase = passphrase

        # Validate mutually exclusive parameters
        key_sources = sum(p is not None for p in [secret_key, private_key_path, private_key_pem])
        if key_sources == 0:
            raise ValueError("One of secret_key, private_key_path, or private_key_pem must be provided.")
        if key_sources > 1:
            raise ValueError("Only one of secret_key, private_key_path, or private_key_pem can be provided.")

        if secret_key:
            self.secret_key = secret_key
            self.key_type = KeyType.HMAC
        else:
            self._load_private_key(private_key_path, private_key_pem)


    def _load_private_key(self, private_key_path: Optional[str], private_key_pem: Optional[str]):
        """Loads and parses the private key from path or string."""
        pem_data: Optional[bytes] = None
        source_description = ""

        if private_key_pem:
            pem_data = private_key_pem.encode('utf-8')
            source_description = "string"
        elif private_key_path:
            source_description = f"file '{private_key_path}'"
            if not os.path.exists(private_key_path):
                raise FileNotFoundError(f"Private key file not found: {private_key_path}")
            try:
                with open(private_key_path, 'rb') as f:
                    pem_data = f.read()
            except IOError as e:
                raise IOError(f"Cannot load private key {source_description}. Error: {e}")

        if not pem_data:
             # This case should ideally not be reached due to initial checks, but added for safety
             raise ValueError("No private key data provided.")

        try:
            passphrase_bytes = self.passphrase.encode('utf-8') if self.passphrase else None
            # Try parsing as PKCS#8 first (covers modern EC and RSA keys)
            try:
                # Attempt import with potential passphrase
                self.private_key = ECC.import_key(pem_data, passphrase=passphrase_bytes)
                # Check if it's actually an ED25519 key
                # We might need a more reliable check here if ECC.import_key loads other curve types
                # For now, assume non-RSA loaded via ECC.import_key could be ED25519 if needed
                try:
                    # Try to check if it's an Ed25519 key using eddsa
                    # We'll check if eddsa can create a new signer with this key
                    # If it succeeds, it's likely an Ed25519 key
                    signer_test = eddsa.new(self.private_key, mode='rfc8032')
                    self.key_type = KeyType.ED25519
                except (ValueError, TypeError) as e_ed25519:
                    # If not Ed25519, check if it's RSA loaded via PKCS#8
                    try:
                        # Try importing specifically as RSA to confirm
                        rsa_key_check = RSA.import_key(pem_data, passphrase=passphrase_bytes)
                        # Confirm it's actually an RSA key object
                        if isinstance(rsa_key_check, RsaKey):
                            self.private_key = rsa_key_check
                            self.key_type = KeyType.RSA
                        else:
                            # If ECC.import_key worked but it's not Ed25519 or RSA, it's an unsupported EC key for Binance
                            raise ValueError("Unsupported EC private key type loaded.")
                    except (ValueError, TypeError, IndexError):
                        # If it failed both Ed25519 and RSA import, but ECC.import_key worked initially,
                        # it might be another EC type not used by Binance or error in logic.
                        # For safety, raise error if not explicitly identified as RSA or ED25519.
                        raise ValueError("Could not determine private key type (not RSA or ED25519).")

            except (ValueError, TypeError, IndexError) as e_pkcs8:
                # If PKCS#8 fails, try legacy PEM formats (PKCS#1 for RSA)
                try:
                    self.private_key = RSA.import_key(pem_data, passphrase=passphrase_bytes)
                    self.key_type = KeyType.RSA
                except (ValueError, TypeError, IndexError) as e_pkcs1:
                    # Try specifically importing as Ed25519 using eddsa
                    try:
                        # This handles raw Ed25519 format (32 bytes)
                        if len(pem_data) == 32 or "BEGIN OPENSSH PRIVATE KEY" in pem_data.decode('utf-8', errors='ignore'):
                            self.private_key = eddsa.import_private_key(pem_data)
                            self.key_type = KeyType.ED25519
                        else:
                            # If all import attempts fail
                            raise ValueError(
                                f"Failed to parse private key from {source_description}. "
                                f"Check format and passphrase. PKCS#8 Error: {e_pkcs8}, PKCS#1 Error: {e_pkcs1}"
                            )
                    except (ValueError, TypeError) as e_raw_ed25519:
                        # If all import attempts fail
                        raise ValueError(
                            f"Failed to parse private key from {source_description}. "
                            f"Check format and passphrase. PKCS#8 Error: {e_pkcs8}, PKCS#1 Error: {e_pkcs1}, "
                            f"Ed25519 Error: {e_raw_ed25519}"
                        )

        except Exception as e:
             # Catch any other unexpected errors during loading/parsing
             raise RuntimeError(f"An unexpected error occurred while processing the private key: {e}")

        if not self.key_type or not self.private_key:
            raise ValueError(f"Could not determine or load private key type from {source_description}.")


    def _get_signature_payload(
        self,
        query_params: Optional[List[Tuple[str, str]]],
        request_body: Optional[Union[str, bytes]],
        parameters_to_url_query: Callable[[List[Tuple[str, str]], Dict[str, str]], str]
    ) -> bytes:
        """
        Constructs the payload string for signing according to Binance rules.
        Payload is queryString[&body]
        """
        query_string = ""
        if query_params:
            # Encode parameters, Binance uses urlencode but doesn't escape '@'
            # Python's urlencode escapes '@' to '%40'. Go code replaces %40 back to @.
            # We replicate the Go behavior here.
            query_string = parameters_to_url_query(query_params, None)


        body_string = ""
        if request_body:
            if isinstance(request_body, bytes):
                 # Assume bytes are already correctly encoded (e.g., application/json uses UTF-8)
                body_string = request_body.decode('utf-8') # Decode for manipulation if needed
            else:
                 # Assume string if not bytes
                body_string = request_body

            body_string = body_string.replace('%40', '@')


        # Combine query string and body
        if query_string and body_string:
            payload = f"{query_string}{body_string}"
        elif body_string:
            payload = body_string
        else:
            payload = query_string # Can be empty if no query params and no body

        return payload.encode('utf-8')


    def sign(
        self,
        header_params: Optional[Dict[str, Any]],
        query_params: Optional[List[Tuple[str, str]]],
        request_body: Optional[Union[str, bytes]],
        parameters_to_url_query: Callable[[List[Tuple[str, str]], Dict[str, str]], str]
    ) -> None:
        """
        Generates the signature for the request data.

        :param header_params: Dictionary of header parameters.
        :param query_params: List of tuples of query parameters.
        :param request_body: The request body as a string or bytes.
        :return: The calculated signature string (hex for HMAC, base64 for RSA/ED25519).
        """
        header_params = header_params or {}
        header_params['X-MBX-APIKEY'] = self.api_key

        payload = self._get_signature_payload(query_params, request_body, parameters_to_url_query)
        signature: str

        if self.key_type == KeyType.HMAC:
            if not self.secret_key:
                 raise ValueError("Secret key is not set for HMAC signing.")
            mac = hmac.new(self.secret_key.encode('utf-8'), payload, hashlib.sha256)
            signature = mac.hexdigest()
        elif self.key_type == KeyType.RSA:
            if not isinstance(self.private_key, RsaKey):
                 raise TypeError("Private key is not a valid RSA key.")
            signer = pkcs1_15.new(self.private_key)
            digest = SHA256.new(payload)
            sig_bytes = signer.sign(digest)
            signature = base64.b64encode(sig_bytes).decode('utf-8')
        elif self.key_type == KeyType.ED25519:
            if not hasattr(self.private_key, 'pointQ'): # Basic check if it looks like an ECC key
                 raise TypeError("Private key is not a valid Ed25519 key or doesn't support signing.")
            # Use EdDSA signature scheme for Ed25519
            signer = eddsa.new(self.private_key, mode='rfc8032') # mode='rfc8032' is standard for Ed25519
            sig_bytes = signer.sign(payload)
            signature = base64.b64encode(sig_bytes).decode('utf-8')
        else:
            raise ValueError(f"Unsupported key type for signing: {self.key_type}")

        # Make sure signature is at the end of the query string
        if query_params:
            query_params.append(('signature', signature))
        else:
            query_params = [('signature', signature)]
