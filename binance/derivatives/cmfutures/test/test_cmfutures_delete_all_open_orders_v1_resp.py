# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.models.cmfutures_delete_all_open_orders_v1_resp import CmfuturesDeleteAllOpenOrdersV1Resp

class TestCmfuturesDeleteAllOpenOrdersV1Resp(unittest.TestCase):
    """CmfuturesDeleteAllOpenOrdersV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmfuturesDeleteAllOpenOrdersV1Resp:
        """Test CmfuturesDeleteAllOpenOrdersV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmfuturesDeleteAllOpenOrdersV1Resp`
        """
        model = CmfuturesDeleteAllOpenOrdersV1Resp()
        if include_optional:
            return CmfuturesDeleteAllOpenOrdersV1Resp(
                code = 56,
                msg = ''
            )
        else:
            return CmfuturesDeleteAllOpenOrdersV1Resp(
        )
        """

    def testCmfuturesDeleteAllOpenOrdersV1Resp(self):
        """Test CmfuturesDeleteAllOpenOrdersV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
