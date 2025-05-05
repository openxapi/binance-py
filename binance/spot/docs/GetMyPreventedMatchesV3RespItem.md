# GetMyPreventedMatchesV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_order_id** | **int** |  | [optional] 
**maker_prevented_quantity** | **str** |  | [optional] 
**maker_symbol** | **str** |  | [optional] 
**prevented_match_id** | **int** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**taker_order_id** | **int** |  | [optional] 
**trade_group_id** | **int** |  | [optional] 
**transact_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_my_prevented_matches_v3_resp_item import GetMyPreventedMatchesV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyPreventedMatchesV3RespItem from a JSON string
get_my_prevented_matches_v3_resp_item_instance = GetMyPreventedMatchesV3RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMyPreventedMatchesV3RespItem.to_json())

# convert the object into a dict
get_my_prevented_matches_v3_resp_item_dict = get_my_prevented_matches_v3_resp_item_instance.to_dict()
# create an instance of GetMyPreventedMatchesV3RespItem from a dict
get_my_prevented_matches_v3_resp_item_from_dict = GetMyPreventedMatchesV3RespItem.from_dict(get_my_prevented_matches_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


