# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.options.models.options_get_account_v1_resp import OptionsGetAccountV1Resp

class TestOptionsGetAccountV1Resp(unittest.TestCase):
    """OptionsGetAccountV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsGetAccountV1Resp:
        """Test OptionsGetAccountV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsGetAccountV1Resp`
        """
        model = OptionsGetAccountV1Resp()
        if include_optional:
            return OptionsGetAccountV1Resp(
                asset = [
                    binance.derivatives.options.models.options_get_account_v1_resp_asset_inner.OptionsGetAccountV1Resp_asset_inner(
                        asset = '', 
                        available = '', 
                        equity = '', 
                        locked = '', 
                        margin_balance = '', 
                        unrealized_pnl = '', )
                    ],
                greek = [
                    binance.derivatives.options.models.options_get_account_v1_resp_greek_inner.OptionsGetAccountV1Resp_greek_inner(
                        delta = '', 
                        gamma = '', 
                        theta = '', 
                        underlying = '', 
                        vega = '', )
                    ],
                risk_level = '',
                time = 56
            )
        else:
            return OptionsGetAccountV1Resp(
        )
        """

    def testOptionsGetAccountV1Resp(self):
        """Test OptionsGetAccountV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
