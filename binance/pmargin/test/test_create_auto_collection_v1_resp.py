# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.pmargin.models.create_auto_collection_v1_resp import CreateAutoCollectionV1Resp

class TestCreateAutoCollectionV1Resp(unittest.TestCase):
    """CreateAutoCollectionV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAutoCollectionV1Resp:
        """Test CreateAutoCollectionV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAutoCollectionV1Resp`
        """
        model = CreateAutoCollectionV1Resp()
        if include_optional:
            return CreateAutoCollectionV1Resp(
                msg = ''
            )
        else:
            return CreateAutoCollectionV1Resp(
        )
        """

    def testCreateAutoCollectionV1Resp(self):
        """Test CreateAutoCollectionV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
