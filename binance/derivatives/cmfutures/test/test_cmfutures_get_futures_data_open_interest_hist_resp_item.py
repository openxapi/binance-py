# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.models.cmfutures_get_futures_data_open_interest_hist_resp_item import CmfuturesGetFuturesDataOpenInterestHistRespItem

class TestCmfuturesGetFuturesDataOpenInterestHistRespItem(unittest.TestCase):
    """CmfuturesGetFuturesDataOpenInterestHistRespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmfuturesGetFuturesDataOpenInterestHistRespItem:
        """Test CmfuturesGetFuturesDataOpenInterestHistRespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmfuturesGetFuturesDataOpenInterestHistRespItem`
        """
        model = CmfuturesGetFuturesDataOpenInterestHistRespItem()
        if include_optional:
            return CmfuturesGetFuturesDataOpenInterestHistRespItem(
                contract_type = '',
                pair = '',
                sum_open_interest = '',
                sum_open_interest_value = '',
                timestamp = 56
            )
        else:
            return CmfuturesGetFuturesDataOpenInterestHistRespItem(
        )
        """

    def testCmfuturesGetFuturesDataOpenInterestHistRespItem(self):
        """Test CmfuturesGetFuturesDataOpenInterestHistRespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
