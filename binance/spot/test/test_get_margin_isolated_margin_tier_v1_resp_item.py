# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_margin_isolated_margin_tier_v1_resp_item import GetMarginIsolatedMarginTierV1RespItem

class TestGetMarginIsolatedMarginTierV1RespItem(unittest.TestCase):
    """GetMarginIsolatedMarginTierV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMarginIsolatedMarginTierV1RespItem:
        """Test GetMarginIsolatedMarginTierV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMarginIsolatedMarginTierV1RespItem`
        """
        model = GetMarginIsolatedMarginTierV1RespItem()
        if include_optional:
            return GetMarginIsolatedMarginTierV1RespItem(
                base_asset_max_borrowable = '',
                effective_multiple = '',
                initial_risk_ratio = '',
                liquidation_risk_ratio = '',
                quote_asset_max_borrowable = '',
                symbol = '',
                tier = 56
            )
        else:
            return GetMarginIsolatedMarginTierV1RespItem(
        )
        """

    def testGetMarginIsolatedMarginTierV1RespItem(self):
        """Test GetMarginIsolatedMarginTierV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
