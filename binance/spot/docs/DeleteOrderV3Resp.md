# DeleteOrderV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orig_client_order_id** | **str** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**transact_time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.delete_order_v3_resp import DeleteOrderV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOrderV3Resp from a JSON string
delete_order_v3_resp_instance = DeleteOrderV3Resp.from_json(json)
# print the JSON string representation of the object
print(DeleteOrderV3Resp.to_json())

# convert the object into a dict
delete_order_v3_resp_dict = delete_order_v3_resp_instance.to_dict()
# create an instance of DeleteOrderV3Resp from a dict
delete_order_v3_resp_from_dict = DeleteOrderV3Resp.from_dict(delete_order_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


