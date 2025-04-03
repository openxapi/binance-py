# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_balance_v3_resp_item import UmfuturesGetBalanceV3RespItem

class TestUmfuturesGetBalanceV3RespItem(unittest.TestCase):
    """UmfuturesGetBalanceV3RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetBalanceV3RespItem:
        """Test UmfuturesGetBalanceV3RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetBalanceV3RespItem`
        """
        model = UmfuturesGetBalanceV3RespItem()
        if include_optional:
            return UmfuturesGetBalanceV3RespItem(
                account_alias = '',
                asset = '',
                available_balance = '',
                balance = '',
                cross_un_pnl = '',
                cross_wallet_balance = '',
                margin_available = True,
                max_withdraw_amount = '',
                update_time = 56
            )
        else:
            return UmfuturesGetBalanceV3RespItem(
        )
        """

    def testUmfuturesGetBalanceV3RespItem(self):
        """Test UmfuturesGetBalanceV3RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
