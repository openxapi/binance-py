# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_simple_earn_flexible_subscribe_v1_resp import CreateSimpleEarnFlexibleSubscribeV1Resp

class TestCreateSimpleEarnFlexibleSubscribeV1Resp(unittest.TestCase):
    """CreateSimpleEarnFlexibleSubscribeV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSimpleEarnFlexibleSubscribeV1Resp:
        """Test CreateSimpleEarnFlexibleSubscribeV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSimpleEarnFlexibleSubscribeV1Resp`
        """
        model = CreateSimpleEarnFlexibleSubscribeV1Resp()
        if include_optional:
            return CreateSimpleEarnFlexibleSubscribeV1Resp(
                purchase_id = 56,
                success = True
            )
        else:
            return CreateSimpleEarnFlexibleSubscribeV1Resp(
        )
        """

    def testCreateSimpleEarnFlexibleSubscribeV1Resp(self):
        """Test CreateSimpleEarnFlexibleSubscribeV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
