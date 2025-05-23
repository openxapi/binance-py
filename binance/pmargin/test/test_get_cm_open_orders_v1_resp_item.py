# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.pmargin.models.get_cm_open_orders_v1_resp_item import GetCmOpenOrdersV1RespItem

class TestGetCmOpenOrdersV1RespItem(unittest.TestCase):
    """GetCmOpenOrdersV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCmOpenOrdersV1RespItem:
        """Test GetCmOpenOrdersV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCmOpenOrdersV1RespItem`
        """
        model = GetCmOpenOrdersV1RespItem()
        if include_optional:
            return GetCmOpenOrdersV1RespItem(
                avg_price = '',
                client_order_id = '',
                cum_base = '',
                executed_qty = '',
                order_id = 56,
                orig_qty = '',
                orig_type = '',
                pair = '',
                position_side = '',
                price = '',
                reduce_only = True,
                side = '',
                status = '',
                symbol = '',
                time = 56,
                time_in_force = '',
                type = '',
                update_time = 56
            )
        else:
            return GetCmOpenOrdersV1RespItem(
        )
        """

    def testGetCmOpenOrdersV1RespItem(self):
        """Test GetCmOpenOrdersV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
