# CreateSorOrderV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_order_id** | **str** |  | [optional] 
**cummulative_quote_qty** | **str** |  | [optional] 
**executed_qty** | **str** |  | [optional] 
**fills** | [**List[CreateSorOrderV3RespFillsInner]**](CreateSorOrderV3RespFillsInner.md) |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**orig_quote_order_qty** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**self_trade_prevention_mode** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**transact_time** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**used_sor** | **bool** |  | [optional] 
**working_floor** | **str** |  | [optional] 
**working_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_sor_order_v3_resp import CreateSorOrderV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSorOrderV3Resp from a JSON string
create_sor_order_v3_resp_instance = CreateSorOrderV3Resp.from_json(json)
# print the JSON string representation of the object
print(CreateSorOrderV3Resp.to_json())

# convert the object into a dict
create_sor_order_v3_resp_dict = create_sor_order_v3_resp_instance.to_dict()
# create an instance of CreateSorOrderV3Resp from a dict
create_sor_order_v3_resp_from_dict = CreateSorOrderV3Resp.from_dict(create_sor_order_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


