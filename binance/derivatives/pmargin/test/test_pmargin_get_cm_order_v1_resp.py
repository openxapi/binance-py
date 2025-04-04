# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_cm_order_v1_resp import PmarginGetCmOrderV1Resp

class TestPmarginGetCmOrderV1Resp(unittest.TestCase):
    """PmarginGetCmOrderV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetCmOrderV1Resp:
        """Test PmarginGetCmOrderV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetCmOrderV1Resp`
        """
        model = PmarginGetCmOrderV1Resp()
        if include_optional:
            return PmarginGetCmOrderV1Resp(
                avg_price = '',
                client_order_id = '',
                cum_base = '',
                executed_qty = '',
                order_id = 56,
                orig_qty = '',
                orig_type = '',
                pair = '',
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
            return PmarginGetCmOrderV1Resp(
        )
        """

    def testPmarginGetCmOrderV1Resp(self):
        """Test PmarginGetCmOrderV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
