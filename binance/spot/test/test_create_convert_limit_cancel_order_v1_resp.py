# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_convert_limit_cancel_order_v1_resp import CreateConvertLimitCancelOrderV1Resp

class TestCreateConvertLimitCancelOrderV1Resp(unittest.TestCase):
    """CreateConvertLimitCancelOrderV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateConvertLimitCancelOrderV1Resp:
        """Test CreateConvertLimitCancelOrderV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateConvertLimitCancelOrderV1Resp`
        """
        model = CreateConvertLimitCancelOrderV1Resp()
        if include_optional:
            return CreateConvertLimitCancelOrderV1Resp(
                order_id = 56,
                status = ''
            )
        else:
            return CreateConvertLimitCancelOrderV1Resp(
        )
        """

    def testCreateConvertLimitCancelOrderV1Resp(self):
        """Test CreateConvertLimitCancelOrderV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
