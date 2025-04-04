# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_portfolio_negative_balance_exchange_record_v1_resp_rows_inner_details_inner import PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner

class TestPmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner(unittest.TestCase):
    """PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner:
        """Test PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner`
        """
        model = PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner()
        if include_optional:
            return PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner(
                asset = '',
                negative_balance = 56,
                negative_max_threshold = 56
            )
        else:
            return PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner(
        )
        """

    def testPmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner(self):
        """Test PmarginGetPortfolioNegativeBalanceExchangeRecordV1RespRowsInnerDetailsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
