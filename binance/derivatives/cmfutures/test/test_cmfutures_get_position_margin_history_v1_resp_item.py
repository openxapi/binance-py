# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.models.cmfutures_get_position_margin_history_v1_resp_item import CmfuturesGetPositionMarginHistoryV1RespItem

class TestCmfuturesGetPositionMarginHistoryV1RespItem(unittest.TestCase):
    """CmfuturesGetPositionMarginHistoryV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmfuturesGetPositionMarginHistoryV1RespItem:
        """Test CmfuturesGetPositionMarginHistoryV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmfuturesGetPositionMarginHistoryV1RespItem`
        """
        model = CmfuturesGetPositionMarginHistoryV1RespItem()
        if include_optional:
            return CmfuturesGetPositionMarginHistoryV1RespItem(
                amount = '',
                asset = '',
                position_side = '',
                symbol = '',
                time = 56,
                type = 56
            )
        else:
            return CmfuturesGetPositionMarginHistoryV1RespItem(
        )
        """

    def testCmfuturesGetPositionMarginHistoryV1RespItem(self):
        """Test CmfuturesGetPositionMarginHistoryV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
