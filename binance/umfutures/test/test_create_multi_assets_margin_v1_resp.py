# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.umfutures.models.create_multi_assets_margin_v1_resp import CreateMultiAssetsMarginV1Resp

class TestCreateMultiAssetsMarginV1Resp(unittest.TestCase):
    """CreateMultiAssetsMarginV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateMultiAssetsMarginV1Resp:
        """Test CreateMultiAssetsMarginV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateMultiAssetsMarginV1Resp`
        """
        model = CreateMultiAssetsMarginV1Resp()
        if include_optional:
            return CreateMultiAssetsMarginV1Resp(
                code = 56,
                msg = ''
            )
        else:
            return CreateMultiAssetsMarginV1Resp(
        )
        """

    def testCreateMultiAssetsMarginV1Resp(self):
        """Test CreateMultiAssetsMarginV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
