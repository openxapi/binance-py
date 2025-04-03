# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.spot_create_order_list_oco_v3_resp_orders_inner import SpotCreateOrderListOcoV3RespOrdersInner

class TestSpotCreateOrderListOcoV3RespOrdersInner(unittest.TestCase):
    """SpotCreateOrderListOcoV3RespOrdersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotCreateOrderListOcoV3RespOrdersInner:
        """Test SpotCreateOrderListOcoV3RespOrdersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotCreateOrderListOcoV3RespOrdersInner`
        """
        model = SpotCreateOrderListOcoV3RespOrdersInner()
        if include_optional:
            return SpotCreateOrderListOcoV3RespOrdersInner(
                client_order_id = '',
                order_id = 56,
                symbol = ''
            )
        else:
            return SpotCreateOrderListOcoV3RespOrdersInner(
        )
        """

    def testSpotCreateOrderListOcoV3RespOrdersInner(self):
        """Test SpotCreateOrderListOcoV3RespOrdersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
