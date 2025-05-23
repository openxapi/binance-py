# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_localentity_withdraw_history_v1_resp_item import GetLocalentityWithdrawHistoryV1RespItem

class TestGetLocalentityWithdrawHistoryV1RespItem(unittest.TestCase):
    """GetLocalentityWithdrawHistoryV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLocalentityWithdrawHistoryV1RespItem:
        """Test GetLocalentityWithdrawHistoryV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLocalentityWithdrawHistoryV1RespItem`
        """
        model = GetLocalentityWithdrawHistoryV1RespItem()
        if include_optional:
            return GetLocalentityWithdrawHistoryV1RespItem(
                address = '',
                address_tag = '',
                amount = '',
                apply_time = '',
                coin = '',
                complete_time = '',
                confirm_no = 56,
                id = '',
                info = '',
                network = '',
                questionnaire = '',
                tr_id = 56,
                transaction_fee = '',
                transfer_type = 56,
                travel_rule_status = 56,
                tx_id = '',
                tx_key = '',
                wallet_type = 56,
                withdraw_order_id = '',
                withdrawal_status = 56
            )
        else:
            return GetLocalentityWithdrawHistoryV1RespItem(
        )
        """

    def testGetLocalentityWithdrawHistoryV1RespItem(self):
        """Test GetLocalentityWithdrawHistoryV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
