# GetUmAccountV2RespPositionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_margin** | **str** |  | [optional] 
**maint_margin** | **str** |  | [optional] 
**notional** | **str** |  | [optional] 
**position_amt** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**unrealized_profit** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_account_v2_resp_positions_inner import GetUmAccountV2RespPositionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmAccountV2RespPositionsInner from a JSON string
get_um_account_v2_resp_positions_inner_instance = GetUmAccountV2RespPositionsInner.from_json(json)
# print the JSON string representation of the object
print(GetUmAccountV2RespPositionsInner.to_json())

# convert the object into a dict
get_um_account_v2_resp_positions_inner_dict = get_um_account_v2_resp_positions_inner_instance.to_dict()
# create an instance of GetUmAccountV2RespPositionsInner from a dict
get_um_account_v2_resp_positions_inner_from_dict = GetUmAccountV2RespPositionsInner.from_dict(get_um_account_v2_resp_positions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


