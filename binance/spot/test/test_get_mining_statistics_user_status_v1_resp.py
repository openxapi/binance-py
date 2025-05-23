# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_mining_statistics_user_status_v1_resp import GetMiningStatisticsUserStatusV1Resp

class TestGetMiningStatisticsUserStatusV1Resp(unittest.TestCase):
    """GetMiningStatisticsUserStatusV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMiningStatisticsUserStatusV1Resp:
        """Test GetMiningStatisticsUserStatusV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMiningStatisticsUserStatusV1Resp`
        """
        model = GetMiningStatisticsUserStatusV1Resp()
        if include_optional:
            return GetMiningStatisticsUserStatusV1Resp(
                code = 56,
                data = binance.spot.models.get_mining_statistics_user_status_v1_resp_data.GetMiningStatisticsUserStatusV1Resp_data(
                    algo = '', 
                    day_hash_rate = '', 
                    fifteen_min_hash_rate = '', 
                    invalid_num = 56, 
                    profit_today = binance.spot.models.get_mining_statistics_user_status_v1_resp_data_profit_today.GetMiningStatisticsUserStatusV1Resp_data_profitToday(
                        bch = '', 
                        bsv = '', 
                        btc = '', ), 
                    profit_yesterday = binance.spot.models.get_mining_statistics_user_status_v1_resp_data_profit_today.GetMiningStatisticsUserStatusV1Resp_data_profitToday(
                        bch = '', 
                        bsv = '', 
                        btc = '', ), 
                    unit = '', 
                    user_name = '', 
                    valid_num = 56, ),
                msg = ''
            )
        else:
            return GetMiningStatisticsUserStatusV1Resp(
        )
        """

    def testGetMiningStatisticsUserStatusV1Resp(self):
        """Test GetMiningStatisticsUserStatusV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
