# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_sub_account_sub_account_api_ip_restriction_v1_resp import GetSubAccountSubAccountApiIpRestrictionV1Resp

class TestGetSubAccountSubAccountApiIpRestrictionV1Resp(unittest.TestCase):
    """GetSubAccountSubAccountApiIpRestrictionV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSubAccountSubAccountApiIpRestrictionV1Resp:
        """Test GetSubAccountSubAccountApiIpRestrictionV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSubAccountSubAccountApiIpRestrictionV1Resp`
        """
        model = GetSubAccountSubAccountApiIpRestrictionV1Resp()
        if include_optional:
            return GetSubAccountSubAccountApiIpRestrictionV1Resp(
                api_key = '',
                ip_list = [
                    ''
                    ],
                ip_restrict = '',
                update_time = 56
            )
        else:
            return GetSubAccountSubAccountApiIpRestrictionV1Resp(
        )
        """

    def testGetSubAccountSubAccountApiIpRestrictionV1Resp(self):
        """Test GetSubAccountSubAccountApiIpRestrictionV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
