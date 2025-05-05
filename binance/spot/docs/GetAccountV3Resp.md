# GetAccountV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** |  | [optional] 
**balances** | [**List[GetAccountSnapshotV1RespSnapshotVosInnerDataBalancesInner]**](GetAccountSnapshotV1RespSnapshotVosInnerDataBalancesInner.md) |  | [optional] 
**brokered** | **bool** |  | [optional] 
**buyer_commission** | **int** |  | [optional] 
**can_deposit** | **bool** |  | [optional] 
**can_trade** | **bool** |  | [optional] 
**can_withdraw** | **bool** |  | [optional] 
**commission_rates** | [**GetAccountCommissionV3RespStandardCommission**](GetAccountCommissionV3RespStandardCommission.md) |  | [optional] 
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
from binance.spot.models.get_account_v3_resp import GetAccountV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountV3Resp from a JSON string
get_account_v3_resp_instance = GetAccountV3Resp.from_json(json)
# print the JSON string representation of the object
print(GetAccountV3Resp.to_json())

# convert the object into a dict
get_account_v3_resp_dict = get_account_v3_resp_instance.to_dict()
# create an instance of GetAccountV3Resp from a dict
get_account_v3_resp_from_dict = GetAccountV3Resp.from_dict(get_account_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


