# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_get_margin_leverage_bracket_v1_resp_item_brackets_inner import MarginGetMarginLeverageBracketV1RespItemBracketsInner

class TestMarginGetMarginLeverageBracketV1RespItemBracketsInner(unittest.TestCase):
    """MarginGetMarginLeverageBracketV1RespItemBracketsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginGetMarginLeverageBracketV1RespItemBracketsInner:
        """Test MarginGetMarginLeverageBracketV1RespItemBracketsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginGetMarginLeverageBracketV1RespItemBracketsInner`
        """
        model = MarginGetMarginLeverageBracketV1RespItemBracketsInner()
        if include_optional:
            return MarginGetMarginLeverageBracketV1RespItemBracketsInner(
                fast_num = 56,
                initial_margin_rate = 1.337,
                leverage = 56,
                maintenance_margin_rate = 1.337,
                max_debt = 56
            )
        else:
            return MarginGetMarginLeverageBracketV1RespItemBracketsInner(
        )
        """

    def testMarginGetMarginLeverageBracketV1RespItemBracketsInner(self):
        """Test MarginGetMarginLeverageBracketV1RespItemBracketsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
