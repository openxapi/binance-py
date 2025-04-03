# coding: utf-8

"""
    Binance Algorithmic Trading API

    OpenAPI specification for Binance exchange - Algo API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.algo.models.algo_get_algo_spot_historical_orders_v1_resp import AlgoGetAlgoSpotHistoricalOrdersV1Resp

class TestAlgoGetAlgoSpotHistoricalOrdersV1Resp(unittest.TestCase):
    """AlgoGetAlgoSpotHistoricalOrdersV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlgoGetAlgoSpotHistoricalOrdersV1Resp:
        """Test AlgoGetAlgoSpotHistoricalOrdersV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlgoGetAlgoSpotHistoricalOrdersV1Resp`
        """
        model = AlgoGetAlgoSpotHistoricalOrdersV1Resp()
        if include_optional:
            return AlgoGetAlgoSpotHistoricalOrdersV1Resp(
                orders = [
                    binance.algo.models.algo_get_algo_spot_historical_orders_v1_resp_orders_inner.AlgoGetAlgoSpotHistoricalOrdersV1Resp_orders_inner(
                        algo_id = 56, 
                        algo_status = '', 
                        algo_type = '', 
                        avg_price = '', 
                        book_time = 56, 
                        client_algo_id = '', 
                        end_time = 56, 
                        executed_amt = '', 
                        executed_qty = '', 
                        side = '', 
                        symbol = '', 
                        total_qty = '', 
                        urgency = '', )
                    ],
                total = 56
            )
        else:
            return AlgoGetAlgoSpotHistoricalOrdersV1Resp(
        )
        """

    def testAlgoGetAlgoSpotHistoricalOrdersV1Resp(self):
        """Test AlgoGetAlgoSpotHistoricalOrdersV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
