# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_delete_um_conditional_order_v1_resp import PmarginDeleteUmConditionalOrderV1Resp

class TestPmarginDeleteUmConditionalOrderV1Resp(unittest.TestCase):
    """PmarginDeleteUmConditionalOrderV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginDeleteUmConditionalOrderV1Resp:
        """Test PmarginDeleteUmConditionalOrderV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginDeleteUmConditionalOrderV1Resp`
        """
        model = PmarginDeleteUmConditionalOrderV1Resp()
        if include_optional:
            return PmarginDeleteUmConditionalOrderV1Resp(
                activate_price = '',
                book_time = 56,
                good_till_date = 56,
                new_client_strategy_id = '',
                orig_qty = '',
                position_side = '',
                price = '',
                price_match = '',
                price_protect = True,
                price_rate = '',
                reduce_only = True,
                self_trade_prevention_mode = '',
                side = '',
                stop_price = '',
                strategy_id = 56,
                strategy_status = '',
                strategy_type = '',
                symbol = '',
                time_in_force = '',
                update_time = 56,
                working_type = ''
            )
        else:
            return PmarginDeleteUmConditionalOrderV1Resp(
        )
        """

    def testPmarginDeleteUmConditionalOrderV1Resp(self):
        """Test PmarginDeleteUmConditionalOrderV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
