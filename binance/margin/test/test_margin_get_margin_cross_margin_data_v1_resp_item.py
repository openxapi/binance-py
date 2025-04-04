# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_get_margin_cross_margin_data_v1_resp_item import MarginGetMarginCrossMarginDataV1RespItem

class TestMarginGetMarginCrossMarginDataV1RespItem(unittest.TestCase):
    """MarginGetMarginCrossMarginDataV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginGetMarginCrossMarginDataV1RespItem:
        """Test MarginGetMarginCrossMarginDataV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginGetMarginCrossMarginDataV1RespItem`
        """
        model = MarginGetMarginCrossMarginDataV1RespItem()
        if include_optional:
            return MarginGetMarginCrossMarginDataV1RespItem(
                borrow_limit = '',
                borrowable = True,
                coin = '',
                daily_interest = '',
                marginable_pairs = [
                    ''
                    ],
                transfer_in = True,
                vip_level = 56,
                yearly_interest = ''
            )
        else:
            return MarginGetMarginCrossMarginDataV1RespItem(
        )
        """

    def testMarginGetMarginCrossMarginDataV1RespItem(self):
        """Test MarginGetMarginCrossMarginDataV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
