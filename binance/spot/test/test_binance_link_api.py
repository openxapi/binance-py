# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.api.binance_link_api import BinanceLinkApi


class TestBinanceLinkApi(unittest.TestCase):
    """BinanceLinkApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BinanceLinkApi()

    def tearDown(self) -> None:
        pass

    def test_create_api_referral_customization_v1(self) -> None:
        """Test case for create_api_referral_customization_v1

        Customize Id For Client (USER DATA) （For Partner）
        """
        pass

    def test_create_api_referral_user_customization_v1(self) -> None:
        """Test case for create_api_referral_user_customization_v1

        Customize Id For Client  (USER DATA)(For client)
        """
        pass

    def test_create_broker_sub_account_api_commission_coin_futures_v1(self) -> None:
        """Test case for create_broker_sub_account_api_commission_coin_futures_v1

        Change Sub Account COIN-Ⓜ Futures Commission Adjustment
        """
        pass

    def test_create_broker_sub_account_api_commission_futures_v1(self) -> None:
        """Test case for create_broker_sub_account_api_commission_futures_v1

        Change Sub Account USDT-Ⓜ Futures Commission Adjustment
        """
        pass

    def test_create_broker_sub_account_api_commission_v1(self) -> None:
        """Test case for create_broker_sub_account_api_commission_v1

        Change Sub Account Commission
        """
        pass

    def test_create_broker_sub_account_api_ip_restriction_v2(self) -> None:
        """Test case for create_broker_sub_account_api_ip_restriction_v2

        Update IP Restriction for Sub-Account API key (For Master Account)
        """
        pass

    def test_create_broker_sub_account_api_permission_universal_transfer_v1(self) -> None:
        """Test case for create_broker_sub_account_api_permission_universal_transfer_v1

        Enable Universal Transfer Permission For Sub Account Api Key
        """
        pass

    def test_create_broker_sub_account_api_permission_v1(self) -> None:
        """Test case for create_broker_sub_account_api_permission_v1

        Change Sub Account Api Permission
        """
        pass

    def test_create_broker_sub_account_api_v1(self) -> None:
        """Test case for create_broker_sub_account_api_v1

        Create Api Key for Sub Account
        """
        pass

    def test_create_broker_sub_account_bnb_burn_margin_interest_v1(self) -> None:
        """Test case for create_broker_sub_account_bnb_burn_margin_interest_v1

        Enable Or Disable BNB Burn for Sub Account Margin Interest
        """
        pass

    def test_create_broker_sub_account_bnb_burn_spot_v1(self) -> None:
        """Test case for create_broker_sub_account_bnb_burn_spot_v1

        Enable Or Disable BNB Burn for Sub Account SPOT and MARGIN
        """
        pass

    def test_create_broker_sub_account_futures_v1(self) -> None:
        """Test case for create_broker_sub_account_futures_v1

        Enable Futures for Sub Account
        """
        pass

    def test_create_broker_sub_account_v1(self) -> None:
        """Test case for create_broker_sub_account_v1

        Create a Sub Account
        """
        pass

    def test_create_broker_transfer_futures_v1(self) -> None:
        """Test case for create_broker_transfer_futures_v1

        Sub Account Transfer（FUTURES）
        """
        pass

    def test_create_broker_transfer_v1(self) -> None:
        """Test case for create_broker_transfer_v1

        Sub Account Transfer（SPOT）
        """
        pass

    def test_create_broker_universal_transfer_v1(self) -> None:
        """Test case for create_broker_universal_transfer_v1

        Universal Transfer
        """
        pass

    def test_delete_broker_sub_account_api_ip_restriction_ip_list_v1(self) -> None:
        """Test case for delete_broker_sub_account_api_ip_restriction_ip_list_v1

        Delete IP Restriction for Sub Account Api Key
        """
        pass

    def test_delete_broker_sub_account_api_v1(self) -> None:
        """Test case for delete_broker_sub_account_api_v1

        Delete Sub Account Api Key
        """
        pass

    def test_delete_broker_sub_account_v1(self) -> None:
        """Test case for delete_broker_sub_account_v1

        Delete Sub Account
        """
        pass

    def test_get_api_referral_customization_v1(self) -> None:
        """Test case for get_api_referral_customization_v1

        Get Client Email Customized Id (USER DATA) （For Partner）
        """
        pass

    def test_get_api_referral_if_new_user_v1(self) -> None:
        """Test case for get_api_referral_if_new_user_v1

        Query Client If The New User (USER  DATA)
        """
        pass

    def test_get_api_referral_kickback_recent_record_v1(self) -> None:
        """Test case for get_api_referral_kickback_recent_record_v1

        Query Rebate Recent Record(For Client)
        """
        pass

    def test_get_api_referral_rebate_recent_record_v1(self) -> None:
        """Test case for get_api_referral_rebate_recent_record_v1

        Query Rebate Recent Record （USER DATA）(For Partner)
        """
        pass

    def test_get_api_referral_user_customization_v1(self) -> None:
        """Test case for get_api_referral_user_customization_v1

        Get User’s Customize Id (USER DATA)
        """
        pass

    def test_get_broker_info_v1(self) -> None:
        """Test case for get_broker_info_v1

        Link Account Information
        """
        pass

    def test_get_broker_rebate_futures_recent_record_v1(self) -> None:
        """Test case for get_broker_rebate_futures_recent_record_v1

        Query Broker Futures Commission Rebate Record
        """
        pass

    def test_get_broker_rebate_recent_record_v1(self) -> None:
        """Test case for get_broker_rebate_recent_record_v1

        Query Broker Commission Rebate Recent Record（Spot）
        """
        pass

    def test_get_broker_sub_account_api_commission_coin_futures_v1(self) -> None:
        """Test case for get_broker_sub_account_api_commission_coin_futures_v1

        Query Sub Account COIN-Ⓜ Futures Commission Adjustment
        """
        pass

    def test_get_broker_sub_account_api_commission_futures_v1(self) -> None:
        """Test case for get_broker_sub_account_api_commission_futures_v1

        Query Sub Account USDT-Ⓜ Futures Commission Adjustment
        """
        pass

    def test_get_broker_sub_account_api_ip_restriction_v1(self) -> None:
        """Test case for get_broker_sub_account_api_ip_restriction_v1

        Get IP Restriction for Sub Account Api Key
        """
        pass

    def test_get_broker_sub_account_api_v1(self) -> None:
        """Test case for get_broker_sub_account_api_v1

        Query Sub Account Api Key
        """
        pass

    def test_get_broker_sub_account_bnb_burn_status_v1(self) -> None:
        """Test case for get_broker_sub_account_bnb_burn_status_v1

        Get BNB Burn Status for Sub Account
        """
        pass

    def test_get_broker_sub_account_deposit_hist_v1(self) -> None:
        """Test case for get_broker_sub_account_deposit_hist_v1

        Get Sub Account Deposit History
        """
        pass

    def test_get_broker_sub_account_deposit_hist_v2(self) -> None:
        """Test case for get_broker_sub_account_deposit_hist_v2

        Get Sub Account Deposit History V2
        """
        pass

    def test_get_broker_sub_account_futures_summary_v3(self) -> None:
        """Test case for get_broker_sub_account_futures_summary_v3

        Query Sub Account Futures Asset info (V3)
        """
        pass

    def test_get_broker_sub_account_margin_summary_v1(self) -> None:
        """Test case for get_broker_sub_account_margin_summary_v1

        Query Sub Account Margin Asset info
        """
        pass

    def test_get_broker_sub_account_spot_summary_v1(self) -> None:
        """Test case for get_broker_sub_account_spot_summary_v1

        Query Sub Account Spot Asset info
        """
        pass

    def test_get_broker_sub_account_v1(self) -> None:
        """Test case for get_broker_sub_account_v1

        Query Sub Account
        """
        pass

    def test_get_broker_transfer_futures_v1(self) -> None:
        """Test case for get_broker_transfer_futures_v1

        Query Sub Account Transfer History（FUTURES）
        """
        pass

    def test_get_broker_transfer_v1(self) -> None:
        """Test case for get_broker_transfer_v1

        Query Sub Account Transfer History（SPOT）
        """
        pass

    def test_get_broker_universal_transfer_v1(self) -> None:
        """Test case for get_broker_universal_transfer_v1

        Query Universal Transfer History
        """
        pass


if __name__ == '__main__':
    unittest.main()
