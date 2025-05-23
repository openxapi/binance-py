# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.options.models.options_delete_batch_orders_v1_resp_inner import OptionsDeleteBatchOrdersV1RespInner

class TestOptionsDeleteBatchOrdersV1RespInner(unittest.TestCase):
    """OptionsDeleteBatchOrdersV1RespInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsDeleteBatchOrdersV1RespInner:
        """Test OptionsDeleteBatchOrdersV1RespInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsDeleteBatchOrdersV1RespInner`
        """
        model = OptionsDeleteBatchOrdersV1RespInner()
        if include_optional:
            return OptionsDeleteBatchOrdersV1RespInner(
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
                update_time = 56,
                code = 56,
                msg = ''
            )
        else:
            return OptionsDeleteBatchOrdersV1RespInner(
        )
        """

    def testOptionsDeleteBatchOrdersV1RespInner(self):
        """Test OptionsDeleteBatchOrdersV1RespInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
