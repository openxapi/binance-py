# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_get_margin_exchange_small_liability_history_v1_resp import MarginGetMarginExchangeSmallLiabilityHistoryV1Resp

class TestMarginGetMarginExchangeSmallLiabilityHistoryV1Resp(unittest.TestCase):
    """MarginGetMarginExchangeSmallLiabilityHistoryV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginGetMarginExchangeSmallLiabilityHistoryV1Resp:
        """Test MarginGetMarginExchangeSmallLiabilityHistoryV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginGetMarginExchangeSmallLiabilityHistoryV1Resp`
        """
        model = MarginGetMarginExchangeSmallLiabilityHistoryV1Resp()
        if include_optional:
            return MarginGetMarginExchangeSmallLiabilityHistoryV1Resp(
                rows = [
                    binance.margin.models.margin_get_margin_exchange_small_liability_history_v1_resp_rows_inner.MarginGetMarginExchangeSmallLiabilityHistoryV1Resp_rows_inner(
                        amount = '', 
                        asset = '', 
                        biz_type = '', 
                        target_amount = '', 
                        target_asset = '', 
                        timestamp = 56, )
                    ],
                total = 56
            )
        else:
            return MarginGetMarginExchangeSmallLiabilityHistoryV1Resp(
        )
        """

    def testMarginGetMarginExchangeSmallLiabilityHistoryV1Resp(self):
        """Test MarginGetMarginExchangeSmallLiabilityHistoryV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
