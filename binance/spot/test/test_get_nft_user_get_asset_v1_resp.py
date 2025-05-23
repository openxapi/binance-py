# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_nft_user_get_asset_v1_resp import GetNftUserGetAssetV1Resp

class TestGetNftUserGetAssetV1Resp(unittest.TestCase):
    """GetNftUserGetAssetV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetNftUserGetAssetV1Resp:
        """Test GetNftUserGetAssetV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetNftUserGetAssetV1Resp`
        """
        model = GetNftUserGetAssetV1Resp()
        if include_optional:
            return GetNftUserGetAssetV1Resp(
                list = [
                    binance.spot.models.get_nft_history_transactions_v1_resp_list_inner_tokens_inner.GetNftHistoryTransactionsV1Resp_list_inner_tokens_inner(
                        contract_address = '', 
                        network = '', 
                        token_id = '', )
                    ],
                total = 56
            )
        else:
            return GetNftUserGetAssetV1Resp(
        )
        """

    def testGetNftUserGetAssetV1Resp(self):
        """Test GetNftUserGetAssetV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
