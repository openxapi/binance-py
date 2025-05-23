# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_sub_account_futures_position_risk_v2_resp import GetSubAccountFuturesPositionRiskV2Resp

class TestGetSubAccountFuturesPositionRiskV2Resp(unittest.TestCase):
    """GetSubAccountFuturesPositionRiskV2Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSubAccountFuturesPositionRiskV2Resp:
        """Test GetSubAccountFuturesPositionRiskV2Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSubAccountFuturesPositionRiskV2Resp`
        """
        model = GetSubAccountFuturesPositionRiskV2Resp()
        if include_optional:
            return GetSubAccountFuturesPositionRiskV2Resp(
                future_position_risk_vos = [
                    binance.spot.models.get_sub_account_futures_position_risk_v2_resp_future_position_risk_vos_inner.GetSubAccountFuturesPositionRiskV2Resp_futurePositionRiskVos_inner(
                        entry_price = '', 
                        leverage = '', 
                        liquidation_price = '', 
                        mark_price = '', 
                        max_notional = '', 
                        position_amount = '', 
                        symbol = '', 
                        unrealized_profit = '', )
                    ]
            )
        else:
            return GetSubAccountFuturesPositionRiskV2Resp(
        )
        """

    def testGetSubAccountFuturesPositionRiskV2Resp(self):
        """Test GetSubAccountFuturesPositionRiskV2Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
