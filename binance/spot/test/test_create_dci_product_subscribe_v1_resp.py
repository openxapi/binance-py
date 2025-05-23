# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from binance.spot.models.create_dci_product_subscribe_v1_resp import CreateDciProductSubscribeV1Resp

class TestCreateDciProductSubscribeV1Resp(unittest.TestCase):
    """CreateDciProductSubscribeV1Resp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateDciProductSubscribeV1Resp:
        """Test CreateDciProductSubscribeV1Resp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateDciProductSubscribeV1Resp`
        """
        model = CreateDciProductSubscribeV1Resp()
        if include_optional:
            return CreateDciProductSubscribeV1Resp(
                apr = '',
                auto_compound_plan = '',
                duration = 56,
                exercised_coin = '',
                invest_coin = '',
                option_type = '',
                order_id = 56,
                position_id = 56,
                purchase_status = '',
                purchase_time = 56,
                settle_date = 56,
                strike_price = '',
                subscription_amount = ''
            )
        else:
            return CreateDciProductSubscribeV1Resp(
        )
        """

    def testCreateDciProductSubscribeV1Resp(self):
        """Test CreateDciProductSubscribeV1Resp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
