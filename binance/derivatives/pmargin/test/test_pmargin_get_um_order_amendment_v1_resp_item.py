# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_um_order_amendment_v1_resp_item import PmarginGetUmOrderAmendmentV1RespItem

class TestPmarginGetUmOrderAmendmentV1RespItem(unittest.TestCase):
    """PmarginGetUmOrderAmendmentV1RespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetUmOrderAmendmentV1RespItem:
        """Test PmarginGetUmOrderAmendmentV1RespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetUmOrderAmendmentV1RespItem`
        """
        model = PmarginGetUmOrderAmendmentV1RespItem()
        if include_optional:
            return PmarginGetUmOrderAmendmentV1RespItem(
                amendment = binance.derivatives.pmargin.models.pmargin_get_cm_order_amendment_v1_resp_item_amendment.PmarginGetCmOrderAmendmentV1RespItem_amendment(
                    count = 56, 
                    orig_qty = binance.derivatives.pmargin.models.pmargin_get_cm_order_amendment_v1_resp_item_amendment_orig_qty.PmarginGetCmOrderAmendmentV1RespItem_amendment_origQty(
                        after = '', 
                        before = '', ), 
                    price = binance.derivatives.pmargin.models.pmargin_get_cm_order_amendment_v1_resp_item_amendment_orig_qty.PmarginGetCmOrderAmendmentV1RespItem_amendment_origQty(
                        after = '', 
                        before = '', ), ),
                amendment_id = 56,
                client_order_id = '',
                order_id = 56,
                pair = '',
                price_match = '',
                symbol = '',
                time = 56
            )
        else:
            return PmarginGetUmOrderAmendmentV1RespItem(
        )
        """

    def testPmarginGetUmOrderAmendmentV1RespItem(self):
        """Test PmarginGetUmOrderAmendmentV1RespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
