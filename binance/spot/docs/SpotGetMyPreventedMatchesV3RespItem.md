# SpotGetMyPreventedMatchesV3RespItem


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
from binance.spot.models.spot_get_my_prevented_matches_v3_resp_item import SpotGetMyPreventedMatchesV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetMyPreventedMatchesV3RespItem from a JSON string
spot_get_my_prevented_matches_v3_resp_item_instance = SpotGetMyPreventedMatchesV3RespItem.from_json(json)
# print the JSON string representation of the object
print(SpotGetMyPreventedMatchesV3RespItem.to_json())

# convert the object into a dict
spot_get_my_prevented_matches_v3_resp_item_dict = spot_get_my_prevented_matches_v3_resp_item_instance.to_dict()
# create an instance of SpotGetMyPreventedMatchesV3RespItem from a dict
spot_get_my_prevented_matches_v3_resp_item_from_dict = SpotGetMyPreventedMatchesV3RespItem.from_dict(spot_get_my_prevented_matches_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


