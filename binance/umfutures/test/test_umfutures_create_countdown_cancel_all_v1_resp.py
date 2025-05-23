# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.umfutures.models.umfutures_create_countdown_cancel_all_v1_resp import UmfuturesCreateCountdownCancelAllV1Resp

class TestUmfuturesCreateCountdownCancelAllV1Resp(unittest.TestCase):
    """UmfuturesCreateCountdownCancelAllV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesCreateCountdownCancelAllV1Resp:
        """Test UmfuturesCreateCountdownCancelAllV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesCreateCountdownCancelAllV1Resp`
        """
        model = UmfuturesCreateCountdownCancelAllV1Resp()
        if include_optional:
            return UmfuturesCreateCountdownCancelAllV1Resp(
                countdown_time = '',
                symbol = ''
            )
        else:
            return UmfuturesCreateCountdownCancelAllV1Resp(
        )
        """

    def testUmfuturesCreateCountdownCancelAllV1Resp(self):
        """Test UmfuturesCreateCountdownCancelAllV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
