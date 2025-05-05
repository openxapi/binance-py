# GetAccountV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[GetAccountV3RespAssetsInner]**](GetAccountV3RespAssetsInner.md) |  | [optional] 
**available_balance** | **str** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**positions** | [**List[GetAccountV3RespPositionsInner]**](GetAccountV3RespPositionsInner.md) |  | [optional] 
**total_cross_un_pnl** | **str** |  | [optional] 
**total_cross_wallet_balance** | **str** |  | [optional] 
**total_initial_margin** | **str** |  | [optional] 
**total_maint_margin** | **str** |  | [optional] 
**total_margin_balance** | **str** |  | [optional] 
**total_open_order_initial_margin** | **str** |  | [optional] 
**total_position_initial_margin** | **str** |  | [optional] 
**total_unrealized_profit** | **str** |  | [optional] 
**total_wallet_balance** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_account_v3_resp import GetAccountV3Resp

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


