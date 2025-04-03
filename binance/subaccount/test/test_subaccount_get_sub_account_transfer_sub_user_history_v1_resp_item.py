# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_sub_account_transfer_sub_user_history_v1_resp_item import SubaccountGetSubAccountTransferSubUserHistoryV1RespItem

class TestSubaccountGetSubAccountTransferSubUserHistoryV1RespItem(unittest.TestCase):
    """SubaccountGetSubAccountTransferSubUserHistoryV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetSubAccountTransferSubUserHistoryV1RespItem:
        """Test SubaccountGetSubAccountTransferSubUserHistoryV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetSubAccountTransferSubUserHistoryV1RespItem`
        """
        model = SubaccountGetSubAccountTransferSubUserHistoryV1RespItem()
        if include_optional:
            return SubaccountGetSubAccountTransferSubUserHistoryV1RespItem(
                asset = '',
                counter_party = '',
                email = '',
                from_account_type = '',
                qty = '',
                status = '',
                time = 56,
                to_account_type = '',
                tran_id = 56,
                type = 56
            )
        else:
            return SubaccountGetSubAccountTransferSubUserHistoryV1RespItem(
        )
        """

    def testSubaccountGetSubAccountTransferSubUserHistoryV1RespItem(self):
        """Test SubaccountGetSubAccountTransferSubUserHistoryV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
