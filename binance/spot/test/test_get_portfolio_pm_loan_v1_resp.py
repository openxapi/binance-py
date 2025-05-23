# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_portfolio_pm_loan_v1_resp import GetPortfolioPmLoanV1Resp

class TestGetPortfolioPmLoanV1Resp(unittest.TestCase):
    """GetPortfolioPmLoanV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPortfolioPmLoanV1Resp:
        """Test GetPortfolioPmLoanV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPortfolioPmLoanV1Resp`
        """
        model = GetPortfolioPmLoanV1Resp()
        if include_optional:
            return GetPortfolioPmLoanV1Resp(
                amount = '',
                asset = ''
            )
        else:
            return GetPortfolioPmLoanV1Resp(
        )
        """

    def testGetPortfolioPmLoanV1Resp(self):
        """Test GetPortfolioPmLoanV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
