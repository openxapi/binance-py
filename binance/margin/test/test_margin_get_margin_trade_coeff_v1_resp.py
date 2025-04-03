# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_get_margin_trade_coeff_v1_resp import MarginGetMarginTradeCoeffV1Resp

class TestMarginGetMarginTradeCoeffV1Resp(unittest.TestCase):
    """MarginGetMarginTradeCoeffV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginGetMarginTradeCoeffV1Resp:
        """Test MarginGetMarginTradeCoeffV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginGetMarginTradeCoeffV1Resp`
        """
        model = MarginGetMarginTradeCoeffV1Resp()
        if include_optional:
            return MarginGetMarginTradeCoeffV1Resp(
                force_liquidation_bar = '',
                margin_call_bar = '',
                normal_bar = ''
            )
        else:
            return MarginGetMarginTradeCoeffV1Resp(
        )
        """

    def testMarginGetMarginTradeCoeffV1Resp(self):
        """Test MarginGetMarginTradeCoeffV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
