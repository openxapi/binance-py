# coding: utf-8

"""
    Binance Wallet API

    OpenAPI specification for Binance exchange - Wallet API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.wallet.models.wallet_get_asset_transfer_v1_resp import WalletGetAssetTransferV1Resp

class TestWalletGetAssetTransferV1Resp(unittest.TestCase):
    """WalletGetAssetTransferV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletGetAssetTransferV1Resp:
        """Test WalletGetAssetTransferV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletGetAssetTransferV1Resp`
        """
        model = WalletGetAssetTransferV1Resp()
        if include_optional:
            return WalletGetAssetTransferV1Resp(
                rows = [
                    binance.wallet.models.wallet_get_asset_transfer_v1_resp_rows_inner.WalletGetAssetTransferV1Resp_rows_inner(
                        amount = '', 
                        asset = '', 
                        status = '', 
                        timestamp = 56, 
                        tran_id = 56, 
                        type = '', )
                    ],
                total = 56
            )
        else:
            return WalletGetAssetTransferV1Resp(
        )
        """

    def testWalletGetAssetTransferV1Resp(self):
        """Test WalletGetAssetTransferV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
