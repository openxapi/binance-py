# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_cm_order_amendment_v1_resp_item_amendment_orig_qty import PmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty

class TestPmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty(unittest.TestCase):
    """PmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty:
        """Test PmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty`
        """
        model = PmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty()
        if include_optional:
            return PmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty(
                after = '',
                before = ''
            )
        else:
            return PmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty(
        )
        """

    def testPmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty(self):
        """Test PmarginGetCmOrderAmendmentV1RespItemAmendmentOrigQty"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
