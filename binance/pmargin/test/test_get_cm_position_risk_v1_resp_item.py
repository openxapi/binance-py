# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.pmargin.models.get_cm_position_risk_v1_resp_item import GetCmPositionRiskV1RespItem

class TestGetCmPositionRiskV1RespItem(unittest.TestCase):
    """GetCmPositionRiskV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCmPositionRiskV1RespItem:
        """Test GetCmPositionRiskV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCmPositionRiskV1RespItem`
        """
        model = GetCmPositionRiskV1RespItem()
        if include_optional:
            return GetCmPositionRiskV1RespItem(
                entry_price = '',
                leverage = '',
                liquidation_price = '',
                mark_price = '',
                max_qty = '',
                notional_value = '',
                position_amt = '',
                position_side = '',
                symbol = '',
                un_realized_profit = '',
                update_time = 56
            )
        else:
            return GetCmPositionRiskV1RespItem(
        )
        """

    def testGetCmPositionRiskV1RespItem(self):
        """Test GetCmPositionRiskV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
