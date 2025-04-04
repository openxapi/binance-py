# coding: utf-8

"""
    Binance Wallet API

    OpenAPI specification for Binance exchange - Wallet API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.wallet.models.wallet_update_localentity_broker_deposit_provide_info_v1_resp import WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp

class TestWalletUpdateLocalentityBrokerDepositProvideInfoV1Resp(unittest.TestCase):
    """WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp:
        """Test WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp`
        """
        model = WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp()
        if include_optional:
            return WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp(
                accepted = True,
                info = '',
                tr_id = 56
            )
        else:
            return WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp(
        )
        """

    def testWalletUpdateLocalentityBrokerDepositProvideInfoV1Resp(self):
        """Test WalletUpdateLocalentityBrokerDepositProvideInfoV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
