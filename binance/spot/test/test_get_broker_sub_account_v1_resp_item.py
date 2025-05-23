# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_broker_sub_account_v1_resp_item import GetBrokerSubAccountV1RespItem

class TestGetBrokerSubAccountV1RespItem(unittest.TestCase):
    """GetBrokerSubAccountV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetBrokerSubAccountV1RespItem:
        """Test GetBrokerSubAccountV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBrokerSubAccountV1RespItem`
        """
        model = GetBrokerSubAccountV1RespItem()
        if include_optional:
            return GetBrokerSubAccountV1RespItem(
                create_time = 56,
                email = '',
                maker_commission = 1.337,
                margin_maker_commission = 56,
                margin_taker_commission = 56,
                subaccount_id = '',
                tag = '',
                taker_commission = 1.337
            )
        else:
            return GetBrokerSubAccountV1RespItem(
        )
        """

    def testGetBrokerSubAccountV1RespItem(self):
        """Test GetBrokerSubAccountV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
