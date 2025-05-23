# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_asset_ledger_transfer_cloud_mining_query_by_page_v1_resp_rows_inner import GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner

class TestGetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner(unittest.TestCase):
    """GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner:
        """Test GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner`
        """
        model = GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner()
        if include_optional:
            return GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner(
                amount = '',
                asset = '',
                create_time = 56,
                status = '',
                tran_id = 56,
                type = 56
            )
        else:
            return GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner(
        )
        """

    def testGetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner(self):
        """Test GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
