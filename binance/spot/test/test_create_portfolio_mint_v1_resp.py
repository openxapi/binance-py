# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_portfolio_mint_v1_resp import CreatePortfolioMintV1Resp

class TestCreatePortfolioMintV1Resp(unittest.TestCase):
    """CreatePortfolioMintV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePortfolioMintV1Resp:
        """Test CreatePortfolioMintV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePortfolioMintV1Resp`
        """
        model = CreatePortfolioMintV1Resp()
        if include_optional:
            return CreatePortfolioMintV1Resp(
                from_asset = '',
                from_asset_qty = 56,
                rate = 1.337,
                target_asset = '',
                target_asset_qty = 1.337
            )
        else:
            return CreatePortfolioMintV1Resp(
        )
        """

    def testCreatePortfolioMintV1Resp(self):
        """Test CreatePortfolioMintV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
