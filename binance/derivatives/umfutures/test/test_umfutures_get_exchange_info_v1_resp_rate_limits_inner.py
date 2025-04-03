# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp_rate_limits_inner import UmfuturesGetExchangeInfoV1RespRateLimitsInner

class TestUmfuturesGetExchangeInfoV1RespRateLimitsInner(unittest.TestCase):
    """UmfuturesGetExchangeInfoV1RespRateLimitsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetExchangeInfoV1RespRateLimitsInner:
        """Test UmfuturesGetExchangeInfoV1RespRateLimitsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetExchangeInfoV1RespRateLimitsInner`
        """
        model = UmfuturesGetExchangeInfoV1RespRateLimitsInner()
        if include_optional:
            return UmfuturesGetExchangeInfoV1RespRateLimitsInner(
                interval = '',
                interval_num = 56,
                limit = 56,
                rate_limit_type = ''
            )
        else:
            return UmfuturesGetExchangeInfoV1RespRateLimitsInner(
        )
        """

    def testUmfuturesGetExchangeInfoV1RespRateLimitsInner(self):
        """Test UmfuturesGetExchangeInfoV1RespRateLimitsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
