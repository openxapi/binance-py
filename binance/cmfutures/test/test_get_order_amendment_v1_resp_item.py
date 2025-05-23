# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.cmfutures.models.get_order_amendment_v1_resp_item import GetOrderAmendmentV1RespItem

class TestGetOrderAmendmentV1RespItem(unittest.TestCase):
    """GetOrderAmendmentV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetOrderAmendmentV1RespItem:
        """Test GetOrderAmendmentV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetOrderAmendmentV1RespItem`
        """
        model = GetOrderAmendmentV1RespItem()
        if include_optional:
            return GetOrderAmendmentV1RespItem(
                amendment = binance.cmfutures.models.get_order_amendment_v1_resp_item_amendment.GetOrderAmendmentV1RespItem_amendment(
                    count = 56, 
                    orig_qty = binance.cmfutures.models.get_order_amendment_v1_resp_item_amendment_orig_qty.GetOrderAmendmentV1RespItem_amendment_origQty(
                        after = '', 
                        before = '', ), 
                    price = binance.cmfutures.models.get_order_amendment_v1_resp_item_amendment_orig_qty.GetOrderAmendmentV1RespItem_amendment_origQty(
                        after = '', 
                        before = '', ), ),
                amendment_id = 56,
                client_order_id = '',
                order_id = 56,
                pair = '',
                symbol = '',
                time = 56
            )
        else:
            return GetOrderAmendmentV1RespItem(
        )
        """

    def testGetOrderAmendmentV1RespItem(self):
        """Test GetOrderAmendmentV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
