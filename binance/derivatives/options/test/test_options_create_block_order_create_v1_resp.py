# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.options.models.options_create_block_order_create_v1_resp import OptionsCreateBlockOrderCreateV1Resp

class TestOptionsCreateBlockOrderCreateV1Resp(unittest.TestCase):
    """OptionsCreateBlockOrderCreateV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsCreateBlockOrderCreateV1Resp:
        """Test OptionsCreateBlockOrderCreateV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsCreateBlockOrderCreateV1Resp`
        """
        model = OptionsCreateBlockOrderCreateV1Resp()
        if include_optional:
            return OptionsCreateBlockOrderCreateV1Resp(
                block_trade_settlement_key = '',
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
            return OptionsCreateBlockOrderCreateV1Resp(
        )
        """

    def testOptionsCreateBlockOrderCreateV1Resp(self):
        """Test OptionsCreateBlockOrderCreateV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
