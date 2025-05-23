# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_asset_transfer_v1_resp import CreateAssetTransferV1Resp

class TestCreateAssetTransferV1Resp(unittest.TestCase):
    """CreateAssetTransferV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAssetTransferV1Resp:
        """Test CreateAssetTransferV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAssetTransferV1Resp`
        """
        model = CreateAssetTransferV1Resp()
        if include_optional:
            return CreateAssetTransferV1Resp(
                tran_id = 56
            )
        else:
            return CreateAssetTransferV1Resp(
        )
        """

    def testCreateAssetTransferV1Resp(self):
        """Test CreateAssetTransferV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
