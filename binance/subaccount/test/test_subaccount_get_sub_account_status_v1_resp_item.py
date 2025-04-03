# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_sub_account_status_v1_resp_item import SubaccountGetSubAccountStatusV1RespItem

class TestSubaccountGetSubAccountStatusV1RespItem(unittest.TestCase):
    """SubaccountGetSubAccountStatusV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetSubAccountStatusV1RespItem:
        """Test SubaccountGetSubAccountStatusV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetSubAccountStatusV1RespItem`
        """
        model = SubaccountGetSubAccountStatusV1RespItem()
        if include_optional:
            return SubaccountGetSubAccountStatusV1RespItem(
                email = '',
                insert_time = 56,
                is_future_enabled = True,
                is_margin_enabled = True,
                is_sub_user_enabled = True,
                is_user_active = True,
                mobile = 56
            )
        else:
            return SubaccountGetSubAccountStatusV1RespItem(
        )
        """

    def testSubaccountGetSubAccountStatusV1RespItem(self):
        """Test SubaccountGetSubAccountStatusV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
