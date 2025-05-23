# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.pmargin.models.get_um_fee_burn_v1_resp import GetUmFeeBurnV1Resp

class TestGetUmFeeBurnV1Resp(unittest.TestCase):
    """GetUmFeeBurnV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUmFeeBurnV1Resp:
        """Test GetUmFeeBurnV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUmFeeBurnV1Resp`
        """
        model = GetUmFeeBurnV1Resp()
        if include_optional:
            return GetUmFeeBurnV1Resp(
                fee_burn = True
            )
        else:
            return GetUmFeeBurnV1Resp(
        )
        """

    def testGetUmFeeBurnV1Resp(self):
        """Test GetUmFeeBurnV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
