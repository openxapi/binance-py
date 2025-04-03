# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp_symbols_inner import UmfuturesGetExchangeInfoV1RespSymbolsInner

class TestUmfuturesGetExchangeInfoV1RespSymbolsInner(unittest.TestCase):
    """UmfuturesGetExchangeInfoV1RespSymbolsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetExchangeInfoV1RespSymbolsInner:
        """Test UmfuturesGetExchangeInfoV1RespSymbolsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetExchangeInfoV1RespSymbolsInner`
        """
        model = UmfuturesGetExchangeInfoV1RespSymbolsInner()
        if include_optional:
            return UmfuturesGetExchangeInfoV1RespSymbolsInner(
                order_type = [
                    ''
                    ],
                base_asset = '',
                base_asset_precision = 56,
                contract_type = '',
                delivery_date = 56,
                filters = [
                    binance.derivatives.umfutures.models.umfutures_get_exchange_info_v1_resp_symbols_inner_filters_inner.UmfuturesGetExchangeInfoV1Resp_symbols_inner_filters_inner(
                        filter_type = '', 
                        max_price = '', 
                        min_price = '', 
                        tick_size = '', )
                    ],
                liquidation_fee = '',
                maint_margin_percent = '',
                margin_asset = '',
                market_take_bound = '',
                onboard_date = 56,
                pair = '',
                price_precision = 56,
                quantity_precision = 56,
                quote_asset = '',
                quote_precision = 56,
                required_margin_percent = '',
                settle_plan = 56,
                status = '',
                symbol = '',
                time_in_force = [
                    ''
                    ],
                trigger_protect = '',
                underlying_sub_type = [
                    ''
                    ],
                underlying_type = ''
            )
        else:
            return UmfuturesGetExchangeInfoV1RespSymbolsInner(
        )
        """

    def testUmfuturesGetExchangeInfoV1RespSymbolsInner(self):
        """Test UmfuturesGetExchangeInfoV1RespSymbolsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
