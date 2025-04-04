# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_get_margin_isolated_account_v1_resp_assets_inner import MarginGetMarginIsolatedAccountV1RespAssetsInner

class TestMarginGetMarginIsolatedAccountV1RespAssetsInner(unittest.TestCase):
    """MarginGetMarginIsolatedAccountV1RespAssetsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginGetMarginIsolatedAccountV1RespAssetsInner:
        """Test MarginGetMarginIsolatedAccountV1RespAssetsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginGetMarginIsolatedAccountV1RespAssetsInner`
        """
        model = MarginGetMarginIsolatedAccountV1RespAssetsInner()
        if include_optional:
            return MarginGetMarginIsolatedAccountV1RespAssetsInner(
                base_asset = binance.margin.models.margin_get_margin_isolated_account_v1_resp_assets_inner_base_asset.MarginGetMarginIsolatedAccountV1Resp_assets_inner_baseAsset(
                    asset = '', 
                    borrow_enabled = True, 
                    borrowed = '', 
                    free = '', 
                    interest = '', 
                    locked = '', 
                    net_asset = '', 
                    net_asset_of_btc = '', 
                    repay_enabled = True, 
                    total_asset = '', ),
                enabled = True,
                index_price = '',
                isolated_created = True,
                liquidate_price = '',
                liquidate_rate = '',
                margin_level = '',
                margin_level_status = '',
                margin_ratio = '',
                quote_asset = binance.margin.models.margin_get_margin_isolated_account_v1_resp_assets_inner_base_asset.MarginGetMarginIsolatedAccountV1Resp_assets_inner_baseAsset(
                    asset = '', 
                    borrow_enabled = True, 
                    borrowed = '', 
                    free = '', 
                    interest = '', 
                    locked = '', 
                    net_asset = '', 
                    net_asset_of_btc = '', 
                    repay_enabled = True, 
                    total_asset = '', ),
                symbol = '',
                trade_enabled = True
            )
        else:
            return MarginGetMarginIsolatedAccountV1RespAssetsInner(
        )
        """

    def testMarginGetMarginIsolatedAccountV1RespAssetsInner(self):
        """Test MarginGetMarginIsolatedAccountV1RespAssetsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
