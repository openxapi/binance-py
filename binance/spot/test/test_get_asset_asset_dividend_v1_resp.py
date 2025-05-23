# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_asset_asset_dividend_v1_resp import GetAssetAssetDividendV1Resp

class TestGetAssetAssetDividendV1Resp(unittest.TestCase):
    """GetAssetAssetDividendV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAssetAssetDividendV1Resp:
        """Test GetAssetAssetDividendV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAssetAssetDividendV1Resp`
        """
        model = GetAssetAssetDividendV1Resp()
        if include_optional:
            return GetAssetAssetDividendV1Resp(
                rows = [
                    binance.spot.models.get_asset_asset_dividend_v1_resp_rows_inner.GetAssetAssetDividendV1Resp_rows_inner(
                        amount = '', 
                        asset = '', 
                        div_time = 56, 
                        en_info = '', 
                        id = 56, 
                        tran_id = 56, )
                    ],
                total = 56
            )
        else:
            return GetAssetAssetDividendV1Resp(
        )
        """

    def testGetAssetAssetDividendV1Resp(self):
        """Test GetAssetAssetDividendV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
