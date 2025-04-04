# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_adl_quantile_v1_resp_item_adl_quantile import UmfuturesGetAdlQuantileV1RespItemAdlQuantile

class TestUmfuturesGetAdlQuantileV1RespItemAdlQuantile(unittest.TestCase):
    """UmfuturesGetAdlQuantileV1RespItemAdlQuantile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetAdlQuantileV1RespItemAdlQuantile:
        """Test UmfuturesGetAdlQuantileV1RespItemAdlQuantile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetAdlQuantileV1RespItemAdlQuantile`
        """
        model = UmfuturesGetAdlQuantileV1RespItemAdlQuantile()
        if include_optional:
            return UmfuturesGetAdlQuantileV1RespItemAdlQuantile(
                hedge = 56,
                long = 56,
                short = 56
            )
        else:
            return UmfuturesGetAdlQuantileV1RespItemAdlQuantile(
        )
        """

    def testUmfuturesGetAdlQuantileV1RespItemAdlQuantile(self):
        """Test UmfuturesGetAdlQuantileV1RespItemAdlQuantile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
