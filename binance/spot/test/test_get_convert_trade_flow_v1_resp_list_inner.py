# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_convert_trade_flow_v1_resp_list_inner import GetConvertTradeFlowV1RespListInner

class TestGetConvertTradeFlowV1RespListInner(unittest.TestCase):
    """GetConvertTradeFlowV1RespListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetConvertTradeFlowV1RespListInner:
        """Test GetConvertTradeFlowV1RespListInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetConvertTradeFlowV1RespListInner`
        """
        model = GetConvertTradeFlowV1RespListInner()
        if include_optional:
            return GetConvertTradeFlowV1RespListInner(
                create_time = 56,
                from_amount = '',
                from_asset = '',
                inverse_ratio = '',
                order_id = 56,
                order_status = '',
                quote_id = '',
                ratio = '',
                to_amount = '',
                to_asset = ''
            )
        else:
            return GetConvertTradeFlowV1RespListInner(
        )
        """

    def testGetConvertTradeFlowV1RespListInner(self):
        """Test GetConvertTradeFlowV1RespListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
