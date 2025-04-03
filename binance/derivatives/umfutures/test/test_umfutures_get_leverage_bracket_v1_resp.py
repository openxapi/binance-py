# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_leverage_bracket_v1_resp import UmfuturesGetLeverageBracketV1Resp

class TestUmfuturesGetLeverageBracketV1Resp(unittest.TestCase):
    """UmfuturesGetLeverageBracketV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetLeverageBracketV1Resp:
        """Test UmfuturesGetLeverageBracketV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetLeverageBracketV1Resp`
        """
        model = UmfuturesGetLeverageBracketV1Resp()
        if include_optional:
            return UmfuturesGetLeverageBracketV1Resp(
                brackets = [
                    binance.derivatives.umfutures.models.umfutures_get_leverage_bracket_v1_resp_item_brackets_inner.UmfuturesGetLeverageBracketV1RespItem_brackets_inner(
                        bracket = 56, 
                        cum = 56, 
                        initial_leverage = 56, 
                        maint_margin_ratio = 1.337, 
                        notional_cap = 56, 
                        notional_floor = 56, )
                    ],
                notional_coef = 1.337,
                symbol = ''
            )
        else:
            return UmfuturesGetLeverageBracketV1Resp(
        )
        """

    def testUmfuturesGetLeverageBracketV1Resp(self):
        """Test UmfuturesGetLeverageBracketV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
