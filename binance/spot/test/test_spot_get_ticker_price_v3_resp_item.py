# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.spot_get_ticker_price_v3_resp_item import SpotGetTickerPriceV3RespItem

class TestSpotGetTickerPriceV3RespItem(unittest.TestCase):
    """SpotGetTickerPriceV3RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotGetTickerPriceV3RespItem:
        """Test SpotGetTickerPriceV3RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotGetTickerPriceV3RespItem`
        """
        model = SpotGetTickerPriceV3RespItem()
        if include_optional:
            return SpotGetTickerPriceV3RespItem(
                price = '',
                symbol = ''
            )
        else:
            return SpotGetTickerPriceV3RespItem(
        )
        """

    def testSpotGetTickerPriceV3RespItem(self):
        """Test SpotGetTickerPriceV3RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
