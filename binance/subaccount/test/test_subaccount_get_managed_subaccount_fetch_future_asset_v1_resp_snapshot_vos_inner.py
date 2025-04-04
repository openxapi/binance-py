# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner import SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner

class TestSubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner(unittest.TestCase):
    """SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner:
        """Test SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner`
        """
        model = SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner()
        if include_optional:
            return SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner(
                data = binance.subaccount.models.subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data.SubaccountGetManagedSubaccountFetchFutureAssetV1Resp_snapshotVos_inner_data(
                    assets = [
                        binance.subaccount.models.subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_assets_inner.SubaccountGetManagedSubaccountFetchFutureAssetV1Resp_snapshotVos_inner_data_assets_inner(
                            asset = '', 
                            margin_balance = 56, 
                            wallet_balance = 56, )
                        ], 
                    position = [
                        binance.subaccount.models.subaccount_get_managed_subaccount_fetch_future_asset_v1_resp_snapshot_vos_inner_data_position_inner.SubaccountGetManagedSubaccountFetchFutureAssetV1Resp_snapshotVos_inner_data_position_inner(
                            entry_price = 56, 
                            mark_price = 56, 
                            position_amt = 1.337, 
                            symbol = '', )
                        ], ),
                type = '',
                update_time = 56
            )
        else:
            return SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner(
        )
        """

    def testSubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner(self):
        """Test SubaccountGetManagedSubaccountFetchFutureAssetV1RespSnapshotVosInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
