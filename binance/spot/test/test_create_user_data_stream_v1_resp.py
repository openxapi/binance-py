# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_user_data_stream_v1_resp import CreateUserDataStreamV1Resp

class TestCreateUserDataStreamV1Resp(unittest.TestCase):
    """CreateUserDataStreamV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUserDataStreamV1Resp:
        """Test CreateUserDataStreamV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUserDataStreamV1Resp`
        """
        model = CreateUserDataStreamV1Resp()
        if include_optional:
            return CreateUserDataStreamV1Resp(
                listen_key = ''
            )
        else:
            return CreateUserDataStreamV1Resp(
        )
        """

    def testCreateUserDataStreamV1Resp(self):
        """Test CreateUserDataStreamV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
