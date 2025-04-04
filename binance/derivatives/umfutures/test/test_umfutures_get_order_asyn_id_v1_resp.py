# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_order_asyn_id_v1_resp import UmfuturesGetOrderAsynIdV1Resp

class TestUmfuturesGetOrderAsynIdV1Resp(unittest.TestCase):
    """UmfuturesGetOrderAsynIdV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetOrderAsynIdV1Resp:
        """Test UmfuturesGetOrderAsynIdV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetOrderAsynIdV1Resp`
        """
        model = UmfuturesGetOrderAsynIdV1Resp()
        if include_optional:
            return UmfuturesGetOrderAsynIdV1Resp(
                download_id = '',
                expiration_timestamp = 56,
                is_expired = None,
                notified = True,
                status = '',
                url = ''
            )
        else:
            return UmfuturesGetOrderAsynIdV1Resp(
        )
        """

    def testUmfuturesGetOrderAsynIdV1Resp(self):
        """Test UmfuturesGetOrderAsynIdV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
