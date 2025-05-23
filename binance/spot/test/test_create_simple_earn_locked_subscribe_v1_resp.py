# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_simple_earn_locked_subscribe_v1_resp import CreateSimpleEarnLockedSubscribeV1Resp

class TestCreateSimpleEarnLockedSubscribeV1Resp(unittest.TestCase):
    """CreateSimpleEarnLockedSubscribeV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSimpleEarnLockedSubscribeV1Resp:
        """Test CreateSimpleEarnLockedSubscribeV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSimpleEarnLockedSubscribeV1Resp`
        """
        model = CreateSimpleEarnLockedSubscribeV1Resp()
        if include_optional:
            return CreateSimpleEarnLockedSubscribeV1Resp(
                position_id = '',
                purchase_id = 56,
                success = True
            )
        else:
            return CreateSimpleEarnLockedSubscribeV1Resp(
        )
        """

    def testCreateSimpleEarnLockedSubscribeV1Resp(self):
        """Test CreateSimpleEarnLockedSubscribeV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
