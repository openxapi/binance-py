# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_sub_account_assets_v3_resp import GetSubAccountAssetsV3Resp

class TestGetSubAccountAssetsV3Resp(unittest.TestCase):
    """GetSubAccountAssetsV3Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSubAccountAssetsV3Resp:
        """Test GetSubAccountAssetsV3Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSubAccountAssetsV3Resp`
        """
        model = GetSubAccountAssetsV3Resp()
        if include_optional:
            return GetSubAccountAssetsV3Resp(
                balances = [
                    binance.spot.models.get_sub_account_assets_v3_resp_balances_inner.GetSubAccountAssetsV3Resp_balances_inner(
                        asset = '', 
                        free = 56, 
                        freeze = 56, 
                        locked = 56, 
                        withdrawing = 56, )
                    ]
            )
        else:
            return GetSubAccountAssetsV3Resp(
        )
        """

    def testGetSubAccountAssetsV3Resp(self):
        """Test GetSubAccountAssetsV3Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
