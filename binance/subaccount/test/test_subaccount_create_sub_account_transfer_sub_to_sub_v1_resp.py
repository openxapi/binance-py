# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_create_sub_account_transfer_sub_to_sub_v1_resp import SubaccountCreateSubAccountTransferSubToSubV1Resp

class TestSubaccountCreateSubAccountTransferSubToSubV1Resp(unittest.TestCase):
    """SubaccountCreateSubAccountTransferSubToSubV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountCreateSubAccountTransferSubToSubV1Resp:
        """Test SubaccountCreateSubAccountTransferSubToSubV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountCreateSubAccountTransferSubToSubV1Resp`
        """
        model = SubaccountCreateSubAccountTransferSubToSubV1Resp()
        if include_optional:
            return SubaccountCreateSubAccountTransferSubToSubV1Resp(
                txn_id = ''
            )
        else:
            return SubaccountCreateSubAccountTransferSubToSubV1Resp(
        )
        """

    def testSubaccountCreateSubAccountTransferSubToSubV1Resp(self):
        """Test SubaccountCreateSubAccountTransferSubToSubV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
