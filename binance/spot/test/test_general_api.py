# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.api.general_api import GeneralApi


class TestGeneralApi(unittest.TestCase):
    """GeneralApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GeneralApi()

    def tearDown(self) -> None:
        pass

    def test_spot_get_exchange_info_v3(self) -> None:
        """Test case for spot_get_exchange_info_v3

        Exchange information
        """
        pass

    def test_spot_get_ping_v3(self) -> None:
        """Test case for spot_get_ping_v3

        Test connectivity
        """
        pass

    def test_spot_get_time_v3(self) -> None:
        """Test case for spot_get_time_v3

        Check server time
        """
        pass


if __name__ == '__main__':
    unittest.main()
