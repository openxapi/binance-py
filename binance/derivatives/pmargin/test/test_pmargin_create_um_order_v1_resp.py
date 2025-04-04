# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_create_um_order_v1_resp import PmarginCreateUmOrderV1Resp

class TestPmarginCreateUmOrderV1Resp(unittest.TestCase):
    """PmarginCreateUmOrderV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginCreateUmOrderV1Resp:
        """Test PmarginCreateUmOrderV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginCreateUmOrderV1Resp`
        """
        model = PmarginCreateUmOrderV1Resp()
        if include_optional:
            return PmarginCreateUmOrderV1Resp(
                avg_price = '',
                client_order_id = '',
                cum_qty = '',
                cum_quote = '',
                executed_qty = '',
                good_till_date = 56,
                order_id = 56,
                orig_qty = '',
                position_side = '',
                price = '',
                price_match = '',
                reduce_only = True,
                self_trade_prevention_mode = '',
                side = '',
                status = '',
                symbol = '',
                time_in_force = '',
                type = '',
                update_time = 56
            )
        else:
            return PmarginCreateUmOrderV1Resp(
        )
        """

    def testPmarginCreateUmOrderV1Resp(self):
        """Test PmarginCreateUmOrderV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
