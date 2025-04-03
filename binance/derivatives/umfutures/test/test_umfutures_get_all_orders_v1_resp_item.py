# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_all_orders_v1_resp_item import UmfuturesGetAllOrdersV1RespItem

class TestUmfuturesGetAllOrdersV1RespItem(unittest.TestCase):
    """UmfuturesGetAllOrdersV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetAllOrdersV1RespItem:
        """Test UmfuturesGetAllOrdersV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetAllOrdersV1RespItem`
        """
        model = UmfuturesGetAllOrdersV1RespItem()
        if include_optional:
            return UmfuturesGetAllOrdersV1RespItem(
                activate_price = '',
                avg_price = '',
                client_order_id = '',
                close_position = True,
                cum_quote = '',
                executed_qty = '',
                good_till_date = 56,
                order_id = 56,
                orig_qty = '',
                orig_type = '',
                position_side = '',
                price = '',
                price_match = '',
                price_protect = True,
                price_rate = '',
                reduce_only = True,
                self_trade_prevention_mode = '',
                side = '',
                status = '',
                stop_price = '',
                symbol = '',
                time = 56,
                time_in_force = '',
                type = '',
                update_time = 56,
                working_type = ''
            )
        else:
            return UmfuturesGetAllOrdersV1RespItem(
        )
        """

    def testUmfuturesGetAllOrdersV1RespItem(self):
        """Test UmfuturesGetAllOrdersV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
