# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_create_sub_account_virtual_sub_account_v1_resp import SubaccountCreateSubAccountVirtualSubAccountV1Resp

class TestSubaccountCreateSubAccountVirtualSubAccountV1Resp(unittest.TestCase):
    """SubaccountCreateSubAccountVirtualSubAccountV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountCreateSubAccountVirtualSubAccountV1Resp:
        """Test SubaccountCreateSubAccountVirtualSubAccountV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountCreateSubAccountVirtualSubAccountV1Resp`
        """
        model = SubaccountCreateSubAccountVirtualSubAccountV1Resp()
        if include_optional:
            return SubaccountCreateSubAccountVirtualSubAccountV1Resp(
                email = ''
            )
        else:
            return SubaccountCreateSubAccountVirtualSubAccountV1Resp(
        )
        """

    def testSubaccountCreateSubAccountVirtualSubAccountV1Resp(self):
        """Test SubaccountCreateSubAccountVirtualSubAccountV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
