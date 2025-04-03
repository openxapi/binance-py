# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_get_margin_all_pairs_v1_resp_item import MarginGetMarginAllPairsV1RespItem

class TestMarginGetMarginAllPairsV1RespItem(unittest.TestCase):
    """MarginGetMarginAllPairsV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginGetMarginAllPairsV1RespItem:
        """Test MarginGetMarginAllPairsV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginGetMarginAllPairsV1RespItem`
        """
        model = MarginGetMarginAllPairsV1RespItem()
        if include_optional:
            return MarginGetMarginAllPairsV1RespItem(
                base = '',
                id = 56,
                is_buy_allowed = True,
                is_margin_trade = True,
                is_sell_allowed = True,
                quote = '',
                symbol = ''
            )
        else:
            return MarginGetMarginAllPairsV1RespItem(
        )
        """

    def testMarginGetMarginAllPairsV1RespItem(self):
        """Test MarginGetMarginAllPairsV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
