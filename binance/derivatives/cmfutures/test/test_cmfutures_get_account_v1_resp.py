# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.models.cmfutures_get_account_v1_resp import CmfuturesGetAccountV1Resp

class TestCmfuturesGetAccountV1Resp(unittest.TestCase):
    """CmfuturesGetAccountV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmfuturesGetAccountV1Resp:
        """Test CmfuturesGetAccountV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmfuturesGetAccountV1Resp`
        """
        model = CmfuturesGetAccountV1Resp()
        if include_optional:
            return CmfuturesGetAccountV1Resp(
                assets = [
                    binance.derivatives.cmfutures.models.cmfutures_get_account_v1_resp_assets_inner.CmfuturesGetAccountV1Resp_assets_inner(
                        asset = '', 
                        available_balance = '', 
                        cross_un_pnl = '', 
                        cross_wallet_balance = '', 
                        initial_margin = '', 
                        maint_margin = '', 
                        margin_balance = '', 
                        max_withdraw_amount = '', 
                        open_order_initial_margin = '', 
                        position_initial_margin = '', 
                        unrealized_profit = '', 
                        update_time = 56, 
                        wallet_balance = '', )
                    ],
                can_deposit = True,
                can_trade = True,
                can_withdraw = True,
                fee_tier = 56,
                positions = [
                    binance.derivatives.cmfutures.models.cmfutures_get_account_v1_resp_positions_inner.CmfuturesGetAccountV1Resp_positions_inner(
                        break_even_price = '', 
                        entry_price = '', 
                        initial_margin = '', 
                        isolated = True, 
                        leverage = '', 
                        maint_margin = '', 
                        max_qty = '', 
                        open_order_initial_margin = '', 
                        position_amt = '', 
                        position_initial_margin = '', 
                        position_side = '', 
                        symbol = '', 
                        unrealized_profit = '', 
                        update_time = 56, )
                    ],
                update_time = 56
            )
        else:
            return CmfuturesGetAccountV1Resp(
        )
        """

    def testCmfuturesGetAccountV1Resp(self):
        """Test CmfuturesGetAccountV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
