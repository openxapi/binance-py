# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.api.staking_api import StakingApi


class TestStakingApi(unittest.TestCase):
    """StakingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StakingApi()

    def tearDown(self) -> None:
        pass

    def test_create_eth_staking_eth_redeem_v1(self) -> None:
        """Test case for create_eth_staking_eth_redeem_v1

        Redeem ETH(TRADE)
        """
        pass

    def test_create_eth_staking_eth_stake_v2(self) -> None:
        """Test case for create_eth_staking_eth_stake_v2

        Subscribe ETH Staking(TRADE)
        """
        pass

    def test_create_eth_staking_wbeth_wrap_v1(self) -> None:
        """Test case for create_eth_staking_wbeth_wrap_v1

        Wrap BETH(TRADE)
        """
        pass

    def test_create_sol_staking_sol_claim_v1(self) -> None:
        """Test case for create_sol_staking_sol_claim_v1

        Claim Boost Rewards(TRADE)
        """
        pass

    def test_create_sol_staking_sol_redeem_v1(self) -> None:
        """Test case for create_sol_staking_sol_redeem_v1

        Redeem SOL(TRADE)
        """
        pass

    def test_create_sol_staking_sol_stake_v1(self) -> None:
        """Test case for create_sol_staking_sol_stake_v1

        Subscribe SOL Staking(TRADE)
        """
        pass

    def test_get_eth_staking_account_v2(self) -> None:
        """Test case for get_eth_staking_account_v2

        ETH Staking account(USER_DATA)
        """
        pass

    def test_get_eth_staking_eth_history_rate_history_v1(self) -> None:
        """Test case for get_eth_staking_eth_history_rate_history_v1

        Get WBETH Rate History(USER_DATA)
        """
        pass

    def test_get_eth_staking_eth_history_redemption_history_v1(self) -> None:
        """Test case for get_eth_staking_eth_history_redemption_history_v1

        Get ETH redemption history(USER_DATA)
        """
        pass

    def test_get_eth_staking_eth_history_rewards_history_v1(self) -> None:
        """Test case for get_eth_staking_eth_history_rewards_history_v1

        Get BETH rewards distribution history(USER_DATA)
        """
        pass

    def test_get_eth_staking_eth_history_staking_history_v1(self) -> None:
        """Test case for get_eth_staking_eth_history_staking_history_v1

        Get ETH staking history(USER_DATA)
        """
        pass

    def test_get_eth_staking_eth_history_wbeth_rewards_history_v1(self) -> None:
        """Test case for get_eth_staking_eth_history_wbeth_rewards_history_v1

        Get WBETH rewards history(USER_DATA)
        """
        pass

    def test_get_eth_staking_eth_quota_v1(self) -> None:
        """Test case for get_eth_staking_eth_quota_v1

        Get current ETH staking quota(USER_DATA)
        """
        pass

    def test_get_eth_staking_wbeth_history_unwrap_history_v1(self) -> None:
        """Test case for get_eth_staking_wbeth_history_unwrap_history_v1

        Get WBETH unwrap history(USER_DATA)
        """
        pass

    def test_get_eth_staking_wbeth_history_wrap_history_v1(self) -> None:
        """Test case for get_eth_staking_wbeth_history_wrap_history_v1

        Get WBETH wrap history(USER_DATA)
        """
        pass

    def test_get_sol_staking_account_v1(self) -> None:
        """Test case for get_sol_staking_account_v1

        SOL Staking account(USER_DATA)
        """
        pass

    def test_get_sol_staking_sol_history_bnsol_rewards_history_v1(self) -> None:
        """Test case for get_sol_staking_sol_history_bnsol_rewards_history_v1

        Get BNSOL rewards history(USER_DATA)
        """
        pass

    def test_get_sol_staking_sol_history_boost_rewards_history_v1(self) -> None:
        """Test case for get_sol_staking_sol_history_boost_rewards_history_v1

        Get Boost Rewards History(USER_DATA)
        """
        pass

    def test_get_sol_staking_sol_history_rate_history_v1(self) -> None:
        """Test case for get_sol_staking_sol_history_rate_history_v1

        Get BNSOL Rate History(USER_DATA)
        """
        pass

    def test_get_sol_staking_sol_history_redemption_history_v1(self) -> None:
        """Test case for get_sol_staking_sol_history_redemption_history_v1

        Get SOL redemption history(USER_DATA)
        """
        pass

    def test_get_sol_staking_sol_history_staking_history_v1(self) -> None:
        """Test case for get_sol_staking_sol_history_staking_history_v1

        Get SOL staking history(USER_DATA)
        """
        pass

    def test_get_sol_staking_sol_history_unclaimed_rewards_v1(self) -> None:
        """Test case for get_sol_staking_sol_history_unclaimed_rewards_v1

        Get Unclaimed Rewards(USER_DATA)
        """
        pass

    def test_get_sol_staking_sol_quota_v1(self) -> None:
        """Test case for get_sol_staking_sol_quota_v1

        Get SOL staking quota details(USER_DATA)
        """
        pass


if __name__ == '__main__':
    unittest.main()
