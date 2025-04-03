# coding: utf-8

"""
    Binance Sub Account API

    OpenAPI specification for Binance exchange - Subaccount API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.subaccount.models.subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner import SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner

class TestSubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner(unittest.TestCase):
    """SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner:
        """Test SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner`
        """
        model = SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner()
        if include_optional:
            return SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner(
                data = binance.subaccount.models.subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_data.SubaccountGetManagedSubaccountAccountSnapshotV1Resp_snapshotVos_inner_data(
                    balances = [
                        binance.subaccount.models.subaccount_get_managed_subaccount_account_snapshot_v1_resp_snapshot_vos_inner_data_balances_inner.SubaccountGetManagedSubaccountAccountSnapshotV1Resp_snapshotVos_inner_data_balances_inner(
                            asset = '', 
                            free = '', 
                            locked = '', )
                        ], 
                    total_asset_of_btc = '', ),
                type = '',
                update_time = 56
            )
        else:
            return SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner(
        )
        """

    def testSubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner(self):
        """Test SubaccountGetManagedSubaccountAccountSnapshotV1RespSnapshotVosInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
