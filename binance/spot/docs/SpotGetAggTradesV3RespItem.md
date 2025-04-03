# SpotGetAggTradesV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m** | **bool** |  | [optional] 
**t** | **int** |  | [optional] 
**a** | **int** |  | [optional] 
**f** | **int** |  | [optional] 
**l** | **int** |  | [optional] 
**m** | **bool** |  | [optional] 
**p** | **str** |  | [optional] 
**q** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_agg_trades_v3_resp_item import SpotGetAggTradesV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetAggTradesV3RespItem from a JSON string
spot_get_agg_trades_v3_resp_item_instance = SpotGetAggTradesV3RespItem.from_json(json)
# print the JSON string representation of the object
print(SpotGetAggTradesV3RespItem.to_json())

# convert the object into a dict
spot_get_agg_trades_v3_resp_item_dict = spot_get_agg_trades_v3_resp_item_instance.to_dict()
# create an instance of SpotGetAggTradesV3RespItem from a dict
spot_get_agg_trades_v3_resp_item_from_dict = SpotGetAggTradesV3RespItem.from_dict(spot_get_agg_trades_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


