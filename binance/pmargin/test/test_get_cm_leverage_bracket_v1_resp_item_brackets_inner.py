# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.pmargin.models.get_cm_leverage_bracket_v1_resp_item_brackets_inner import GetCmLeverageBracketV1RespItemBracketsInner

class TestGetCmLeverageBracketV1RespItemBracketsInner(unittest.TestCase):
    """GetCmLeverageBracketV1RespItemBracketsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCmLeverageBracketV1RespItemBracketsInner:
        """Test GetCmLeverageBracketV1RespItemBracketsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCmLeverageBracketV1RespItemBracketsInner`
        """
        model = GetCmLeverageBracketV1RespItemBracketsInner()
        if include_optional:
            return GetCmLeverageBracketV1RespItemBracketsInner(
                bracket = 56,
                cum = 56,
                initial_leverage = 56,
                maint_margin_ratio = 1.337,
                qty_cap = 56,
                qty_floor = 56
            )
        else:
            return GetCmLeverageBracketV1RespItemBracketsInner(
        )
        """

    def testGetCmLeverageBracketV1RespItemBracketsInner(self):
        """Test GetCmLeverageBracketV1RespItemBracketsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
