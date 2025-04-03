# coding: utf-8

"""
    Binance Portfolio Margin Pro API

    OpenAPI specification for Binance exchange - Pmarginpro API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmarginpro.models.pmarginpro_create_portfolio_repay_v1_resp import PmarginproCreatePortfolioRepayV1Resp

class TestPmarginproCreatePortfolioRepayV1Resp(unittest.TestCase):
    """PmarginproCreatePortfolioRepayV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginproCreatePortfolioRepayV1Resp:
        """Test PmarginproCreatePortfolioRepayV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginproCreatePortfolioRepayV1Resp`
        """
        model = PmarginproCreatePortfolioRepayV1Resp()
        if include_optional:
            return PmarginproCreatePortfolioRepayV1Resp(
                tran_id = 56
            )
        else:
            return PmarginproCreatePortfolioRepayV1Resp(
        )
        """

    def testPmarginproCreatePortfolioRepayV1Resp(self):
        """Test PmarginproCreatePortfolioRepayV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
