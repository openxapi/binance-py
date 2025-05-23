# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_eth_staking_account_v2_resp_profit import GetEthStakingAccountV2RespProfit

class TestGetEthStakingAccountV2RespProfit(unittest.TestCase):
    """GetEthStakingAccountV2RespProfit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetEthStakingAccountV2RespProfit:
        """Test GetEthStakingAccountV2RespProfit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEthStakingAccountV2RespProfit`
        """
        model = GetEthStakingAccountV2RespProfit()
        if include_optional:
            return GetEthStakingAccountV2RespProfit(
                amount_from_beth = '',
                amount_from_wbeth = ''
            )
        else:
            return GetEthStakingAccountV2RespProfit(
        )
        """

    def testGetEthStakingAccountV2RespProfit(self):
        """Test GetEthStakingAccountV2RespProfit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
