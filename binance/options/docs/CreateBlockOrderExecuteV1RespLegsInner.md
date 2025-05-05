# CreateBlockOrderExecuteV1RespLegsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.options.models.create_block_order_execute_v1_resp_legs_inner import CreateBlockOrderExecuteV1RespLegsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlockOrderExecuteV1RespLegsInner from a JSON string
create_block_order_execute_v1_resp_legs_inner_instance = CreateBlockOrderExecuteV1RespLegsInner.from_json(json)
# print the JSON string representation of the object
print(CreateBlockOrderExecuteV1RespLegsInner.to_json())

# convert the object into a dict
create_block_order_execute_v1_resp_legs_inner_dict = create_block_order_execute_v1_resp_legs_inner_instance.to_dict()
# create an instance of CreateBlockOrderExecuteV1RespLegsInner from a dict
create_block_order_execute_v1_resp_legs_inner_from_dict = CreateBlockOrderExecuteV1RespLegsInner.from_dict(create_block_order_execute_v1_resp_legs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


