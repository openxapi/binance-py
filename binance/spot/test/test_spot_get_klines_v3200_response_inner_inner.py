# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.spot_get_klines_v3200_response_inner_inner import SpotGetKlinesV3200ResponseInnerInner

class TestSpotGetKlinesV3200ResponseInnerInner(unittest.TestCase):
    """SpotGetKlinesV3200ResponseInnerInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotGetKlinesV3200ResponseInnerInner:
        """Test SpotGetKlinesV3200ResponseInnerInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotGetKlinesV3200ResponseInnerInner`
        """
        model = SpotGetKlinesV3200ResponseInnerInner()
        if include_optional:
            return SpotGetKlinesV3200ResponseInnerInner(
            )
        else:
            return SpotGetKlinesV3200ResponseInnerInner(
        )
        """

    def testSpotGetKlinesV3200ResponseInnerInner(self):
        """Test SpotGetKlinesV3200ResponseInnerInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
