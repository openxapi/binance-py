# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_funding_info_v1_resp_item import UmfuturesGetFundingInfoV1RespItem

class TestUmfuturesGetFundingInfoV1RespItem(unittest.TestCase):
    """UmfuturesGetFundingInfoV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetFundingInfoV1RespItem:
        """Test UmfuturesGetFundingInfoV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetFundingInfoV1RespItem`
        """
        model = UmfuturesGetFundingInfoV1RespItem()
        if include_optional:
            return UmfuturesGetFundingInfoV1RespItem(
                adjusted_funding_rate_cap = '',
                adjusted_funding_rate_floor = '',
                disclaimer = True,
                funding_interval_hours = 56,
                symbol = ''
            )
        else:
            return UmfuturesGetFundingInfoV1RespItem(
        )
        """

    def testUmfuturesGetFundingInfoV1RespItem(self):
        """Test UmfuturesGetFundingInfoV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
