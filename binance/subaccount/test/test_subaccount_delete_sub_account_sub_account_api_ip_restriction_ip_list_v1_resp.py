# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_delete_sub_account_sub_account_api_ip_restriction_ip_list_v1_resp import SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp

class TestSubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp(unittest.TestCase):
    """SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp:
        """Test SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp`
        """
        model = SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp()
        if include_optional:
            return SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp(
                api_key = '',
                ip_list = [
                    ''
                    ],
                ip_restrict = '',
                update_time = 56
            )
        else:
            return SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp(
        )
        """

    def testSubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp(self):
        """Test SubaccountDeleteSubAccountSubAccountApiIpRestrictionIpListV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
