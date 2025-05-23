# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.update_localentity_deposit_provide_info_v1_resp import UpdateLocalentityDepositProvideInfoV1Resp

class TestUpdateLocalentityDepositProvideInfoV1Resp(unittest.TestCase):
    """UpdateLocalentityDepositProvideInfoV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateLocalentityDepositProvideInfoV1Resp:
        """Test UpdateLocalentityDepositProvideInfoV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateLocalentityDepositProvideInfoV1Resp`
        """
        model = UpdateLocalentityDepositProvideInfoV1Resp()
        if include_optional:
            return UpdateLocalentityDepositProvideInfoV1Resp(
                accepted = True,
                info = '',
                tr_id = 56
            )
        else:
            return UpdateLocalentityDepositProvideInfoV1Resp(
        )
        """

    def testUpdateLocalentityDepositProvideInfoV1Resp(self):
        """Test UpdateLocalentityDepositProvideInfoV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
