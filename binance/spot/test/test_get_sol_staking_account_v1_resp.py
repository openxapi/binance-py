# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_sol_staking_account_v1_resp import GetSolStakingAccountV1Resp

class TestGetSolStakingAccountV1Resp(unittest.TestCase):
    """GetSolStakingAccountV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSolStakingAccountV1Resp:
        """Test GetSolStakingAccountV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSolStakingAccountV1Resp`
        """
        model = GetSolStakingAccountV1Resp()
        if include_optional:
            return GetSolStakingAccountV1Resp(
                bnsol_amount = '',
                holding_in_sol = '',
                thirty_days_profit_in_sol = ''
            )
        else:
            return GetSolStakingAccountV1Resp(
        )
        """

    def testGetSolStakingAccountV1Resp(self):
        """Test GetSolStakingAccountV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
