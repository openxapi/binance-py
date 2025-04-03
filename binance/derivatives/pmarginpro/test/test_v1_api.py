# coding: utf-8

"""
    Binance Portfolio Margin Pro API

    OpenAPI specification for Binance exchange - Pmarginpro API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.derivatives.pmarginpro.api.v1_api import V1Api


class TestV1Api(unittest.TestCase):
    """V1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = V1Api()

    def tearDown(self) -> None:
        pass

    def test_pmarginpro_create_portfolio_asset_collection_v1(self) -> None:
        """Test case for pmarginpro_create_portfolio_asset_collection_v1

        Fund Collection by Asset(USER_DATA)
        """
        pass

    def test_pmarginpro_create_portfolio_auto_collection_v1(self) -> None:
        """Test case for pmarginpro_create_portfolio_auto_collection_v1

        Fund Auto-collection(USER_DATA)
        """
        pass

    def test_pmarginpro_create_portfolio_bnb_transfer_v1(self) -> None:
        """Test case for pmarginpro_create_portfolio_bnb_transfer_v1

        BNB transfer(USER_DATA)
        """
        pass

    def test_pmarginpro_create_portfolio_mint_v1(self) -> None:
        """Test case for pmarginpro_create_portfolio_mint_v1

        Mint BFUSD for Portfolio Margin(TRADE)
        """
        pass

    def test_pmarginpro_create_portfolio_redeem_v1(self) -> None:
        """Test case for pmarginpro_create_portfolio_redeem_v1

        Redeem BFUSD for Portfolio Margin(TRADE)
        """
        pass

    def test_pmarginpro_create_portfolio_repay_futures_negative_balance_v1(self) -> None:
        """Test case for pmarginpro_create_portfolio_repay_futures_negative_balance_v1

        Repay futures Negative Balance(USER_DATA)
        """
        pass

    def test_pmarginpro_create_portfolio_repay_futures_switch_v1(self) -> None:
        """Test case for pmarginpro_create_portfolio_repay_futures_switch_v1

        Change Auto-repay-futures Status(TRADE)
        """
        pass

    def test_pmarginpro_create_portfolio_repay_v1(self) -> None:
        """Test case for pmarginpro_create_portfolio_repay_v1

        Portfolio Margin Pro Bankruptcy Loan Repay
        """
        pass

    def test_pmarginpro_get_portfolio_account_v1(self) -> None:
        """Test case for pmarginpro_get_portfolio_account_v1

        Get Portfolio Margin Pro Account Info(USER_DATA)
        """
        pass

    def test_pmarginpro_get_portfolio_asset_index_price_v1(self) -> None:
        """Test case for pmarginpro_get_portfolio_asset_index_price_v1

        Query Portfolio Margin Asset Index Price (MARKET_DATA)
        """
        pass

    def test_pmarginpro_get_portfolio_balance_v1(self) -> None:
        """Test case for pmarginpro_get_portfolio_balance_v1

        Get Portfolio Margin Pro Account Balance(USER_DATA)
        """
        pass

    def test_pmarginpro_get_portfolio_collateral_rate_v1(self) -> None:
        """Test case for pmarginpro_get_portfolio_collateral_rate_v1

        Portfolio Margin Collateral Rate(MARKET_DATA)
        """
        pass

    def test_pmarginpro_get_portfolio_interest_history_v1(self) -> None:
        """Test case for pmarginpro_get_portfolio_interest_history_v1

        Query Portfolio Margin Pro Negative Balance Interest History(USER_DATA)
        """
        pass

    def test_pmarginpro_get_portfolio_margin_asset_leverage_v1(self) -> None:
        """Test case for pmarginpro_get_portfolio_margin_asset_leverage_v1

        Get Portfolio Margin Asset Leverage(USER_DATA)
        """
        pass

    def test_pmarginpro_get_portfolio_pm_loan_history_v1(self) -> None:
        """Test case for pmarginpro_get_portfolio_pm_loan_history_v1

        Query Portfolio Margin Pro Bankruptcy Loan Repay History(USER_DATA)
        """
        pass

    def test_pmarginpro_get_portfolio_pm_loan_v1(self) -> None:
        """Test case for pmarginpro_get_portfolio_pm_loan_v1

        Query Portfolio Margin Pro Bankruptcy Loan Amount(USER_DATA)
        """
        pass

    def test_pmarginpro_get_portfolio_repay_futures_switch_v1(self) -> None:
        """Test case for pmarginpro_get_portfolio_repay_futures_switch_v1

        Get Auto-repay-futures Status(USER_DATA)
        """
        pass


if __name__ == '__main__':
    unittest.main()
