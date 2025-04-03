# coding: utf-8

"""
    Binance Algorithmic Trading API

    OpenAPI specification for Binance exchange - Algo API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.algo.models.algo_get_algo_spot_historical_orders_v1_resp_orders_inner import AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner

class TestAlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner(unittest.TestCase):
    """AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner:
        """Test AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner`
        """
        model = AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner()
        if include_optional:
            return AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner(
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
                urgency = ''
            )
        else:
            return AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner(
        )
        """

    def testAlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner(self):
        """Test AlgoGetAlgoSpotHistoricalOrdersV1RespOrdersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
