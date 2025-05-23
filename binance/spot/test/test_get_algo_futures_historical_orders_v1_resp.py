# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_algo_futures_historical_orders_v1_resp import GetAlgoFuturesHistoricalOrdersV1Resp

class TestGetAlgoFuturesHistoricalOrdersV1Resp(unittest.TestCase):
    """GetAlgoFuturesHistoricalOrdersV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAlgoFuturesHistoricalOrdersV1Resp:
        """Test GetAlgoFuturesHistoricalOrdersV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAlgoFuturesHistoricalOrdersV1Resp`
        """
        model = GetAlgoFuturesHistoricalOrdersV1Resp()
        if include_optional:
            return GetAlgoFuturesHistoricalOrdersV1Resp(
                orders = [
                    binance.spot.models.get_algo_futures_historical_orders_v1_resp_orders_inner.GetAlgoFuturesHistoricalOrdersV1Resp_orders_inner(
                        algo_id = 56, 
                        algo_status = '', 
                        algo_type = '', 
                        avg_price = '', 
                        book_time = 56, 
                        client_algo_id = '', 
                        end_time = 56, 
                        executed_amt = '', 
                        executed_qty = '', 
                        position_side = '', 
                        side = '', 
                        symbol = '', 
                        total_qty = '', 
                        urgency = '', )
                    ],
                total = 56
            )
        else:
            return GetAlgoFuturesHistoricalOrdersV1Resp(
        )
        """

    def testGetAlgoFuturesHistoricalOrdersV1Resp(self):
        """Test GetAlgoFuturesHistoricalOrdersV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
