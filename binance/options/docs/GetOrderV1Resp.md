# GetOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_price** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**create_time** | **int** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**fee** | **str** |  | [optional] 
**mmp** | **bool** |  | [optional] 
**option_side** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**post_only** | **bool** |  | [optional] 
**price** | **str** |  | [optional] 
**price_scale** | **int** |  | [optional] 
**quantity** | **str** |  | [optional] 
**quantity_scale** | **int** |  | [optional] 
**quote_asset** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**side** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.options.models.get_order_v1_resp import GetOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderV1Resp from a JSON string
get_order_v1_resp_instance = GetOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetOrderV1Resp.to_json())

# convert the object into a dict
get_order_v1_resp_dict = get_order_v1_resp_instance.to_dict()
# create an instance of GetOrderV1Resp from a dict
get_order_v1_resp_from_dict = GetOrderV1Resp.from_dict(get_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


