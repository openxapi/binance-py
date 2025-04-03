# SpotGetAccountV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** |  | [optional] 
**balances** | [**List[SpotGetAccountV3RespBalancesInner]**](SpotGetAccountV3RespBalancesInner.md) |  | [optional] 
**brokered** | **bool** |  | [optional] 
**buyer_commission** | **int** |  | [optional] 
**can_deposit** | **bool** |  | [optional] 
**can_trade** | **bool** |  | [optional] 
**can_withdraw** | **bool** |  | [optional] 
**commission_rates** | [**SpotGetAccountCommissionV3RespStandardCommission**](SpotGetAccountCommissionV3RespStandardCommission.md) |  | [optional] 
**maker_commission** | **int** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**prevent_sor** | **bool** |  | [optional] 
**require_self_trade_prevention** | **bool** |  | [optional] 
**seller_commission** | **int** |  | [optional] 
**taker_commission** | **int** |  | [optional] 
**uid** | **int** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_account_v3_resp import SpotGetAccountV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetAccountV3Resp from a JSON string
spot_get_account_v3_resp_instance = SpotGetAccountV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotGetAccountV3Resp.to_json())

# convert the object into a dict
spot_get_account_v3_resp_dict = spot_get_account_v3_resp_instance.to_dict()
# create an instance of SpotGetAccountV3Resp from a dict
spot_get_account_v3_resp_from_dict = SpotGetAccountV3Resp.from_dict(spot_get_account_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


