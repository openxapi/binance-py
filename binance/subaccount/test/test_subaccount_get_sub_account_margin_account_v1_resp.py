# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_sub_account_margin_account_v1_resp import SubaccountGetSubAccountMarginAccountV1Resp

class TestSubaccountGetSubAccountMarginAccountV1Resp(unittest.TestCase):
    """SubaccountGetSubAccountMarginAccountV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetSubAccountMarginAccountV1Resp:
        """Test SubaccountGetSubAccountMarginAccountV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetSubAccountMarginAccountV1Resp`
        """
        model = SubaccountGetSubAccountMarginAccountV1Resp()
        if include_optional:
            return SubaccountGetSubAccountMarginAccountV1Resp(
                email = '',
                margin_level = '',
                margin_trade_coeff_vo = binance.subaccount.models.subaccount_get_sub_account_margin_account_v1_resp_margin_trade_coeff_vo.SubaccountGetSubAccountMarginAccountV1Resp_marginTradeCoeffVo(
                    force_liquidation_bar = '', 
                    margin_call_bar = '', 
                    normal_bar = '', ),
                margin_user_asset_vo_list = [
                    binance.subaccount.models.subaccount_get_managed_subaccount_margin_asset_v1_resp_user_assets_inner.SubaccountGetManagedSubaccountMarginAssetV1Resp_userAssets_inner(
                        asset = '', 
                        borrowed = '', 
                        free = '', 
                        interest = '', 
                        locked = '', 
                        net_asset = '', )
                    ],
                total_asset_of_btc = '',
                total_liability_of_btc = '',
                total_net_asset_of_btc = ''
            )
        else:
            return SubaccountGetSubAccountMarginAccountV1Resp(
        )
        """

    def testSubaccountGetSubAccountMarginAccountV1Resp(self):
        """Test SubaccountGetSubAccountMarginAccountV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
