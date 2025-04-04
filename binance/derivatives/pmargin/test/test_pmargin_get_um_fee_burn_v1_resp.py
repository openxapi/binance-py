# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmargin.models.pmargin_get_um_fee_burn_v1_resp import PmarginGetUmFeeBurnV1Resp

class TestPmarginGetUmFeeBurnV1Resp(unittest.TestCase):
    """PmarginGetUmFeeBurnV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PmarginGetUmFeeBurnV1Resp:
        """Test PmarginGetUmFeeBurnV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PmarginGetUmFeeBurnV1Resp`
        """
        model = PmarginGetUmFeeBurnV1Resp()
        if include_optional:
            return PmarginGetUmFeeBurnV1Resp(
                fee_burn = True
            )
        else:
            return PmarginGetUmFeeBurnV1Resp(
        )
        """

    def testPmarginGetUmFeeBurnV1Resp(self):
        """Test PmarginGetUmFeeBurnV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
