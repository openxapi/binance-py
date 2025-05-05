# GetUmAccountV1RespPositionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_notional** | **str** |  | [optional] 
**bid_notional** | **str** |  | [optional] 
**entry_price** | **str** |  | [optional] 
**initial_margin** | **str** |  | [optional] 
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
from binance.pmargin.models.get_um_account_v1_resp_positions_inner import GetUmAccountV1RespPositionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmAccountV1RespPositionsInner from a JSON string
get_um_account_v1_resp_positions_inner_instance = GetUmAccountV1RespPositionsInner.from_json(json)
# print the JSON string representation of the object
print(GetUmAccountV1RespPositionsInner.to_json())

# convert the object into a dict
get_um_account_v1_resp_positions_inner_dict = get_um_account_v1_resp_positions_inner_instance.to_dict()
# create an instance of GetUmAccountV1RespPositionsInner from a dict
get_um_account_v1_resp_positions_inner_from_dict = GetUmAccountV1RespPositionsInner.from_dict(get_um_account_v1_resp_positions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


