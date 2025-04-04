# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_sub_account_margin_account_summary_v1_resp_sub_account_list_inner import SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner

class TestSubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner(unittest.TestCase):
    """SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner:
        """Test SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner`
        """
        model = SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner()
        if include_optional:
            return SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner(
                email = '',
                total_asset_of_btc = '',
                total_liability_of_btc = '',
                total_net_asset_of_btc = ''
            )
        else:
            return SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner(
        )
        """

    def testSubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner(self):
        """Test SubaccountGetSubAccountMarginAccountSummaryV1RespSubAccountListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
