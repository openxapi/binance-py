# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.models.cmfutures_create_listen_key_v1_resp import CmfuturesCreateListenKeyV1Resp

class TestCmfuturesCreateListenKeyV1Resp(unittest.TestCase):
    """CmfuturesCreateListenKeyV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmfuturesCreateListenKeyV1Resp:
        """Test CmfuturesCreateListenKeyV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmfuturesCreateListenKeyV1Resp`
        """
        model = CmfuturesCreateListenKeyV1Resp()
        if include_optional:
            return CmfuturesCreateListenKeyV1Resp(
                listen_key = ''
            )
        else:
            return CmfuturesCreateListenKeyV1Resp(
        )
        """

    def testCmfuturesCreateListenKeyV1Resp(self):
        """Test CmfuturesCreateListenKeyV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
