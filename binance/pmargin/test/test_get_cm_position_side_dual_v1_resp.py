# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.pmargin.models.get_cm_position_side_dual_v1_resp import GetCmPositionSideDualV1Resp

class TestGetCmPositionSideDualV1Resp(unittest.TestCase):
    """GetCmPositionSideDualV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCmPositionSideDualV1Resp:
        """Test GetCmPositionSideDualV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCmPositionSideDualV1Resp`
        """
        model = GetCmPositionSideDualV1Resp()
        if include_optional:
            return GetCmPositionSideDualV1Resp(
                dual_side_position = True
            )
        else:
            return GetCmPositionSideDualV1Resp(
        )
        """

    def testGetCmPositionSideDualV1Resp(self):
        """Test GetCmPositionSideDualV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
