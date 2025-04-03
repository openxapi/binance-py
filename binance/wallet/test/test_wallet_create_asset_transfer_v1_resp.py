# coding: utf-8

"""
    Binance Wallet API

    OpenAPI specification for Binance exchange - Wallet API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.wallet.models.wallet_create_asset_transfer_v1_resp import WalletCreateAssetTransferV1Resp

class TestWalletCreateAssetTransferV1Resp(unittest.TestCase):
    """WalletCreateAssetTransferV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletCreateAssetTransferV1Resp:
        """Test WalletCreateAssetTransferV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletCreateAssetTransferV1Resp`
        """
        model = WalletCreateAssetTransferV1Resp()
        if include_optional:
            return WalletCreateAssetTransferV1Resp(
                tran_id = 56
            )
        else:
            return WalletCreateAssetTransferV1Resp(
        )
        """

    def testWalletCreateAssetTransferV1Resp(self):
        """Test WalletCreateAssetTransferV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
