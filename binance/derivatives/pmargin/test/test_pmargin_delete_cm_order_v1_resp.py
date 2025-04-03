# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_delete_cm_order_v1_resp import PmarginDeleteCmOrderV1Resp

class TestPmarginDeleteCmOrderV1Resp(unittest.TestCase):
    """PmarginDeleteCmOrderV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginDeleteCmOrderV1Resp:
        """Test PmarginDeleteCmOrderV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginDeleteCmOrderV1Resp`
        """
        model = PmarginDeleteCmOrderV1Resp()
        if include_optional:
            return PmarginDeleteCmOrderV1Resp(
                avg_price = '',
                client_order_id = '',
                cum_base = '',
                cum_qty = '',
                executed_qty = '',
                order_id = 56,
                orig_qty = '',
                pair = '',
                position_side = '',
                price = '',
                reduce_only = True,
                side = '',
                status = '',
                symbol = '',
                time_in_force = '',
                type = '',
                update_time = 56
            )
        else:
            return PmarginDeleteCmOrderV1Resp(
        )
        """

    def testPmarginDeleteCmOrderV1Resp(self):
        """Test PmarginDeleteCmOrderV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
