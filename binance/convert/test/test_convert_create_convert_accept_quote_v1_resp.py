# coding: utf-8

"""
    Binance Convert API

    OpenAPI specification for Binance exchange - Convert API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.convert.models.convert_create_convert_accept_quote_v1_resp import ConvertCreateConvertAcceptQuoteV1Resp

class TestConvertCreateConvertAcceptQuoteV1Resp(unittest.TestCase):
    """ConvertCreateConvertAcceptQuoteV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConvertCreateConvertAcceptQuoteV1Resp:
        """Test ConvertCreateConvertAcceptQuoteV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConvertCreateConvertAcceptQuoteV1Resp`
        """
        model = ConvertCreateConvertAcceptQuoteV1Resp()
        if include_optional:
            return ConvertCreateConvertAcceptQuoteV1Resp(
                create_time = 56,
                order_id = '',
                order_status = ''
            )
        else:
            return ConvertCreateConvertAcceptQuoteV1Resp(
        )
        """

    def testConvertCreateConvertAcceptQuoteV1Resp(self):
        """Test ConvertCreateConvertAcceptQuoteV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
