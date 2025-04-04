# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_cm_conditional_open_orders_v1_resp_item import PmarginGetCmConditionalOpenOrdersV1RespItem

class TestPmarginGetCmConditionalOpenOrdersV1RespItem(unittest.TestCase):
    """PmarginGetCmConditionalOpenOrdersV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetCmConditionalOpenOrdersV1RespItem:
        """Test PmarginGetCmConditionalOpenOrdersV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetCmConditionalOpenOrdersV1RespItem`
        """
        model = PmarginGetCmConditionalOpenOrdersV1RespItem()
        if include_optional:
            return PmarginGetCmConditionalOpenOrdersV1RespItem(
                activate_price = '',
                book_time = 56,
                new_client_strategy_id = '',
                orig_qty = '',
                position_side = '',
                price = '',
                price_rate = '',
                reduce_only = True,
                side = '',
                stop_price = '',
                strategy_id = 56,
                strategy_status = '',
                strategy_type = '',
                symbol = '',
                time_in_force = '',
                update_time = 56
            )
        else:
            return PmarginGetCmConditionalOpenOrdersV1RespItem(
        )
        """

    def testPmarginGetCmConditionalOpenOrdersV1RespItem(self):
        """Test PmarginGetCmConditionalOpenOrdersV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
