# DeleteMarginOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**is_isolated** | **bool** |  | [optional] 
**order_id** | **str** |  | [optional] 
**orig_client_order_id** | **str** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.delete_margin_order_v1_resp import DeleteMarginOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMarginOrderV1Resp from a JSON string
delete_margin_order_v1_resp_instance = DeleteMarginOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(DeleteMarginOrderV1Resp.to_json())

# convert the object into a dict
delete_margin_order_v1_resp_dict = delete_margin_order_v1_resp_instance.to_dict()
# create an instance of DeleteMarginOrderV1Resp from a dict
delete_margin_order_v1_resp_from_dict = DeleteMarginOrderV1Resp.from_dict(delete_margin_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


