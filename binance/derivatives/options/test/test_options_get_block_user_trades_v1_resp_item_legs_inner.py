# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.options.models.options_get_block_user_trades_v1_resp_item_legs_inner import OptionsGetBlockUserTradesV1RespItemLegsInner

class TestOptionsGetBlockUserTradesV1RespItemLegsInner(unittest.TestCase):
    """OptionsGetBlockUserTradesV1RespItemLegsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsGetBlockUserTradesV1RespItemLegsInner:
        """Test OptionsGetBlockUserTradesV1RespItemLegsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsGetBlockUserTradesV1RespItemLegsInner`
        """
        model = OptionsGetBlockUserTradesV1RespItemLegsInner()
        if include_optional:
            return OptionsGetBlockUserTradesV1RespItemLegsInner(
                commission = 1.337,
                create_time = 56,
                executed_amount = 1.337,
                executed_qty = 1.337,
                fee = 1.337,
                id = '',
                liquidity = '',
                order_id = '',
                order_price = 1.337,
                order_quantity = 1.337,
                order_side = '',
                order_status = '',
                order_type = '',
                symbol = '',
                trade_id = 56,
                trade_price = 1.337,
                trade_qty = 1.337,
                trade_time = 56,
                update_time = 56
            )
        else:
            return OptionsGetBlockUserTradesV1RespItemLegsInner(
        )
        """

    def testOptionsGetBlockUserTradesV1RespItemLegsInner(self):
        """Test OptionsGetBlockUserTradesV1RespItemLegsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
