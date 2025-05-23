# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_sub_account_futures_move_position_v1_resp_future_move_position_order_vo_list_inner import GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner

class TestGetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner(unittest.TestCase):
    """GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner:
        """Test GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner`
        """
        model = GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner()
        if include_optional:
            return GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner(
                from_user_email = '',
                position_side = '',
                price = '',
                product_type = '',
                quantity = '',
                side = '',
                symbol = '',
                time_stamp = 56,
                to_user_email = ''
            )
        else:
            return GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner(
        )
        """

    def testGetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner(self):
        """Test GetSubAccountFuturesMovePositionV1RespFutureMovePositionOrderVoListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
