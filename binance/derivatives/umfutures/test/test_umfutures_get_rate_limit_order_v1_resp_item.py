# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_rate_limit_order_v1_resp_item import UmfuturesGetRateLimitOrderV1RespItem

class TestUmfuturesGetRateLimitOrderV1RespItem(unittest.TestCase):
    """UmfuturesGetRateLimitOrderV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetRateLimitOrderV1RespItem:
        """Test UmfuturesGetRateLimitOrderV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetRateLimitOrderV1RespItem`
        """
        model = UmfuturesGetRateLimitOrderV1RespItem()
        if include_optional:
            return UmfuturesGetRateLimitOrderV1RespItem(
                interval = '',
                interval_num = 56,
                limit = 56,
                rate_limit_type = ''
            )
        else:
            return UmfuturesGetRateLimitOrderV1RespItem(
        )
        """

    def testUmfuturesGetRateLimitOrderV1RespItem(self):
        """Test UmfuturesGetRateLimitOrderV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
