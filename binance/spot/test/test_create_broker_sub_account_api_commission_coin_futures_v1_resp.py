# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_broker_sub_account_api_commission_coin_futures_v1_resp import CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp

class TestCreateBrokerSubAccountApiCommissionCoinFuturesV1Resp(unittest.TestCase):
    """CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp:
        """Test CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp`
        """
        model = CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp()
        if include_optional:
            return CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp(
                maker_adjustment = 56,
                maker_commission = 56,
                pair = '',
                sub_account_id = 56,
                taker_adjustment = 56,
                taker_commission = 56
            )
        else:
            return CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp(
        )
        """

    def testCreateBrokerSubAccountApiCommissionCoinFuturesV1Resp(self):
        """Test CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
