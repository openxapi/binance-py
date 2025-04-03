# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.umfutures.models.umfutures_get_futures_data_basis_resp_item import UmfuturesGetFuturesDataBasisRespItem

class TestUmfuturesGetFuturesDataBasisRespItem(unittest.TestCase):
    """UmfuturesGetFuturesDataBasisRespItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UmfuturesGetFuturesDataBasisRespItem:
        """Test UmfuturesGetFuturesDataBasisRespItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UmfuturesGetFuturesDataBasisRespItem`
        """
        model = UmfuturesGetFuturesDataBasisRespItem()
        if include_optional:
            return UmfuturesGetFuturesDataBasisRespItem(
                annualized_basis_rate = '',
                basis = '',
                basis_rate = '',
                contract_type = '',
                futures_price = '',
                index_price = '',
                pair = '',
                timestamp = 56
            )
        else:
            return UmfuturesGetFuturesDataBasisRespItem(
        )
        """

    def testUmfuturesGetFuturesDataBasisRespItem(self):
        """Test UmfuturesGetFuturesDataBasisRespItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
