# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.models.margin_get_margin_transfer_v1_resp import MarginGetMarginTransferV1Resp

class TestMarginGetMarginTransferV1Resp(unittest.TestCase):
    """MarginGetMarginTransferV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginGetMarginTransferV1Resp:
        """Test MarginGetMarginTransferV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginGetMarginTransferV1Resp`
        """
        model = MarginGetMarginTransferV1Resp()
        if include_optional:
            return MarginGetMarginTransferV1Resp(
                rows = [
                    binance.margin.models.margin_get_margin_transfer_v1_resp_rows_inner.MarginGetMarginTransferV1Resp_rows_inner(
                        amount = '', 
                        asset = '', 
                        status = '', 
                        timestamp = 56, 
                        trans_from = '', 
                        trans_to = '', 
                        tx_id = 56, 
                        type = '', )
                    ],
                total = 56
            )
        else:
            return MarginGetMarginTransferV1Resp(
        )
        """

    def testMarginGetMarginTransferV1Resp(self):
        """Test MarginGetMarginTransferV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
