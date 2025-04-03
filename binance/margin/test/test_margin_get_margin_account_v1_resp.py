# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_get_margin_account_v1_resp import MarginGetMarginAccountV1Resp

class TestMarginGetMarginAccountV1Resp(unittest.TestCase):
    """MarginGetMarginAccountV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginGetMarginAccountV1Resp:
        """Test MarginGetMarginAccountV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginGetMarginAccountV1Resp`
        """
        model = MarginGetMarginAccountV1Resp()
        if include_optional:
            return MarginGetMarginAccountV1Resp(
                total_collateral_value_in_usdt = '',
                account_type = '',
                borrow_enabled = True,
                collateral_margin_level = '',
                created = True,
                margin_level = '',
                total_asset_of_btc = '',
                total_liability_of_btc = '',
                total_net_asset_of_btc = '',
                total_open_order_loss_in_usdt = '',
                trade_enabled = True,
                transfer_in_enabled = True,
                transfer_out_enabled = True,
                user_assets = [
                    binance.margin.models.margin_get_margin_account_v1_resp_user_assets_inner.MarginGetMarginAccountV1Resp_userAssets_inner(
                        asset = '', 
                        borrowed = '', 
                        free = '', 
                        interest = '', 
                        locked = '', 
                        net_asset = '', )
                    ]
            )
        else:
            return MarginGetMarginAccountV1Resp(
        )
        """

    def testMarginGetMarginAccountV1Resp(self):
        """Test MarginGetMarginAccountV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
