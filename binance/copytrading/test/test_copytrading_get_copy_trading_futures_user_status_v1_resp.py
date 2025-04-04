# coding: utf-8

"""
    Binance Copy Trading API

    OpenAPI specification for Binance exchange - Copytrading API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.copytrading.models.copytrading_get_copy_trading_futures_user_status_v1_resp import CopytradingGetCopyTradingFuturesUserStatusV1Resp

class TestCopytradingGetCopyTradingFuturesUserStatusV1Resp(unittest.TestCase):
    """CopytradingGetCopyTradingFuturesUserStatusV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CopytradingGetCopyTradingFuturesUserStatusV1Resp:
        """Test CopytradingGetCopyTradingFuturesUserStatusV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CopytradingGetCopyTradingFuturesUserStatusV1Resp`
        """
        model = CopytradingGetCopyTradingFuturesUserStatusV1Resp()
        if include_optional:
            return CopytradingGetCopyTradingFuturesUserStatusV1Resp(
                code = '',
                data = binance.copytrading.models.copytrading_get_copy_trading_futures_user_status_v1_resp_data.CopytradingGetCopyTradingFuturesUserStatusV1Resp_data(
                    is_lead_trader = True, 
                    time = 56, ),
                message = '',
                success = True
            )
        else:
            return CopytradingGetCopyTradingFuturesUserStatusV1Resp(
        )
        """

    def testCopytradingGetCopyTradingFuturesUserStatusV1Resp(self):
        """Test CopytradingGetCopyTradingFuturesUserStatusV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
