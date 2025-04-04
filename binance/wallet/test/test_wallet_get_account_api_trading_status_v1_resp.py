# coding: utf-8

"""
    Binance Wallet API

    OpenAPI specification for Binance exchange - Wallet API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.wallet.models.wallet_get_account_api_trading_status_v1_resp import WalletGetAccountApiTradingStatusV1Resp

class TestWalletGetAccountApiTradingStatusV1Resp(unittest.TestCase):
    """WalletGetAccountApiTradingStatusV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WalletGetAccountApiTradingStatusV1Resp:
        """Test WalletGetAccountApiTradingStatusV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WalletGetAccountApiTradingStatusV1Resp`
        """
        model = WalletGetAccountApiTradingStatusV1Resp()
        if include_optional:
            return WalletGetAccountApiTradingStatusV1Resp(
                data = binance.wallet.models.wallet_get_account_api_trading_status_v1_resp_data.WalletGetAccountApiTradingStatusV1Resp_data(
                    is_locked = True, 
                    planned_recover_time = 56, 
                    trigger_condition = binance.wallet.models.wallet_get_account_api_trading_status_v1_resp_data_trigger_condition.WalletGetAccountApiTradingStatusV1Resp_data_triggerCondition(
                        gcr = 56, 
                        ifer = 56, 
                        ufr = 56, ), 
                    update_time = 56, )
            )
        else:
            return WalletGetAccountApiTradingStatusV1Resp(
        )
        """

    def testWalletGetAccountApiTradingStatusV1Resp(self):
        """Test WalletGetAccountApiTradingStatusV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
