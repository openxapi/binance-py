# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.options.models.options_get_income_asyn_id_v1_resp import OptionsGetIncomeAsynIdV1Resp

class TestOptionsGetIncomeAsynIdV1Resp(unittest.TestCase):
    """OptionsGetIncomeAsynIdV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionsGetIncomeAsynIdV1Resp:
        """Test OptionsGetIncomeAsynIdV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionsGetIncomeAsynIdV1Resp`
        """
        model = OptionsGetIncomeAsynIdV1Resp()
        if include_optional:
            return OptionsGetIncomeAsynIdV1Resp(
                download_id = '',
                expiration_timestamp = 56,
                is_expired = None,
                notified = True,
                status = '',
                url = ''
            )
        else:
            return OptionsGetIncomeAsynIdV1Resp(
        )
        """

    def testOptionsGetIncomeAsynIdV1Resp(self):
        """Test OptionsGetIncomeAsynIdV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
