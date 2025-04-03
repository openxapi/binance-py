# coding: utf-8

"""
    Binance Convert API

    OpenAPI specification for Binance exchange - Convert API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.convert.models.convert_create_convert_limit_place_order_v1_resp import ConvertCreateConvertLimitPlaceOrderV1Resp

class TestConvertCreateConvertLimitPlaceOrderV1Resp(unittest.TestCase):
    """ConvertCreateConvertLimitPlaceOrderV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConvertCreateConvertLimitPlaceOrderV1Resp:
        """Test ConvertCreateConvertLimitPlaceOrderV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConvertCreateConvertLimitPlaceOrderV1Resp`
        """
        model = ConvertCreateConvertLimitPlaceOrderV1Resp()
        if include_optional:
            return ConvertCreateConvertLimitPlaceOrderV1Resp(
                from_amount = '',
                inverse_ratio = '',
                quote_id = '',
                ratio = '',
                to_amount = '',
                valid_timestamp = 56
            )
        else:
            return ConvertCreateConvertLimitPlaceOrderV1Resp(
        )
        """

    def testConvertCreateConvertLimitPlaceOrderV1Resp(self):
        """Test ConvertCreateConvertLimitPlaceOrderV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
