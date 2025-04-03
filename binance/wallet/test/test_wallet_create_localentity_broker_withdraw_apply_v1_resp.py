# coding: utf-8

"""
    Binance Wallet API

    OpenAPI specification for Binance exchange - Wallet API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.wallet.models.wallet_create_localentity_broker_withdraw_apply_v1_resp import WalletCreateLocalentityBrokerWithdrawApplyV1Resp

class TestWalletCreateLocalentityBrokerWithdrawApplyV1Resp(unittest.TestCase):
    """WalletCreateLocalentityBrokerWithdrawApplyV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletCreateLocalentityBrokerWithdrawApplyV1Resp:
        """Test WalletCreateLocalentityBrokerWithdrawApplyV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletCreateLocalentityBrokerWithdrawApplyV1Resp`
        """
        model = WalletCreateLocalentityBrokerWithdrawApplyV1Resp()
        if include_optional:
            return WalletCreateLocalentityBrokerWithdrawApplyV1Resp(
                accpted = True,
                info = '',
                tr_id = 56
            )
        else:
            return WalletCreateLocalentityBrokerWithdrawApplyV1Resp(
        )
        """

    def testWalletCreateLocalentityBrokerWithdrawApplyV1Resp(self):
        """Test WalletCreateLocalentityBrokerWithdrawApplyV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
