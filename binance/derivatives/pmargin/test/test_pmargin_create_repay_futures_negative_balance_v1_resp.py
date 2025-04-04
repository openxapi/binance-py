# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_create_repay_futures_negative_balance_v1_resp import PmarginCreateRepayFuturesNegativeBalanceV1Resp

class TestPmarginCreateRepayFuturesNegativeBalanceV1Resp(unittest.TestCase):
    """PmarginCreateRepayFuturesNegativeBalanceV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginCreateRepayFuturesNegativeBalanceV1Resp:
        """Test PmarginCreateRepayFuturesNegativeBalanceV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginCreateRepayFuturesNegativeBalanceV1Resp`
        """
        model = PmarginCreateRepayFuturesNegativeBalanceV1Resp()
        if include_optional:
            return PmarginCreateRepayFuturesNegativeBalanceV1Resp(
                msg = ''
            )
        else:
            return PmarginCreateRepayFuturesNegativeBalanceV1Resp(
        )
        """

    def testPmarginCreateRepayFuturesNegativeBalanceV1Resp(self):
        """Test PmarginCreateRepayFuturesNegativeBalanceV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
