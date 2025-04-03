# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_sub_account_futures_account_summary_v2_resp_future_account_summary_resp import SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp

class TestSubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp(unittest.TestCase):
    """SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp:
        """Test SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp`
        """
        model = SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp()
        if include_optional:
            return SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp(
                asset = '',
                sub_account_list = [
                    binance.subaccount.models.subaccount_get_sub_account_futures_account_summary_v1_resp_sub_account_list_inner.SubaccountGetSubAccountFuturesAccountSummaryV1Resp_subAccountList_inner(
                        asset = '', 
                        email = '', 
                        total_initial_margin = '', 
                        total_maintenance_margin = '', 
                        total_margin_balance = '', 
                        total_open_order_initial_margin = '', 
                        total_position_initial_margin = '', 
                        total_unrealized_profit = '', 
                        total_wallet_balance = '', )
                    ],
                total_initial_margin = '',
                total_maintenance_margin = '',
                total_margin_balance = '',
                total_open_order_initial_margin = '',
                total_position_initial_margin = '',
                total_unrealized_profit = '',
                total_wallet_balance = ''
            )
        else:
            return SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp(
        )
        """

    def testSubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp(self):
        """Test SubaccountGetSubAccountFuturesAccountSummaryV2RespFutureAccountSummaryResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
