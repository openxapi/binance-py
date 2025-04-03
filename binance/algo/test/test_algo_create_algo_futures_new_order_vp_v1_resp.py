# coding: utf-8

"""
    Binance Algorithmic Trading API

    OpenAPI specification for Binance exchange - Algo API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.algo.models.algo_create_algo_futures_new_order_vp_v1_resp import AlgoCreateAlgoFuturesNewOrderVpV1Resp

class TestAlgoCreateAlgoFuturesNewOrderVpV1Resp(unittest.TestCase):
    """AlgoCreateAlgoFuturesNewOrderVpV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlgoCreateAlgoFuturesNewOrderVpV1Resp:
        """Test AlgoCreateAlgoFuturesNewOrderVpV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlgoCreateAlgoFuturesNewOrderVpV1Resp`
        """
        model = AlgoCreateAlgoFuturesNewOrderVpV1Resp()
        if include_optional:
            return AlgoCreateAlgoFuturesNewOrderVpV1Resp(
                client_algo_id = '',
                code = 56,
                msg = '',
                success = True
            )
        else:
            return AlgoCreateAlgoFuturesNewOrderVpV1Resp(
        )
        """

    def testAlgoCreateAlgoFuturesNewOrderVpV1Resp(self):
        """Test AlgoCreateAlgoFuturesNewOrderVpV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
