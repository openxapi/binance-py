# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.spot_get_my_prevented_matches_v3_resp_item import SpotGetMyPreventedMatchesV3RespItem

class TestSpotGetMyPreventedMatchesV3RespItem(unittest.TestCase):
    """SpotGetMyPreventedMatchesV3RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotGetMyPreventedMatchesV3RespItem:
        """Test SpotGetMyPreventedMatchesV3RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotGetMyPreventedMatchesV3RespItem`
        """
        model = SpotGetMyPreventedMatchesV3RespItem()
        if include_optional:
            return SpotGetMyPreventedMatchesV3RespItem(
                maker_order_id = 56,
                maker_prevented_quantity = '',
                maker_symbol = '',
                prevented_match_id = 56,
                price = '',
                self_trade_prevention_mode = '',
                symbol = '',
                taker_order_id = 56,
                trade_group_id = 56,
                transact_time = 56
            )
        else:
            return SpotGetMyPreventedMatchesV3RespItem(
        )
        """

    def testSpotGetMyPreventedMatchesV3RespItem(self):
        """Test SpotGetMyPreventedMatchesV3RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
