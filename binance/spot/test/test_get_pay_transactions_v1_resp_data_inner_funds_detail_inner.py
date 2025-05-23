# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_pay_transactions_v1_resp_data_inner_funds_detail_inner import GetPayTransactionsV1RespDataInnerFundsDetailInner

class TestGetPayTransactionsV1RespDataInnerFundsDetailInner(unittest.TestCase):
    """GetPayTransactionsV1RespDataInnerFundsDetailInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPayTransactionsV1RespDataInnerFundsDetailInner:
        """Test GetPayTransactionsV1RespDataInnerFundsDetailInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPayTransactionsV1RespDataInnerFundsDetailInner`
        """
        model = GetPayTransactionsV1RespDataInnerFundsDetailInner()
        if include_optional:
            return GetPayTransactionsV1RespDataInnerFundsDetailInner(
                amount = '',
                currency = '',
                wallet_asset_cost = [
                    binance.spot.models.get_pay_transactions_v1_resp_data_inner_funds_detail_inner_wallet_asset_cost_inner.GetPayTransactionsV1Resp_data_inner_fundsDetail_inner_walletAssetCost_inner(
                        1 = '', )
                    ]
            )
        else:
            return GetPayTransactionsV1RespDataInnerFundsDetailInner(
        )
        """

    def testGetPayTransactionsV1RespDataInnerFundsDetailInner(self):
        """Test GetPayTransactionsV1RespDataInnerFundsDetailInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
