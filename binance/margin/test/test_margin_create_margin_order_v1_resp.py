# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_create_margin_order_v1_resp import MarginCreateMarginOrderV1Resp

class TestMarginCreateMarginOrderV1Resp(unittest.TestCase):
    """MarginCreateMarginOrderV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginCreateMarginOrderV1Resp:
        """Test MarginCreateMarginOrderV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginCreateMarginOrderV1Resp`
        """
        model = MarginCreateMarginOrderV1Resp()
        if include_optional:
            return MarginCreateMarginOrderV1Resp(
                client_order_id = '',
                cummulative_quote_qty = '',
                executed_qty = '',
                fills = [
                    binance.margin.models.margin_create_margin_order_v1_resp_fills_inner.MarginCreateMarginOrderV1Resp_fills_inner(
                        commission = '', 
                        commission_asset = '', 
                        price = '', 
                        qty = '', 
                        trade_id = 56, )
                    ],
                is_isolated = True,
                margin_buy_borrow_amount = 56,
                margin_buy_borrow_asset = '',
                order_id = 56,
                orig_qty = '',
                price = '',
                self_trade_prevention_mode = '',
                side = '',
                status = '',
                symbol = '',
                time_in_force = '',
                transact_time = 56,
                type = ''
            )
        else:
            return MarginCreateMarginOrderV1Resp(
        )
        """

    def testMarginCreateMarginOrderV1Resp(self):
        """Test MarginCreateMarginOrderV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
