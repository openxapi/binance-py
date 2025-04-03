# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.options.models.options_get_mark_v1_resp_item import OptionsGetMarkV1RespItem

class TestOptionsGetMarkV1RespItem(unittest.TestCase):
    """OptionsGetMarkV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsGetMarkV1RespItem:
        """Test OptionsGetMarkV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsGetMarkV1RespItem`
        """
        model = OptionsGetMarkV1RespItem()
        if include_optional:
            return OptionsGetMarkV1RespItem(
                ask_iv = '',
                bid_iv = '',
                delta = '',
                gamma = '',
                high_price_limit = '',
                low_price_limit = '',
                mark_iv = '',
                mark_price = '',
                risk_free_interest = '',
                symbol = '',
                theta = '',
                vega = ''
            )
        else:
            return OptionsGetMarkV1RespItem(
        )
        """

    def testOptionsGetMarkV1RespItem(self):
        """Test OptionsGetMarkV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
