# OptionsCreateBlockOrderCreateV1RespLegsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_create_block_order_create_v1_resp_legs_inner import OptionsCreateBlockOrderCreateV1RespLegsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsCreateBlockOrderCreateV1RespLegsInner from a JSON string
options_create_block_order_create_v1_resp_legs_inner_instance = OptionsCreateBlockOrderCreateV1RespLegsInner.from_json(json)
# print the JSON string representation of the object
print(OptionsCreateBlockOrderCreateV1RespLegsInner.to_json())

# convert the object into a dict
options_create_block_order_create_v1_resp_legs_inner_dict = options_create_block_order_create_v1_resp_legs_inner_instance.to_dict()
# create an instance of OptionsCreateBlockOrderCreateV1RespLegsInner from a dict
options_create_block_order_create_v1_resp_legs_inner_from_dict = OptionsCreateBlockOrderCreateV1RespLegsInner.from_dict(options_create_block_order_create_v1_resp_legs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


