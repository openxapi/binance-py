# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.spot_get_exchange_info_v3_resp_sors_inner import SpotGetExchangeInfoV3RespSorsInner

class TestSpotGetExchangeInfoV3RespSorsInner(unittest.TestCase):
    """SpotGetExchangeInfoV3RespSorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotGetExchangeInfoV3RespSorsInner:
        """Test SpotGetExchangeInfoV3RespSorsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotGetExchangeInfoV3RespSorsInner`
        """
        model = SpotGetExchangeInfoV3RespSorsInner()
        if include_optional:
            return SpotGetExchangeInfoV3RespSorsInner(
                base_asset = '',
                symbols = [
                    ''
                    ]
            )
        else:
            return SpotGetExchangeInfoV3RespSorsInner(
        )
        """

    def testSpotGetExchangeInfoV3RespSorsInner(self):
        """Test SpotGetExchangeInfoV3RespSorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
