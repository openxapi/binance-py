# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.pmargin.models.get_um_account_v2_resp_positions_inner import GetUmAccountV2RespPositionsInner

class TestGetUmAccountV2RespPositionsInner(unittest.TestCase):
    """GetUmAccountV2RespPositionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUmAccountV2RespPositionsInner:
        """Test GetUmAccountV2RespPositionsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUmAccountV2RespPositionsInner`
        """
        model = GetUmAccountV2RespPositionsInner()
        if include_optional:
            return GetUmAccountV2RespPositionsInner(
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
            return GetUmAccountV2RespPositionsInner(
        )
        """

    def testGetUmAccountV2RespPositionsInner(self):
        """Test GetUmAccountV2RespPositionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
