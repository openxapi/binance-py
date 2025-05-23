# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.delete_margin_open_orders_v1_resp_item import DeleteMarginOpenOrdersV1RespItem

class TestDeleteMarginOpenOrdersV1RespItem(unittest.TestCase):
    """DeleteMarginOpenOrdersV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteMarginOpenOrdersV1RespItem:
        """Test DeleteMarginOpenOrdersV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteMarginOpenOrdersV1RespItem`
        """
        model = DeleteMarginOpenOrdersV1RespItem()
        if include_optional:
            return DeleteMarginOpenOrdersV1RespItem(
                client_order_id = '',
                cummulative_quote_qty = '',
                executed_qty = '',
                is_isolated = True,
                order_id = 56,
                order_list_id = 56,
                orig_client_order_id = '',
                orig_qty = '',
                price = '',
                self_trade_prevention_mode = '',
                side = '',
                status = '',
                symbol = '',
                time_in_force = '',
                type = ''
            )
        else:
            return DeleteMarginOpenOrdersV1RespItem(
        )
        """

    def testDeleteMarginOpenOrdersV1RespItem(self):
        """Test DeleteMarginOpenOrdersV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
