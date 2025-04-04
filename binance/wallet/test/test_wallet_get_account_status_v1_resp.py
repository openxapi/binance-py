# coding: utf-8

"""
    Binance Wallet API

    OpenAPI specification for Binance exchange - Wallet API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.wallet.models.wallet_get_account_status_v1_resp import WalletGetAccountStatusV1Resp

class TestWalletGetAccountStatusV1Resp(unittest.TestCase):
    """WalletGetAccountStatusV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletGetAccountStatusV1Resp:
        """Test WalletGetAccountStatusV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletGetAccountStatusV1Resp`
        """
        model = WalletGetAccountStatusV1Resp()
        if include_optional:
            return WalletGetAccountStatusV1Resp(
                data = ''
            )
        else:
            return WalletGetAccountStatusV1Resp(
        )
        """

    def testWalletGetAccountStatusV1Resp(self):
        """Test WalletGetAccountStatusV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
