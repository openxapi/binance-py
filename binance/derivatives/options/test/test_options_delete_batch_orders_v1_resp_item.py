# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.options.models.options_delete_batch_orders_v1_resp_item import OptionsDeleteBatchOrdersV1RespItem

class TestOptionsDeleteBatchOrdersV1RespItem(unittest.TestCase):
    """OptionsDeleteBatchOrdersV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsDeleteBatchOrdersV1RespItem:
        """Test OptionsDeleteBatchOrdersV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsDeleteBatchOrdersV1RespItem`
        """
        model = OptionsDeleteBatchOrdersV1RespItem()
        if include_optional:
            return OptionsDeleteBatchOrdersV1RespItem(
                avg_price = '',
                client_order_id = '',
                create_time = 56,
                executed_qty = '',
                fee = 56,
                order_id = 56,
                price = '',
                quantity = '',
                reduce_only = True,
                side = '',
                status = '',
                symbol = '',
                time_in_force = '',
                type = '',
                update_time = 56
            )
        else:
            return OptionsDeleteBatchOrdersV1RespItem(
        )
        """

    def testOptionsDeleteBatchOrdersV1RespItem(self):
        """Test OptionsDeleteBatchOrdersV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
