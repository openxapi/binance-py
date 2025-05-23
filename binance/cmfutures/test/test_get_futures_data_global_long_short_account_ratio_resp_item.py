# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.cmfutures.models.get_futures_data_global_long_short_account_ratio_resp_item import GetFuturesDataGlobalLongShortAccountRatioRespItem

class TestGetFuturesDataGlobalLongShortAccountRatioRespItem(unittest.TestCase):
    """GetFuturesDataGlobalLongShortAccountRatioRespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFuturesDataGlobalLongShortAccountRatioRespItem:
        """Test GetFuturesDataGlobalLongShortAccountRatioRespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFuturesDataGlobalLongShortAccountRatioRespItem`
        """
        model = GetFuturesDataGlobalLongShortAccountRatioRespItem()
        if include_optional:
            return GetFuturesDataGlobalLongShortAccountRatioRespItem(
                long_account = '',
                long_short_ratio = '',
                pair = '',
                short_account = '',
                timestamp = 56
            )
        else:
            return GetFuturesDataGlobalLongShortAccountRatioRespItem(
        )
        """

    def testGetFuturesDataGlobalLongShortAccountRatioRespItem(self):
        """Test GetFuturesDataGlobalLongShortAccountRatioRespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
