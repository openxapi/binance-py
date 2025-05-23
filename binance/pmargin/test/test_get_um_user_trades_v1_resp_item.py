# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.pmargin.models.get_um_user_trades_v1_resp_item import GetUmUserTradesV1RespItem

class TestGetUmUserTradesV1RespItem(unittest.TestCase):
    """GetUmUserTradesV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUmUserTradesV1RespItem:
        """Test GetUmUserTradesV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUmUserTradesV1RespItem`
        """
        model = GetUmUserTradesV1RespItem()
        if include_optional:
            return GetUmUserTradesV1RespItem(
                buyer = True,
                commission = '',
                commission_asset = '',
                id = 56,
                maker = True,
                order_id = 56,
                position_side = '',
                price = '',
                qty = '',
                quote_qty = '',
                realized_pnl = '',
                side = '',
                symbol = '',
                time = 56
            )
        else:
            return GetUmUserTradesV1RespItem(
        )
        """

    def testGetUmUserTradesV1RespItem(self):
        """Test GetUmUserTradesV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
