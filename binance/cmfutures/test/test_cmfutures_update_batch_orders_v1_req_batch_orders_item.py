# coding: utf-8

"""
    Binance COIN-M Futures API

    OpenAPI specification for Binance exchange - Cmfutures API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.cmfutures.models.cmfutures_update_batch_orders_v1_req_batch_orders_item import CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem

class TestCmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem(unittest.TestCase):
    """CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem:
        """Test CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem`
        """
        model = CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem()
        if include_optional:
            return CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem(
                order_id = 56,
                orig_client_order_id = '',
                price = '',
                quantity = '',
                recv_window = 56,
                side = '',
                symbol = '',
                timestamp = 56
            )
        else:
            return CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem(
                side = '',
                symbol = '',
                timestamp = 56,
        )
        """

    def testCmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem(self):
        """Test CmfuturesUpdateBatchOrdersV1ReqBatchOrdersItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
