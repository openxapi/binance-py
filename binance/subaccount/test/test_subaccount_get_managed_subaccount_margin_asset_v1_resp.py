# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_managed_subaccount_margin_asset_v1_resp import SubaccountGetManagedSubaccountMarginAssetV1Resp

class TestSubaccountGetManagedSubaccountMarginAssetV1Resp(unittest.TestCase):
    """SubaccountGetManagedSubaccountMarginAssetV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetManagedSubaccountMarginAssetV1Resp:
        """Test SubaccountGetManagedSubaccountMarginAssetV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetManagedSubaccountMarginAssetV1Resp`
        """
        model = SubaccountGetManagedSubaccountMarginAssetV1Resp()
        if include_optional:
            return SubaccountGetManagedSubaccountMarginAssetV1Resp(
                margin_level = '',
                total_asset_of_btc = '',
                total_liability_of_btc = '',
                total_net_asset_of_btc = '',
                user_assets = [
                    binance.subaccount.models.subaccount_get_managed_subaccount_margin_asset_v1_resp_user_assets_inner.SubaccountGetManagedSubaccountMarginAssetV1Resp_userAssets_inner(
                        asset = '', 
                        borrowed = '', 
                        free = '', 
                        interest = '', 
                        locked = '', 
                        net_asset = '', )
                    ]
            )
        else:
            return SubaccountGetManagedSubaccountMarginAssetV1Resp(
        )
        """

    def testSubaccountGetManagedSubaccountMarginAssetV1Resp(self):
        """Test SubaccountGetManagedSubaccountMarginAssetV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
