# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_eth_staking_eth_history_rate_history_v1_resp_rows_inner import GetEthStakingEthHistoryRateHistoryV1RespRowsInner

class TestGetEthStakingEthHistoryRateHistoryV1RespRowsInner(unittest.TestCase):
    """GetEthStakingEthHistoryRateHistoryV1RespRowsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetEthStakingEthHistoryRateHistoryV1RespRowsInner:
        """Test GetEthStakingEthHistoryRateHistoryV1RespRowsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEthStakingEthHistoryRateHistoryV1RespRowsInner`
        """
        model = GetEthStakingEthHistoryRateHistoryV1RespRowsInner()
        if include_optional:
            return GetEthStakingEthHistoryRateHistoryV1RespRowsInner(
                annual_percentage_rate = '',
                exchange_rate = '',
                time = 56
            )
        else:
            return GetEthStakingEthHistoryRateHistoryV1RespRowsInner(
        )
        """

    def testGetEthStakingEthHistoryRateHistoryV1RespRowsInner(self):
        """Test GetEthStakingEthHistoryRateHistoryV1RespRowsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
