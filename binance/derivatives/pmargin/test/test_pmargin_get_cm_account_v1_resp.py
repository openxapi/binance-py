# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_cm_account_v1_resp import PmarginGetCmAccountV1Resp

class TestPmarginGetCmAccountV1Resp(unittest.TestCase):
    """PmarginGetCmAccountV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetCmAccountV1Resp:
        """Test PmarginGetCmAccountV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetCmAccountV1Resp`
        """
        model = PmarginGetCmAccountV1Resp()
        if include_optional:
            return PmarginGetCmAccountV1Resp(
                assets = [
                    binance.derivatives.pmargin.models.pmargin_get_cm_account_v1_resp_assets_inner.PmarginGetCmAccountV1Resp_assets_inner(
                        asset = '', 
                        cross_un_pnl = '', 
                        cross_wallet_balance = '', 
                        initial_margin = '', 
                        maint_margin = '', 
                        open_order_initial_margin = '', 
                        position_initial_margin = '', 
                        update_time = 56, )
                    ],
                positions = [
                    binance.derivatives.pmargin.models.pmargin_get_cm_account_v1_resp_positions_inner.PmarginGetCmAccountV1Resp_positions_inner(
                        entry_price = '', 
                        initial_margin = '', 
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
                    ]
            )
        else:
            return PmarginGetCmAccountV1Resp(
        )
        """

    def testPmarginGetCmAccountV1Resp(self):
        """Test PmarginGetCmAccountV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
