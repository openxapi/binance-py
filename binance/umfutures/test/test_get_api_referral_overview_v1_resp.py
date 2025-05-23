# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.umfutures.models.get_api_referral_overview_v1_resp import GetApiReferralOverviewV1Resp

class TestGetApiReferralOverviewV1Resp(unittest.TestCase):
    """GetApiReferralOverviewV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiReferralOverviewV1Resp:
        """Test GetApiReferralOverviewV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiReferralOverviewV1Resp`
        """
        model = GetApiReferralOverviewV1Resp()
        if include_optional:
            return GetApiReferralOverviewV1Resp(
                broker_id = '',
                new_trader_rebate_commission = '',
                old_trader_rebate_commission = '',
                time = 56,
                total_rebate_vol = '',
                total_trade_user = 56,
                total_trade_vol = '',
                unit = ''
            )
        else:
            return GetApiReferralOverviewV1Resp(
        )
        """

    def testGetApiReferralOverviewV1Resp(self):
        """Test GetApiReferralOverviewV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
