# coding: utf-8

"""
    Binance Wallet API

    OpenAPI specification for Binance exchange - Wallet API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.wallet.models.wallet_get_asset_asset_dividend_v1_resp_rows_inner import WalletGetAssetAssetDividendV1RespRowsInner

class TestWalletGetAssetAssetDividendV1RespRowsInner(unittest.TestCase):
    """WalletGetAssetAssetDividendV1RespRowsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletGetAssetAssetDividendV1RespRowsInner:
        """Test WalletGetAssetAssetDividendV1RespRowsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletGetAssetAssetDividendV1RespRowsInner`
        """
        model = WalletGetAssetAssetDividendV1RespRowsInner()
        if include_optional:
            return WalletGetAssetAssetDividendV1RespRowsInner(
                amount = '',
                asset = '',
                div_time = 56,
                en_info = '',
                id = 56,
                tran_id = 56
            )
        else:
            return WalletGetAssetAssetDividendV1RespRowsInner(
        )
        """

    def testWalletGetAssetAssetDividendV1RespRowsInner(self):
        """Test WalletGetAssetAssetDividendV1RespRowsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
