# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_sol_staking_sol_claim_v1_resp import CreateSolStakingSolClaimV1Resp

class TestCreateSolStakingSolClaimV1Resp(unittest.TestCase):
    """CreateSolStakingSolClaimV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSolStakingSolClaimV1Resp:
        """Test CreateSolStakingSolClaimV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSolStakingSolClaimV1Resp`
        """
        model = CreateSolStakingSolClaimV1Resp()
        if include_optional:
            return CreateSolStakingSolClaimV1Resp(
                success = True
            )
        else:
            return CreateSolStakingSolClaimV1Resp(
        )
        """

    def testCreateSolStakingSolClaimV1Resp(self):
        """Test CreateSolStakingSolClaimV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
