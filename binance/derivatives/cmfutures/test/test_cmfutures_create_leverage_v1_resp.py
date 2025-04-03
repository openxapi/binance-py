# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.models.cmfutures_create_leverage_v1_resp import CmfuturesCreateLeverageV1Resp

class TestCmfuturesCreateLeverageV1Resp(unittest.TestCase):
    """CmfuturesCreateLeverageV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmfuturesCreateLeverageV1Resp:
        """Test CmfuturesCreateLeverageV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmfuturesCreateLeverageV1Resp`
        """
        model = CmfuturesCreateLeverageV1Resp()
        if include_optional:
            return CmfuturesCreateLeverageV1Resp(
                leverage = 56,
                max_qty = '',
                symbol = ''
            )
        else:
            return CmfuturesCreateLeverageV1Resp(
        )
        """

    def testCmfuturesCreateLeverageV1Resp(self):
        """Test CmfuturesCreateLeverageV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
