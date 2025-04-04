# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_create_margin_order_oco_v1_resp_order_reports_inner import MarginCreateMarginOrderOcoV1RespOrderReportsInner

class TestMarginCreateMarginOrderOcoV1RespOrderReportsInner(unittest.TestCase):
    """MarginCreateMarginOrderOcoV1RespOrderReportsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginCreateMarginOrderOcoV1RespOrderReportsInner:
        """Test MarginCreateMarginOrderOcoV1RespOrderReportsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginCreateMarginOrderOcoV1RespOrderReportsInner`
        """
        model = MarginCreateMarginOrderOcoV1RespOrderReportsInner()
        if include_optional:
            return MarginCreateMarginOrderOcoV1RespOrderReportsInner(
                client_order_id = '',
                cummulative_quote_qty = '',
                executed_qty = '',
                order_id = 56,
                order_list_id = 56,
                orig_qty = '',
                price = '',
                self_trade_prevention_mode = '',
                side = '',
                status = '',
                stop_price = '',
                symbol = '',
                time_in_force = '',
                transact_time = 56,
                type = ''
            )
        else:
            return MarginCreateMarginOrderOcoV1RespOrderReportsInner(
        )
        """

    def testMarginCreateMarginOrderOcoV1RespOrderReportsInner(self):
        """Test MarginCreateMarginOrderOcoV1RespOrderReportsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
