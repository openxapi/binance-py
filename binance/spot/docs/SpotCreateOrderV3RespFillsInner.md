# SpotCreateOrderV3RespFillsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**trade_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_v3_resp_fills_inner import SpotCreateOrderV3RespFillsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderV3RespFillsInner from a JSON string
spot_create_order_v3_resp_fills_inner_instance = SpotCreateOrderV3RespFillsInner.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderV3RespFillsInner.to_json())

# convert the object into a dict
spot_create_order_v3_resp_fills_inner_dict = spot_create_order_v3_resp_fills_inner_instance.to_dict()
# create an instance of SpotCreateOrderV3RespFillsInner from a dict
spot_create_order_v3_resp_fills_inner_from_dict = SpotCreateOrderV3RespFillsInner.from_dict(spot_create_order_v3_resp_fills_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


