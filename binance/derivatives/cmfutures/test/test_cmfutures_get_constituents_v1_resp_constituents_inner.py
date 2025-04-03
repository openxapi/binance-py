# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.models.cmfutures_get_constituents_v1_resp_constituents_inner import CmfuturesGetConstituentsV1RespConstituentsInner

class TestCmfuturesGetConstituentsV1RespConstituentsInner(unittest.TestCase):
    """CmfuturesGetConstituentsV1RespConstituentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmfuturesGetConstituentsV1RespConstituentsInner:
        """Test CmfuturesGetConstituentsV1RespConstituentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmfuturesGetConstituentsV1RespConstituentsInner`
        """
        model = CmfuturesGetConstituentsV1RespConstituentsInner()
        if include_optional:
            return CmfuturesGetConstituentsV1RespConstituentsInner(
                exchange = '',
                symbol = ''
            )
        else:
            return CmfuturesGetConstituentsV1RespConstituentsInner(
        )
        """

    def testCmfuturesGetConstituentsV1RespConstituentsInner(self):
        """Test CmfuturesGetConstituentsV1RespConstituentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
