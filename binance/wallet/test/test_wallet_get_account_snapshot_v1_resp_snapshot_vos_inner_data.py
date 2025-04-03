# coding: utf-8

"""
    Binance Wallet API

    OpenAPI specification for Binance exchange - Wallet API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.wallet.models.wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_data import WalletGetAccountSnapshotV1RespSnapshotVosInnerData

class TestWalletGetAccountSnapshotV1RespSnapshotVosInnerData(unittest.TestCase):
    """WalletGetAccountSnapshotV1RespSnapshotVosInnerData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletGetAccountSnapshotV1RespSnapshotVosInnerData:
        """Test WalletGetAccountSnapshotV1RespSnapshotVosInnerData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletGetAccountSnapshotV1RespSnapshotVosInnerData`
        """
        model = WalletGetAccountSnapshotV1RespSnapshotVosInnerData()
        if include_optional:
            return WalletGetAccountSnapshotV1RespSnapshotVosInnerData(
                balances = [
                    binance.wallet.models.wallet_get_account_snapshot_v1_resp_snapshot_vos_inner_data_balances_inner.WalletGetAccountSnapshotV1Resp_snapshotVos_inner_data_balances_inner(
                        asset = '', 
                        free = '', 
                        locked = '', )
                    ],
                total_asset_of_btc = ''
            )
        else:
            return WalletGetAccountSnapshotV1RespSnapshotVosInnerData(
        )
        """

    def testWalletGetAccountSnapshotV1RespSnapshotVosInnerData(self):
        """Test WalletGetAccountSnapshotV1RespSnapshotVosInnerData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
