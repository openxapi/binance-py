# coding: utf-8

"""
    Binance Copy Trading API

    OpenAPI specification for Binance exchange - Copytrading API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.copytrading.models.copytrading_get_copy_trading_futures_lead_symbol_v1_resp import CopytradingGetCopyTradingFuturesLeadSymbolV1Resp

class TestCopytradingGetCopyTradingFuturesLeadSymbolV1Resp(unittest.TestCase):
    """CopytradingGetCopyTradingFuturesLeadSymbolV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopytradingGetCopyTradingFuturesLeadSymbolV1Resp:
        """Test CopytradingGetCopyTradingFuturesLeadSymbolV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopytradingGetCopyTradingFuturesLeadSymbolV1Resp`
        """
        model = CopytradingGetCopyTradingFuturesLeadSymbolV1Resp()
        if include_optional:
            return CopytradingGetCopyTradingFuturesLeadSymbolV1Resp(
                code = '',
                data = [
                    binance.copytrading.models.copytrading_get_copy_trading_futures_lead_symbol_v1_resp_data_inner.CopytradingGetCopyTradingFuturesLeadSymbolV1Resp_data_inner(
                        base_asset = '', 
                        quote_asset = '', 
                        symbol = '', )
                    ],
                message = ''
            )
        else:
            return CopytradingGetCopyTradingFuturesLeadSymbolV1Resp(
        )
        """

    def testCopytradingGetCopyTradingFuturesLeadSymbolV1Resp(self):
        """Test CopytradingGetCopyTradingFuturesLeadSymbolV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
