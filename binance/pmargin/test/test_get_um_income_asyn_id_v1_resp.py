# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.pmargin.models.get_um_income_asyn_id_v1_resp import GetUmIncomeAsynIdV1Resp

class TestGetUmIncomeAsynIdV1Resp(unittest.TestCase):
    """GetUmIncomeAsynIdV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUmIncomeAsynIdV1Resp:
        """Test GetUmIncomeAsynIdV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUmIncomeAsynIdV1Resp`
        """
        model = GetUmIncomeAsynIdV1Resp()
        if include_optional:
            return GetUmIncomeAsynIdV1Resp(
                download_id = '',
                expiration_timestamp = 56,
                is_expired = None,
                notified = True,
                s3_link = None,
                status = '',
                url = ''
            )
        else:
            return GetUmIncomeAsynIdV1Resp(
        )
        """

    def testGetUmIncomeAsynIdV1Resp(self):
        """Test GetUmIncomeAsynIdV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
