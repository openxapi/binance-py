# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_um_force_orders_v1_resp_item import PmarginGetUmForceOrdersV1RespItem

class TestPmarginGetUmForceOrdersV1RespItem(unittest.TestCase):
    """PmarginGetUmForceOrdersV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetUmForceOrdersV1RespItem:
        """Test PmarginGetUmForceOrdersV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetUmForceOrdersV1RespItem`
        """
        model = PmarginGetUmForceOrdersV1RespItem()
        if include_optional:
            return PmarginGetUmForceOrdersV1RespItem(
                avg_price = '',
                client_order_id = '',
                cum_quote = '',
                executed_qty = '',
                order_id = 56,
                orig_qty = '',
                orig_type = '',
                position_side = '',
                price = '',
                reduce_only = True,
                side = '',
                status = '',
                symbol = '',
                time = 56,
                time_in_force = '',
                type = '',
                update_time = 56
            )
        else:
            return PmarginGetUmForceOrdersV1RespItem(
        )
        """

    def testPmarginGetUmForceOrdersV1RespItem(self):
        """Test PmarginGetUmForceOrdersV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
