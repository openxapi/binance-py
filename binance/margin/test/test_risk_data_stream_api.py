# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.margin.api.risk_data_stream_api import RiskDataStreamApi


class TestRiskDataStreamApi(unittest.TestCase):
    """RiskDataStreamApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RiskDataStreamApi()

    def tearDown(self) -> None:
        pass

    def test_margin_create_margin_listen_key_v1(self) -> None:
        """Test case for margin_create_margin_listen_key_v1

        Start User Data Stream (USER_STREAM)
        """
        pass

    def test_margin_delete_margin_listen_key_v1(self) -> None:
        """Test case for margin_delete_margin_listen_key_v1

        Close User Data Stream (USER_STREAM)
        """
        pass

    def test_margin_update_margin_listen_key_v1(self) -> None:
        """Test case for margin_update_margin_listen_key_v1

        Keepalive User Data Stream (USER_STREAM)
        """
        pass


if __name__ == '__main__':
    unittest.main()
