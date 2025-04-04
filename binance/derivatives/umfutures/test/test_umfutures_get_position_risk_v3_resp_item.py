# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_position_risk_v3_resp_item import UmfuturesGetPositionRiskV3RespItem

class TestUmfuturesGetPositionRiskV3RespItem(unittest.TestCase):
    """UmfuturesGetPositionRiskV3RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetPositionRiskV3RespItem:
        """Test UmfuturesGetPositionRiskV3RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetPositionRiskV3RespItem`
        """
        model = UmfuturesGetPositionRiskV3RespItem()
        if include_optional:
            return UmfuturesGetPositionRiskV3RespItem(
                adl = 56,
                ask_notional = '',
                bid_notional = '',
                break_even_price = '',
                entry_price = '',
                initial_margin = '',
                isolated_margin = '',
                isolated_wallet = '',
                liquidation_price = '',
                maint_margin = '',
                margin_asset = '',
                mark_price = '',
                notional = '',
                open_order_initial_margin = '',
                position_amt = '',
                position_initial_margin = '',
                position_side = '',
                symbol = '',
                un_realized_profit = '',
                update_time = 56
            )
        else:
            return UmfuturesGetPositionRiskV3RespItem(
        )
        """

    def testUmfuturesGetPositionRiskV3RespItem(self):
        """Test UmfuturesGetPositionRiskV3RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
