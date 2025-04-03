# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.spot_get_depth_v3_resp import SpotGetDepthV3Resp

class TestSpotGetDepthV3Resp(unittest.TestCase):
    """SpotGetDepthV3Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpotGetDepthV3Resp:
        """Test SpotGetDepthV3Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpotGetDepthV3Resp`
        """
        model = SpotGetDepthV3Resp()
        if include_optional:
            return SpotGetDepthV3Resp(
                asks = [
                    [
                        ''
                        ]
                    ],
                bids = [
                    [
                        ''
                        ]
                    ],
                last_update_id = 56
            )
        else:
            return SpotGetDepthV3Resp(
        )
        """

    def testSpotGetDepthV3Resp(self):
        """Test SpotGetDepthV3Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
