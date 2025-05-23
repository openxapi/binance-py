# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.umfutures.models.get_symbol_config_v1_resp_item import GetSymbolConfigV1RespItem

class TestGetSymbolConfigV1RespItem(unittest.TestCase):
    """GetSymbolConfigV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSymbolConfigV1RespItem:
        """Test GetSymbolConfigV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSymbolConfigV1RespItem`
        """
        model = GetSymbolConfigV1RespItem()
        if include_optional:
            return GetSymbolConfigV1RespItem(
                is_auto_add_margin = '',
                leverage = 56,
                margin_type = '',
                max_notional_value = '',
                symbol = ''
            )
        else:
            return GetSymbolConfigV1RespItem(
        )
        """

    def testGetSymbolConfigV1RespItem(self):
        """Test GetSymbolConfigV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
