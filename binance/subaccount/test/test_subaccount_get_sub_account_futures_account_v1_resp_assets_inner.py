# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_sub_account_futures_account_v1_resp_assets_inner import SubaccountGetSubAccountFuturesAccountV1RespAssetsInner

class TestSubaccountGetSubAccountFuturesAccountV1RespAssetsInner(unittest.TestCase):
    """SubaccountGetSubAccountFuturesAccountV1RespAssetsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetSubAccountFuturesAccountV1RespAssetsInner:
        """Test SubaccountGetSubAccountFuturesAccountV1RespAssetsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetSubAccountFuturesAccountV1RespAssetsInner`
        """
        model = SubaccountGetSubAccountFuturesAccountV1RespAssetsInner()
        if include_optional:
            return SubaccountGetSubAccountFuturesAccountV1RespAssetsInner(
                asset = '',
                initial_margin = '',
                maintenance_margin = '',
                margin_balance = '',
                max_withdraw_amount = '',
                open_order_initial_margin = '',
                position_initial_margin = '',
                unrealized_profit = '',
                wallet_balance = ''
            )
        else:
            return SubaccountGetSubAccountFuturesAccountV1RespAssetsInner(
        )
        """

    def testSubaccountGetSubAccountFuturesAccountV1RespAssetsInner(self):
        """Test SubaccountGetSubAccountFuturesAccountV1RespAssetsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
