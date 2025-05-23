# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.umfutures.models.umfutures_create_countdown_cancel_all_v1_req import UmfuturesCreateCountdownCancelAllV1Req

class TestUmfuturesCreateCountdownCancelAllV1Req(unittest.TestCase):
    """UmfuturesCreateCountdownCancelAllV1Req unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesCreateCountdownCancelAllV1Req:
        """Test UmfuturesCreateCountdownCancelAllV1Req
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesCreateCountdownCancelAllV1Req`
        """
        model = UmfuturesCreateCountdownCancelAllV1Req()
        if include_optional:
            return UmfuturesCreateCountdownCancelAllV1Req(
                countdown_time = 56,
                recv_window = 56,
                symbol = '',
                timestamp = 56
            )
        else:
            return UmfuturesCreateCountdownCancelAllV1Req(
                countdown_time = 56,
                symbol = '',
                timestamp = 56,
        )
        """

    def testUmfuturesCreateCountdownCancelAllV1Req(self):
        """Test UmfuturesCreateCountdownCancelAllV1Req"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
