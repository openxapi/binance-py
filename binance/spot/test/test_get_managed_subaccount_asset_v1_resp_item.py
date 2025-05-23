# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_managed_subaccount_asset_v1_resp_item import GetManagedSubaccountAssetV1RespItem

class TestGetManagedSubaccountAssetV1RespItem(unittest.TestCase):
    """GetManagedSubaccountAssetV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetManagedSubaccountAssetV1RespItem:
        """Test GetManagedSubaccountAssetV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetManagedSubaccountAssetV1RespItem`
        """
        model = GetManagedSubaccountAssetV1RespItem()
        if include_optional:
            return GetManagedSubaccountAssetV1RespItem(
                available_balance = '',
                btc_value = '',
                coin = '',
                in_order = '',
                name = '',
                total_balance = ''
            )
        else:
            return GetManagedSubaccountAssetV1RespItem(
        )
        """

    def testGetManagedSubaccountAssetV1RespItem(self):
        """Test GetManagedSubaccountAssetV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
