# OptionsCreateOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_price** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**create_date** | **int** |  | [optional] 
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
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.options.models.options_create_order_v1_resp import OptionsCreateOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsCreateOrderV1Resp from a JSON string
options_create_order_v1_resp_instance = OptionsCreateOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsCreateOrderV1Resp.to_json())

# convert the object into a dict
options_create_order_v1_resp_dict = options_create_order_v1_resp_instance.to_dict()
# create an instance of OptionsCreateOrderV1Resp from a dict
options_create_order_v1_resp_from_dict = OptionsCreateOrderV1Resp.from_dict(options_create_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


