# DeleteCmConditionalOrderV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate_price** | **str** |  | [optional] 
**book_time** | **int** |  | [optional] 
**new_client_strategy_id** | **str** |  | [optional] 
**orig_qty** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_protect** | **bool** |  | [optional] 
**price_rate** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**side** | **str** |  | [optional] 
**stop_price** | **str** |  | [optional] 
**strategy_id** | **int** |  | [optional] 
**strategy_status** | **str** |  | [optional] 
**strategy_type** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time_in_force** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**working_type** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.delete_cm_conditional_order_v1_resp import DeleteCmConditionalOrderV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCmConditionalOrderV1Resp from a JSON string
delete_cm_conditional_order_v1_resp_instance = DeleteCmConditionalOrderV1Resp.from_json(json)
# print the JSON string representation of the object
print(DeleteCmConditionalOrderV1Resp.to_json())

# convert the object into a dict
delete_cm_conditional_order_v1_resp_dict = delete_cm_conditional_order_v1_resp_instance.to_dict()
# create an instance of DeleteCmConditionalOrderV1Resp from a dict
delete_cm_conditional_order_v1_resp_from_dict = DeleteCmConditionalOrderV1Resp.from_dict(delete_cm_conditional_order_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


