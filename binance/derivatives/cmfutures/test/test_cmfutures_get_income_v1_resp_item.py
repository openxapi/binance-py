# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.cmfutures.models.cmfutures_get_income_v1_resp_item import CmfuturesGetIncomeV1RespItem

class TestCmfuturesGetIncomeV1RespItem(unittest.TestCase):
    """CmfuturesGetIncomeV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmfuturesGetIncomeV1RespItem:
        """Test CmfuturesGetIncomeV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmfuturesGetIncomeV1RespItem`
        """
        model = CmfuturesGetIncomeV1RespItem()
        if include_optional:
            return CmfuturesGetIncomeV1RespItem(
                asset = '',
                income = '',
                income_type = '',
                info = '',
                symbol = '',
                time = 56,
                trade_id = '',
                tran_id = ''
            )
        else:
            return CmfuturesGetIncomeV1RespItem(
        )
        """

    def testCmfuturesGetIncomeV1RespItem(self):
        """Test CmfuturesGetIncomeV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
