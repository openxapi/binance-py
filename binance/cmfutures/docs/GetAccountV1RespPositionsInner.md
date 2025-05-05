# GetAccountV1RespPositionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_even_price** | **str** |  | [optional] 
**entry_price** | **str** |  | [optional] 
**initial_margin** | **str** |  | [optional] 
**isolated** | **bool** |  | [optional] 
**leverage** | **str** |  | [optional] 
**maint_margin** | **str** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**open_order_initial_margin** | **str** |  | [optional] 
**position_amt** | **str** |  | [optional] 
**position_initial_margin** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**unrealized_profit** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_account_v1_resp_positions_inner import GetAccountV1RespPositionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountV1RespPositionsInner from a JSON string
get_account_v1_resp_positions_inner_instance = GetAccountV1RespPositionsInner.from_json(json)
# print the JSON string representation of the object
print(GetAccountV1RespPositionsInner.to_json())

# convert the object into a dict
get_account_v1_resp_positions_inner_dict = get_account_v1_resp_positions_inner_instance.to_dict()
# create an instance of GetAccountV1RespPositionsInner from a dict
get_account_v1_resp_positions_inner_from_dict = GetAccountV1RespPositionsInner.from_dict(get_account_v1_resp_positions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


