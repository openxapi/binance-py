# OptionsGetBlockOrderExecuteV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_trade_settlement_key** | **str** |  | [optional] 
**create_time** | **int** |  | [optional] 
**expire_time** | **int** |  | [optional] 
**legs** | [**List[OptionsCreateBlockOrderCreateV1RespLegsInner]**](OptionsCreateBlockOrderCreateV1RespLegsInner.md) |  | [optional] 
**liquidity** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_block_order_execute_v1_resp import OptionsGetBlockOrderExecuteV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetBlockOrderExecuteV1Resp from a JSON string
options_get_block_order_execute_v1_resp_instance = OptionsGetBlockOrderExecuteV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsGetBlockOrderExecuteV1Resp.to_json())

# convert the object into a dict
options_get_block_order_execute_v1_resp_dict = options_get_block_order_execute_v1_resp_instance.to_dict()
# create an instance of OptionsGetBlockOrderExecuteV1Resp from a dict
options_get_block_order_execute_v1_resp_from_dict = OptionsGetBlockOrderExecuteV1Resp.from_dict(options_get_block_order_execute_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


