# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.umfutures.models.get_api_referral_if_new_user_v1_resp import GetApiReferralIfNewUserV1Resp

class TestGetApiReferralIfNewUserV1Resp(unittest.TestCase):
    """GetApiReferralIfNewUserV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiReferralIfNewUserV1Resp:
        """Test GetApiReferralIfNewUserV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiReferralIfNewUserV1Resp`
        """
        model = GetApiReferralIfNewUserV1Resp()
        if include_optional:
            return GetApiReferralIfNewUserV1Resp(
                broker_id = '',
                if_new_user = True,
                rebate_working = True
            )
        else:
            return GetApiReferralIfNewUserV1Resp(
        )
        """

    def testGetApiReferralIfNewUserV1Resp(self):
        """Test GetApiReferralIfNewUserV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
