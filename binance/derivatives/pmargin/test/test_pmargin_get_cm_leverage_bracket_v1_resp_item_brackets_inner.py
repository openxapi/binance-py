# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_cm_leverage_bracket_v1_resp_item_brackets_inner import PmarginGetCmLeverageBracketV1RespItemBracketsInner

class TestPmarginGetCmLeverageBracketV1RespItemBracketsInner(unittest.TestCase):
    """PmarginGetCmLeverageBracketV1RespItemBracketsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetCmLeverageBracketV1RespItemBracketsInner:
        """Test PmarginGetCmLeverageBracketV1RespItemBracketsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetCmLeverageBracketV1RespItemBracketsInner`
        """
        model = PmarginGetCmLeverageBracketV1RespItemBracketsInner()
        if include_optional:
            return PmarginGetCmLeverageBracketV1RespItemBracketsInner(
                bracket = 56,
                cum = 56,
                initial_leverage = 56,
                maint_margin_ratio = 1.337,
                qty_cap = 56,
                qty_floor = 56
            )
        else:
            return PmarginGetCmLeverageBracketV1RespItemBracketsInner(
        )
        """

    def testPmarginGetCmLeverageBracketV1RespItemBracketsInner(self):
        """Test PmarginGetCmLeverageBracketV1RespItemBracketsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
