# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.spot_create_order_cancel_replace_v3_fail_resp import SpotCreateOrderCancelReplaceV3FailResp

class TestSpotCreateOrderCancelReplaceV3FailResp(unittest.TestCase):
    """SpotCreateOrderCancelReplaceV3FailResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotCreateOrderCancelReplaceV3FailResp:
        """Test SpotCreateOrderCancelReplaceV3FailResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotCreateOrderCancelReplaceV3FailResp`
        """
        model = SpotCreateOrderCancelReplaceV3FailResp()
        if include_optional:
            return SpotCreateOrderCancelReplaceV3FailResp(
                code = 56,
                data = { "cancelResult": "SUCCESS", "newOrderResult": "SUCCESS", "cancelResponse": { "symbol": "BTCUSDT", "origClientOrderId": "DnLo3vTAQcjha43lAZhZ0y", "orderId": 9, "orderListId": -1, "clientOrderId": "osxN3JXAtJvKvCqGeMWMVR", "transactTime": 1684804350068, "price": "0.01000000", "origQty": "0.000100", "executedQty": "0.00000000", "origQuoteOrderQty": "0.000000", "cummulativeQuoteQty": "0.00000000", "status": "CANCELED", "timeInForce": "GTC", "type": "LIMIT", "side": "SELL", "selfTradePreventionMode": "NONE" }, "newOrderResponse": { "symbol": "BTCUSDT", "orderId": 10, "orderListId": -1, "clientOrderId": "wOceeeOzNORyLiQfw7jd8S", "transactTime": 1652928801803, "price": "0.02000000", "origQty": "0.040000", "executedQty": "0.00000000", "cummulativeQuoteQty": "0.00000000", "origQuoteOrderQty": "0.000000", "status": "NEW", "timeInForce": "GTC", "type": "LIMIT", "side": "BUY", "workingTime": 1669277163808, "fills": [], "selfTradePreventionMode": "NONE" } },
                msg = ''
            )
        else:
            return SpotCreateOrderCancelReplaceV3FailResp(
        )
        """

    def testSpotCreateOrderCancelReplaceV3FailResp(self):
        """Test SpotCreateOrderCancelReplaceV3FailResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
