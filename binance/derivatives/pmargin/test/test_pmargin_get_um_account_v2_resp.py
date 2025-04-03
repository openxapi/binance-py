# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_um_account_v2_resp import PmarginGetUmAccountV2Resp

class TestPmarginGetUmAccountV2Resp(unittest.TestCase):
    """PmarginGetUmAccountV2Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetUmAccountV2Resp:
        """Test PmarginGetUmAccountV2Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetUmAccountV2Resp`
        """
        model = PmarginGetUmAccountV2Resp()
        if include_optional:
            return PmarginGetUmAccountV2Resp(
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
                    binance.derivatives.pmargin.models.pmargin_get_um_account_v2_resp_positions_inner.PmarginGetUmAccountV2Resp_positions_inner(
                        initial_margin = '', 
                        maint_margin = '', 
                        notional = '', 
                        position_amt = '', 
                        position_side = '', 
                        symbol = '', 
                        unrealized_profit = '', 
                        update_time = 56, )
                    ]
            )
        else:
            return PmarginGetUmAccountV2Resp(
        )
        """

    def testPmarginGetUmAccountV2Resp(self):
        """Test PmarginGetUmAccountV2Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
