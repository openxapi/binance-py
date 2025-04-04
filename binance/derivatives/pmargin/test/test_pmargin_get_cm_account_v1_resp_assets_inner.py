# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_cm_account_v1_resp_assets_inner import PmarginGetCmAccountV1RespAssetsInner

class TestPmarginGetCmAccountV1RespAssetsInner(unittest.TestCase):
    """PmarginGetCmAccountV1RespAssetsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetCmAccountV1RespAssetsInner:
        """Test PmarginGetCmAccountV1RespAssetsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetCmAccountV1RespAssetsInner`
        """
        model = PmarginGetCmAccountV1RespAssetsInner()
        if include_optional:
            return PmarginGetCmAccountV1RespAssetsInner(
                asset = '',
                cross_un_pnl = '',
                cross_wallet_balance = '',
                initial_margin = '',
                maint_margin = '',
                open_order_initial_margin = '',
                position_initial_margin = '',
                update_time = 56
            )
        else:
            return PmarginGetCmAccountV1RespAssetsInner(
        )
        """

    def testPmarginGetCmAccountV1RespAssetsInner(self):
        """Test PmarginGetCmAccountV1RespAssetsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
