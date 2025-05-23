# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_user_data_stream_isolated_v1_resp import CreateUserDataStreamIsolatedV1Resp

class TestCreateUserDataStreamIsolatedV1Resp(unittest.TestCase):
    """CreateUserDataStreamIsolatedV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUserDataStreamIsolatedV1Resp:
        """Test CreateUserDataStreamIsolatedV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUserDataStreamIsolatedV1Resp`
        """
        model = CreateUserDataStreamIsolatedV1Resp()
        if include_optional:
            return CreateUserDataStreamIsolatedV1Resp(
                listen_key = ''
            )
        else:
            return CreateUserDataStreamIsolatedV1Resp(
        )
        """

    def testCreateUserDataStreamIsolatedV1Resp(self):
        """Test CreateUserDataStreamIsolatedV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
