# coding: utf-8

"""
    Binance Portfolio Margin Pro API

    OpenAPI specification for Binance exchange - Pmarginpro API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_pm_loan_history_v1_resp_rows_inner import PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner

class TestPmarginproGetPortfolioPmLoanHistoryV1RespRowsInner(unittest.TestCase):
    """PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner:
        """Test PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner`
        """
        model = PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner()
        if include_optional:
            return PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner(
                amount = '',
                asset = '',
                repay_time = 56
            )
        else:
            return PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner(
        )
        """

    def testPmarginproGetPortfolioPmLoanHistoryV1RespRowsInner(self):
        """Test PmarginproGetPortfolioPmLoanHistoryV1RespRowsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
