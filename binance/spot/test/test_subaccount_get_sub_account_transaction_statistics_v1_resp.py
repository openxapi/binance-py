# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.subaccount_get_sub_account_transaction_statistics_v1_resp import SubaccountGetSubAccountTransactionStatisticsV1Resp

class TestSubaccountGetSubAccountTransactionStatisticsV1Resp(unittest.TestCase):
    """SubaccountGetSubAccountTransactionStatisticsV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetSubAccountTransactionStatisticsV1Resp:
        """Test SubaccountGetSubAccountTransactionStatisticsV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetSubAccountTransactionStatisticsV1Resp`
        """
        model = SubaccountGetSubAccountTransactionStatisticsV1Resp()
        if include_optional:
            return SubaccountGetSubAccountTransactionStatisticsV1Resp(
                recent30_btc_futures_total = '',
                recent30_btc_margin_total = '',
                recent30_btc_total = '',
                recent30_busd_futures_total = '',
                recent30_busd_margin_total = '',
                recent30_busd_total = '',
                trade_info_vos = [
                    binance.spot.models.subaccount_get_sub_account_transaction_statistics_v1_resp_trade_info_vos_inner.SubaccountGetSubAccountTransactionStatisticsV1Resp_tradeInfoVos_inner(
                        btc = 56, 
                        btc_futures = 56, 
                        btc_margin = 56, 
                        busd = 56, 
                        busd_futures = 56, 
                        busd_margin = 56, 
                        date = 56, 
                        user_id = 56, )
                    ]
            )
        else:
            return SubaccountGetSubAccountTransactionStatisticsV1Resp(
        )
        """

    def testSubaccountGetSubAccountTransactionStatisticsV1Resp(self):
        """Test SubaccountGetSubAccountTransactionStatisticsV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
