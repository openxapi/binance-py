# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_simple_earn_flexible_history_collateral_record_v1_resp_rows_inner import GetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner

class TestGetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner(unittest.TestCase):
    """GetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner:
        """Test GetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner`
        """
        model = GetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner()
        if include_optional:
            return GetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner(
                amount = '',
                asset = '',
                create_time = 56,
                order_id = 56,
                product_id = '',
                product_name = '',
                type = ''
            )
        else:
            return GetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner(
        )
        """

    def testGetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner(self):
        """Test GetSimpleEarnFlexibleHistoryCollateralRecordV1RespRowsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
