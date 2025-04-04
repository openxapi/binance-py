# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_get_margin_all_assets_v1_resp_item import MarginGetMarginAllAssetsV1RespItem

class TestMarginGetMarginAllAssetsV1RespItem(unittest.TestCase):
    """MarginGetMarginAllAssetsV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginGetMarginAllAssetsV1RespItem:
        """Test MarginGetMarginAllAssetsV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginGetMarginAllAssetsV1RespItem`
        """
        model = MarginGetMarginAllAssetsV1RespItem()
        if include_optional:
            return MarginGetMarginAllAssetsV1RespItem(
                asset_full_name = '',
                asset_name = '',
                delist_time = 56,
                is_borrowable = True,
                is_mortgageable = True,
                user_min_borrow = '',
                user_min_repay = ''
            )
        else:
            return MarginGetMarginAllAssetsV1RespItem(
        )
        """

    def testMarginGetMarginAllAssetsV1RespItem(self):
        """Test MarginGetMarginAllAssetsV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
