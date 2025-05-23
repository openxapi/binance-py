# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.get_broker_sub_account_bnb_burn_status_v1_resp import GetBrokerSubAccountBnbBurnStatusV1Resp

class TestGetBrokerSubAccountBnbBurnStatusV1Resp(unittest.TestCase):
    """GetBrokerSubAccountBnbBurnStatusV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetBrokerSubAccountBnbBurnStatusV1Resp:
        """Test GetBrokerSubAccountBnbBurnStatusV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBrokerSubAccountBnbBurnStatusV1Resp`
        """
        model = GetBrokerSubAccountBnbBurnStatusV1Resp()
        if include_optional:
            return GetBrokerSubAccountBnbBurnStatusV1Resp(
                interest_bnb_burn = True,
                spot_bnb_burn = True,
                sub_account_id = 56
            )
        else:
            return GetBrokerSubAccountBnbBurnStatusV1Resp(
        )
        """

    def testGetBrokerSubAccountBnbBurnStatusV1Resp(self):
        """Test GetBrokerSubAccountBnbBurnStatusV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
