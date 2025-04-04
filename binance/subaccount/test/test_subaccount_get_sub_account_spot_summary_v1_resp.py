# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_sub_account_spot_summary_v1_resp import SubaccountGetSubAccountSpotSummaryV1Resp

class TestSubaccountGetSubAccountSpotSummaryV1Resp(unittest.TestCase):
    """SubaccountGetSubAccountSpotSummaryV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetSubAccountSpotSummaryV1Resp:
        """Test SubaccountGetSubAccountSpotSummaryV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetSubAccountSpotSummaryV1Resp`
        """
        model = SubaccountGetSubAccountSpotSummaryV1Resp()
        if include_optional:
            return SubaccountGetSubAccountSpotSummaryV1Resp(
                master_account_total_asset = '',
                spot_sub_user_asset_btc_vo_list = [
                    binance.subaccount.models.subaccount_get_sub_account_spot_summary_v1_resp_spot_sub_user_asset_btc_vo_list_inner.SubaccountGetSubAccountSpotSummaryV1Resp_spotSubUserAssetBtcVoList_inner(
                        email = '', 
                        total_asset = '', )
                    ],
                total_count = 56
            )
        else:
            return SubaccountGetSubAccountSpotSummaryV1Resp(
        )
        """

    def testSubaccountGetSubAccountSpotSummaryV1Resp(self):
        """Test SubaccountGetSubAccountSpotSummaryV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
