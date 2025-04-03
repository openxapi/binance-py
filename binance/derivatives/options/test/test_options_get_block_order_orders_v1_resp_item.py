# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.options.models.options_get_block_order_orders_v1_resp_item import OptionsGetBlockOrderOrdersV1RespItem

class TestOptionsGetBlockOrderOrdersV1RespItem(unittest.TestCase):
    """OptionsGetBlockOrderOrdersV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsGetBlockOrderOrdersV1RespItem:
        """Test OptionsGetBlockOrderOrdersV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsGetBlockOrderOrdersV1RespItem`
        """
        model = OptionsGetBlockOrderOrdersV1RespItem()
        if include_optional:
            return OptionsGetBlockOrderOrdersV1RespItem(
                block_trade_settlement_key = '',
                create_time = 56,
                expire_time = 56,
                legs = [
                    binance.derivatives.options.models.options_create_block_order_create_v1_resp_legs_inner.OptionsCreateBlockOrderCreateV1Resp_legs_inner(
                        price = '', 
                        quantity = '', 
                        side = '', 
                        symbol = '', )
                    ],
                liquidity = '',
                status = ''
            )
        else:
            return OptionsGetBlockOrderOrdersV1RespItem(
        )
        """

    def testOptionsGetBlockOrderOrdersV1RespItem(self):
        """Test OptionsGetBlockOrderOrdersV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
