# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.spot_get_trades_v3_resp_item import SpotGetTradesV3RespItem

class TestSpotGetTradesV3RespItem(unittest.TestCase):
    """SpotGetTradesV3RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotGetTradesV3RespItem:
        """Test SpotGetTradesV3RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotGetTradesV3RespItem`
        """
        model = SpotGetTradesV3RespItem()
        if include_optional:
            return SpotGetTradesV3RespItem(
                id = 56,
                is_best_match = True,
                is_buyer_maker = True,
                price = '',
                qty = '',
                quote_qty = '',
                time = 56
            )
        else:
            return SpotGetTradesV3RespItem(
        )
        """

    def testSpotGetTradesV3RespItem(self):
        """Test SpotGetTradesV3RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
