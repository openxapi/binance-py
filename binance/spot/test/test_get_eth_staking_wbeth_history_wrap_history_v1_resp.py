# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_eth_staking_wbeth_history_wrap_history_v1_resp import GetEthStakingWbethHistoryWrapHistoryV1Resp

class TestGetEthStakingWbethHistoryWrapHistoryV1Resp(unittest.TestCase):
    """GetEthStakingWbethHistoryWrapHistoryV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetEthStakingWbethHistoryWrapHistoryV1Resp:
        """Test GetEthStakingWbethHistoryWrapHistoryV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEthStakingWbethHistoryWrapHistoryV1Resp`
        """
        model = GetEthStakingWbethHistoryWrapHistoryV1Resp()
        if include_optional:
            return GetEthStakingWbethHistoryWrapHistoryV1Resp(
                rows = [
                    binance.spot.models.get_eth_staking_wbeth_history_unwrap_history_v1_resp_rows_inner.GetEthStakingWbethHistoryUnwrapHistoryV1Resp_rows_inner(
                        exchange_rate = '', 
                        from_amount = '', 
                        from_asset = '', 
                        status = '', 
                        time = 56, 
                        to_amount = '', 
                        to_asset = '', )
                    ],
                total = 56
            )
        else:
            return GetEthStakingWbethHistoryWrapHistoryV1Resp(
        )
        """

    def testGetEthStakingWbethHistoryWrapHistoryV1Resp(self):
        """Test GetEthStakingWbethHistoryWrapHistoryV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
