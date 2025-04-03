# coding: utf-8

"""
    Binance Algorithmic Trading API

    OpenAPI specification for Binance exchange - Algo API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.algo.models.algo_create_algo_spot_new_order_twap_v1_resp import AlgoCreateAlgoSpotNewOrderTwapV1Resp

class TestAlgoCreateAlgoSpotNewOrderTwapV1Resp(unittest.TestCase):
    """AlgoCreateAlgoSpotNewOrderTwapV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlgoCreateAlgoSpotNewOrderTwapV1Resp:
        """Test AlgoCreateAlgoSpotNewOrderTwapV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlgoCreateAlgoSpotNewOrderTwapV1Resp`
        """
        model = AlgoCreateAlgoSpotNewOrderTwapV1Resp()
        if include_optional:
            return AlgoCreateAlgoSpotNewOrderTwapV1Resp(
                client_algo_id = '',
                code = 56,
                msg = '',
                success = True
            )
        else:
            return AlgoCreateAlgoSpotNewOrderTwapV1Resp(
        )
        """

    def testAlgoCreateAlgoSpotNewOrderTwapV1Resp(self):
        """Test AlgoCreateAlgoSpotNewOrderTwapV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
