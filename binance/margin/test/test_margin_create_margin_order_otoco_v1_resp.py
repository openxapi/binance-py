# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_create_margin_order_otoco_v1_resp import MarginCreateMarginOrderOtocoV1Resp

class TestMarginCreateMarginOrderOtocoV1Resp(unittest.TestCase):
    """MarginCreateMarginOrderOtocoV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginCreateMarginOrderOtocoV1Resp:
        """Test MarginCreateMarginOrderOtocoV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginCreateMarginOrderOtocoV1Resp`
        """
        model = MarginCreateMarginOrderOtocoV1Resp()
        if include_optional:
            return MarginCreateMarginOrderOtocoV1Resp(
                contingency_type = '',
                is_isolated = True,
                list_client_order_id = '',
                list_order_status = '',
                list_status_type = '',
                order_list_id = 56,
                order_reports = [
                    binance.margin.models.margin_create_margin_order_oto_v1_resp_order_reports_inner.MarginCreateMarginOrderOtoV1Resp_orderReports_inner(
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
                        symbol = '', 
                        time_in_force = '', 
                        transact_time = 56, 
                        type = '', )
                    ],
                orders = [
                    binance.margin.models.margin_create_margin_order_oco_v1_resp_orders_inner.MarginCreateMarginOrderOcoV1Resp_orders_inner(
                        client_order_id = '', 
                        order_id = 56, 
                        symbol = '', )
                    ],
                symbol = '',
                transaction_time = 56
            )
        else:
            return MarginCreateMarginOrderOtocoV1Resp(
        )
        """

    def testMarginCreateMarginOrderOtocoV1Resp(self):
        """Test MarginCreateMarginOrderOtocoV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
