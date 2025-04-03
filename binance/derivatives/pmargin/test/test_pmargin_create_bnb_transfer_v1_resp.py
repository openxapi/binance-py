# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_create_bnb_transfer_v1_resp import PmarginCreateBnbTransferV1Resp

class TestPmarginCreateBnbTransferV1Resp(unittest.TestCase):
    """PmarginCreateBnbTransferV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginCreateBnbTransferV1Resp:
        """Test PmarginCreateBnbTransferV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginCreateBnbTransferV1Resp`
        """
        model = PmarginCreateBnbTransferV1Resp()
        if include_optional:
            return PmarginCreateBnbTransferV1Resp(
                tran_id = 56
            )
        else:
            return PmarginCreateBnbTransferV1Resp(
        )
        """

    def testPmarginCreateBnbTransferV1Resp(self):
        """Test PmarginCreateBnbTransferV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
