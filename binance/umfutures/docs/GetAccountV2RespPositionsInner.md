# GetAccountV2RespPositionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_notional** | **str** |  | [optional] 
**bid_notional** | **str** |  | [optional] 
**entry_price** | **str** |  | [optional] 
**initial_margin** | **str** |  | [optional] 
**isolated** | **bool** |  | [optional] 
**leverage** | **str** |  | [optional] 
**maint_margin** | **str** |  | [optional] 
**max_notional** | **str** |  | [optional] 
**open_order_initial_margin** | **str** |  | [optional] 
**position_amt** | **str** |  | [optional] 
**position_initial_margin** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**unrealized_profit** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_account_v2_resp_positions_inner import GetAccountV2RespPositionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountV2RespPositionsInner from a JSON string
get_account_v2_resp_positions_inner_instance = GetAccountV2RespPositionsInner.from_json(json)
# print the JSON string representation of the object
print(GetAccountV2RespPositionsInner.to_json())

# convert the object into a dict
get_account_v2_resp_positions_inner_dict = get_account_v2_resp_positions_inner_instance.to_dict()
# create an instance of GetAccountV2RespPositionsInner from a dict
get_account_v2_resp_positions_inner_from_dict = GetAccountV2RespPositionsInner.from_dict(get_account_v2_resp_positions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


