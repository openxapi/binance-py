# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_nft_history_withdraw_v1_resp_list_inner import GetNftHistoryWithdrawV1RespListInner

class TestGetNftHistoryWithdrawV1RespListInner(unittest.TestCase):
    """GetNftHistoryWithdrawV1RespListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetNftHistoryWithdrawV1RespListInner:
        """Test GetNftHistoryWithdrawV1RespListInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetNftHistoryWithdrawV1RespListInner`
        """
        model = GetNftHistoryWithdrawV1RespListInner()
        if include_optional:
            return GetNftHistoryWithdrawV1RespListInner(
                contract_adrress = '',
                fee = 1.337,
                fee_asset = '',
                network = '',
                timestamp = 56,
                token_id = '',
                tx_id = ''
            )
        else:
            return GetNftHistoryWithdrawV1RespListInner(
        )
        """

    def testGetNftHistoryWithdrawV1RespListInner(self):
        """Test GetNftHistoryWithdrawV1RespListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
