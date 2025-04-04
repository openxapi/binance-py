# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.options.models.options_get_klines_v1_resp_item import OptionsGetKlinesV1RespItem

class TestOptionsGetKlinesV1RespItem(unittest.TestCase):
    """OptionsGetKlinesV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsGetKlinesV1RespItem:
        """Test OptionsGetKlinesV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsGetKlinesV1RespItem`
        """
        model = OptionsGetKlinesV1RespItem()
        if include_optional:
            return OptionsGetKlinesV1RespItem(
                amount = '',
                close = '',
                close_time = 56,
                high = '',
                interval = '',
                low = '',
                open = '',
                open_time = 56,
                taker_amount = '',
                taker_volume = '',
                trade_count = 56,
                volume = ''
            )
        else:
            return OptionsGetKlinesV1RespItem(
        )
        """

    def testOptionsGetKlinesV1RespItem(self):
        """Test OptionsGetKlinesV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
