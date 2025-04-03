# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_sub_account_universal_transfer_v1_resp import SubaccountGetSubAccountUniversalTransferV1Resp

class TestSubaccountGetSubAccountUniversalTransferV1Resp(unittest.TestCase):
    """SubaccountGetSubAccountUniversalTransferV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetSubAccountUniversalTransferV1Resp:
        """Test SubaccountGetSubAccountUniversalTransferV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetSubAccountUniversalTransferV1Resp`
        """
        model = SubaccountGetSubAccountUniversalTransferV1Resp()
        if include_optional:
            return SubaccountGetSubAccountUniversalTransferV1Resp(
                result = [
                    binance.subaccount.models.subaccount_get_sub_account_universal_transfer_v1_resp_result_inner.SubaccountGetSubAccountUniversalTransferV1Resp_result_inner(
                        amount = '', 
                        asset = '', 
                        client_tran_id = '', 
                        create_time_stamp = 56, 
                        from_account_type = '', 
                        from_email = '', 
                        status = '', 
                        to_account_type = '', 
                        to_email = '', 
                        tran_id = 56, )
                    ],
                total_count = 56
            )
        else:
            return SubaccountGetSubAccountUniversalTransferV1Resp(
        )
        """

    def testSubaccountGetSubAccountUniversalTransferV1Resp(self):
        """Test SubaccountGetSubAccountUniversalTransferV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
