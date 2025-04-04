# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_create_sub_account_transfer_sub_to_master_v1_resp import SubaccountCreateSubAccountTransferSubToMasterV1Resp

class TestSubaccountCreateSubAccountTransferSubToMasterV1Resp(unittest.TestCase):
    """SubaccountCreateSubAccountTransferSubToMasterV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountCreateSubAccountTransferSubToMasterV1Resp:
        """Test SubaccountCreateSubAccountTransferSubToMasterV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountCreateSubAccountTransferSubToMasterV1Resp`
        """
        model = SubaccountCreateSubAccountTransferSubToMasterV1Resp()
        if include_optional:
            return SubaccountCreateSubAccountTransferSubToMasterV1Resp(
                txn_id = ''
            )
        else:
            return SubaccountCreateSubAccountTransferSubToMasterV1Resp(
        )
        """

    def testSubaccountCreateSubAccountTransferSubToMasterV1Resp(self):
        """Test SubaccountCreateSubAccountTransferSubToMasterV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
