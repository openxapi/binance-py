# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_um_account_v2_resp_positions_inner import PmarginGetUmAccountV2RespPositionsInner

class TestPmarginGetUmAccountV2RespPositionsInner(unittest.TestCase):
    """PmarginGetUmAccountV2RespPositionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetUmAccountV2RespPositionsInner:
        """Test PmarginGetUmAccountV2RespPositionsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetUmAccountV2RespPositionsInner`
        """
        model = PmarginGetUmAccountV2RespPositionsInner()
        if include_optional:
            return PmarginGetUmAccountV2RespPositionsInner(
                initial_margin = '',
                maint_margin = '',
                notional = '',
                position_amt = '',
                position_side = '',
                symbol = '',
                unrealized_profit = '',
                update_time = 56
            )
        else:
            return PmarginGetUmAccountV2RespPositionsInner(
        )
        """

    def testPmarginGetUmAccountV2RespPositionsInner(self):
        """Test PmarginGetUmAccountV2RespPositionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
