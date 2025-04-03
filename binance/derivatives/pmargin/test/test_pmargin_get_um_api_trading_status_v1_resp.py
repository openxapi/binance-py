# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_um_api_trading_status_v1_resp import PmarginGetUmApiTradingStatusV1Resp

class TestPmarginGetUmApiTradingStatusV1Resp(unittest.TestCase):
    """PmarginGetUmApiTradingStatusV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetUmApiTradingStatusV1Resp:
        """Test PmarginGetUmApiTradingStatusV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetUmApiTradingStatusV1Resp`
        """
        model = PmarginGetUmApiTradingStatusV1Resp()
        if include_optional:
            return PmarginGetUmApiTradingStatusV1Resp(
                indicators = binance.derivatives.pmargin.models.pmargin_get_um_api_trading_status_v1_resp_indicators.PmarginGetUmApiTradingStatusV1Resp_indicators(
                    btcusdt = [
                        binance.derivatives.pmargin.models.pmargin_get_um_api_trading_status_v1_resp_indicators_btcusdt_inner.PmarginGetUmApiTradingStatusV1Resp_indicators_BTCUSDT_inner(
                            indicator = '', 
                            is_locked = True, 
                            planned_recover_time = 56, 
                            trigger_value = 1.337, 
                            value = 1.337, )
                        ], ),
                update_time = 56
            )
        else:
            return PmarginGetUmApiTradingStatusV1Resp(
        )
        """

    def testPmarginGetUmApiTradingStatusV1Resp(self):
        """Test PmarginGetUmApiTradingStatusV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
