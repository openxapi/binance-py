# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_margin_force_orders_v1_resp_rows_inner import PmarginGetMarginForceOrdersV1RespRowsInner

class TestPmarginGetMarginForceOrdersV1RespRowsInner(unittest.TestCase):
    """PmarginGetMarginForceOrdersV1RespRowsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetMarginForceOrdersV1RespRowsInner:
        """Test PmarginGetMarginForceOrdersV1RespRowsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetMarginForceOrdersV1RespRowsInner`
        """
        model = PmarginGetMarginForceOrdersV1RespRowsInner()
        if include_optional:
            return PmarginGetMarginForceOrdersV1RespRowsInner(
                avg_price = '',
                executed_qty = '',
                order_id = 56,
                price = '',
                qty = '',
                side = '',
                symbol = '',
                time_in_force = '',
                updated_time = 56
            )
        else:
            return PmarginGetMarginForceOrdersV1RespRowsInner(
        )
        """

    def testPmarginGetMarginForceOrdersV1RespRowsInner(self):
        """Test PmarginGetMarginForceOrdersV1RespRowsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
