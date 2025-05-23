# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.cmfutures.models.get_trades_v1_resp_item import GetTradesV1RespItem

class TestGetTradesV1RespItem(unittest.TestCase):
    """GetTradesV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTradesV1RespItem:
        """Test GetTradesV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTradesV1RespItem`
        """
        model = GetTradesV1RespItem()
        if include_optional:
            return GetTradesV1RespItem(
                base_qty = '',
                id = 56,
                is_buyer_maker = True,
                price = '',
                qty = '',
                time = 56
            )
        else:
            return GetTradesV1RespItem(
        )
        """

    def testGetTradesV1RespItem(self):
        """Test GetTradesV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
