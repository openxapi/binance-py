# GetSubAccountFuturesAccountV1RespAssetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**initial_margin** | **str** |  | [optional] 
**maintenance_margin** | **str** |  | [optional] 
**margin_balance** | **str** |  | [optional] 
**max_withdraw_amount** | **str** |  | [optional] 
**open_order_initial_margin** | **str** |  | [optional] 
**position_initial_margin** | **str** |  | [optional] 
**unrealized_profit** | **str** |  | [optional] 
**wallet_balance** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_futures_account_v1_resp_assets_inner import GetSubAccountFuturesAccountV1RespAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountFuturesAccountV1RespAssetsInner from a JSON string
get_sub_account_futures_account_v1_resp_assets_inner_instance = GetSubAccountFuturesAccountV1RespAssetsInner.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountFuturesAccountV1RespAssetsInner.to_json())

# convert the object into a dict
get_sub_account_futures_account_v1_resp_assets_inner_dict = get_sub_account_futures_account_v1_resp_assets_inner_instance.to_dict()
# create an instance of GetSubAccountFuturesAccountV1RespAssetsInner from a dict
get_sub_account_futures_account_v1_resp_assets_inner_from_dict = GetSubAccountFuturesAccountV1RespAssetsInner.from_dict(get_sub_account_futures_account_v1_resp_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


