# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_margin_interest_rate_history_v1_resp_item import GetMarginInterestRateHistoryV1RespItem

class TestGetMarginInterestRateHistoryV1RespItem(unittest.TestCase):
    """GetMarginInterestRateHistoryV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMarginInterestRateHistoryV1RespItem:
        """Test GetMarginInterestRateHistoryV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMarginInterestRateHistoryV1RespItem`
        """
        model = GetMarginInterestRateHistoryV1RespItem()
        if include_optional:
            return GetMarginInterestRateHistoryV1RespItem(
                asset = '',
                daily_interest_rate = '',
                timestamp = 56,
                vip_level = 56
            )
        else:
            return GetMarginInterestRateHistoryV1RespItem(
        )
        """

    def testGetMarginInterestRateHistoryV1RespItem(self):
        """Test GetMarginInterestRateHistoryV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
