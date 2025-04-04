# coding: utf-8

"""
    Binance Portfolio Margin Pro API

    OpenAPI specification for Binance exchange - Pmarginpro API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_interest_history_v1_resp_item import PmarginproGetPortfolioInterestHistoryV1RespItem

class TestPmarginproGetPortfolioInterestHistoryV1RespItem(unittest.TestCase):
    """PmarginproGetPortfolioInterestHistoryV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginproGetPortfolioInterestHistoryV1RespItem:
        """Test PmarginproGetPortfolioInterestHistoryV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginproGetPortfolioInterestHistoryV1RespItem`
        """
        model = PmarginproGetPortfolioInterestHistoryV1RespItem()
        if include_optional:
            return PmarginproGetPortfolioInterestHistoryV1RespItem(
                asset = '',
                interest = '',
                interest_accrued_time = 56,
                interest_rate = '',
                principal = ''
            )
        else:
            return PmarginproGetPortfolioInterestHistoryV1RespItem(
        )
        """

    def testPmarginproGetPortfolioInterestHistoryV1RespItem(self):
        """Test PmarginproGetPortfolioInterestHistoryV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
