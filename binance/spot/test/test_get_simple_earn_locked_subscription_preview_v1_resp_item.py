# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_simple_earn_locked_subscription_preview_v1_resp_item import GetSimpleEarnLockedSubscriptionPreviewV1RespItem

class TestGetSimpleEarnLockedSubscriptionPreviewV1RespItem(unittest.TestCase):
    """GetSimpleEarnLockedSubscriptionPreviewV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSimpleEarnLockedSubscriptionPreviewV1RespItem:
        """Test GetSimpleEarnLockedSubscriptionPreviewV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSimpleEarnLockedSubscriptionPreviewV1RespItem`
        """
        model = GetSimpleEarnLockedSubscriptionPreviewV1RespItem()
        if include_optional:
            return GetSimpleEarnLockedSubscriptionPreviewV1RespItem(
                boost_reward_asset = '',
                deliver_date = '',
                est_daily_reward_amt = '',
                est_total_extra_reward_amt = '',
                extra_reward_asset = '',
                next_pay = '',
                next_pay_date = '',
                next_subscription_date = '',
                reward_asset = '',
                rewards_end_date = '',
                total_reward_amt = '',
                value_date = ''
            )
        else:
            return GetSimpleEarnLockedSubscriptionPreviewV1RespItem(
        )
        """

    def testGetSimpleEarnLockedSubscriptionPreviewV1RespItem(self):
        """Test GetSimpleEarnLockedSubscriptionPreviewV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
