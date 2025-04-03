# coding: utf-8

"""
    Binance Algorithmic Trading API

    OpenAPI specification for Binance exchange - Algo API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.algo.models.api_error import APIError

class TestAPIError(unittest.TestCase):
    """APIError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> APIError:
        """Test APIError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `APIError`
        """
        model = APIError()
        if include_optional:
            return APIError(
                code = 56,
                msg = ''
            )
        else:
            return APIError(
        )
        """

    def testAPIError(self):
        """Test APIError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
