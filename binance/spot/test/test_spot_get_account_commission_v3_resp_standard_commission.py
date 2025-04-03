# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.spot_get_account_commission_v3_resp_standard_commission import SpotGetAccountCommissionV3RespStandardCommission

class TestSpotGetAccountCommissionV3RespStandardCommission(unittest.TestCase):
    """SpotGetAccountCommissionV3RespStandardCommission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotGetAccountCommissionV3RespStandardCommission:
        """Test SpotGetAccountCommissionV3RespStandardCommission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotGetAccountCommissionV3RespStandardCommission`
        """
        model = SpotGetAccountCommissionV3RespStandardCommission()
        if include_optional:
            return SpotGetAccountCommissionV3RespStandardCommission(
                buyer = '',
                maker = '',
                seller = '',
                taker = ''
            )
        else:
            return SpotGetAccountCommissionV3RespStandardCommission(
        )
        """

    def testSpotGetAccountCommissionV3RespStandardCommission(self):
        """Test SpotGetAccountCommissionV3RespStandardCommission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
