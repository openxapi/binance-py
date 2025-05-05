# CreateSorOrderV3RespFillsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alloc_id** | **int** |  | [optional] 
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**match_type** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**trade_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_sor_order_v3_resp_fills_inner import CreateSorOrderV3RespFillsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSorOrderV3RespFillsInner from a JSON string
create_sor_order_v3_resp_fills_inner_instance = CreateSorOrderV3RespFillsInner.from_json(json)
# print the JSON string representation of the object
print(CreateSorOrderV3RespFillsInner.to_json())

# convert the object into a dict
create_sor_order_v3_resp_fills_inner_dict = create_sor_order_v3_resp_fills_inner_instance.to_dict()
# create an instance of CreateSorOrderV3RespFillsInner from a dict
create_sor_order_v3_resp_fills_inner_from_dict = CreateSorOrderV3RespFillsInner.from_dict(create_sor_order_v3_resp_fills_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


