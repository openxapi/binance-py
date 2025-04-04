# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_futures_data_top_long_short_account_ratio_resp_item import UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem

class TestUmfuturesGetFuturesDataTopLongShortAccountRatioRespItem(unittest.TestCase):
    """UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem:
        """Test UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem`
        """
        model = UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem()
        if include_optional:
            return UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem(
                long_account = '',
                long_short_ratio = '',
                short_account = '',
                symbol = '',
                timestamp = ''
            )
        else:
            return UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem(
        )
        """

    def testUmfuturesGetFuturesDataTopLongShortAccountRatioRespItem(self):
        """Test UmfuturesGetFuturesDataTopLongShortAccountRatioRespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
