# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.models.cmfutures_get_account_v1_resp_positions_inner import CmfuturesGetAccountV1RespPositionsInner

class TestCmfuturesGetAccountV1RespPositionsInner(unittest.TestCase):
    """CmfuturesGetAccountV1RespPositionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmfuturesGetAccountV1RespPositionsInner:
        """Test CmfuturesGetAccountV1RespPositionsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmfuturesGetAccountV1RespPositionsInner`
        """
        model = CmfuturesGetAccountV1RespPositionsInner()
        if include_optional:
            return CmfuturesGetAccountV1RespPositionsInner(
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
                update_time = 56
            )
        else:
            return CmfuturesGetAccountV1RespPositionsInner(
        )
        """

    def testCmfuturesGetAccountV1RespPositionsInner(self):
        """Test CmfuturesGetAccountV1RespPositionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
