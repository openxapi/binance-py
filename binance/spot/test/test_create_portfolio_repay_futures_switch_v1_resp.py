# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_portfolio_repay_futures_switch_v1_resp import CreatePortfolioRepayFuturesSwitchV1Resp

class TestCreatePortfolioRepayFuturesSwitchV1Resp(unittest.TestCase):
    """CreatePortfolioRepayFuturesSwitchV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePortfolioRepayFuturesSwitchV1Resp:
        """Test CreatePortfolioRepayFuturesSwitchV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePortfolioRepayFuturesSwitchV1Resp`
        """
        model = CreatePortfolioRepayFuturesSwitchV1Resp()
        if include_optional:
            return CreatePortfolioRepayFuturesSwitchV1Resp(
                msg = ''
            )
        else:
            return CreatePortfolioRepayFuturesSwitchV1Resp(
        )
        """

    def testCreatePortfolioRepayFuturesSwitchV1Resp(self):
        """Test CreatePortfolioRepayFuturesSwitchV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
