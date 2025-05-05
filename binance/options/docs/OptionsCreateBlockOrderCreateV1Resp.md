# OptionsCreateBlockOrderCreateV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_trade_settlement_key** | **str** |  | [optional] 
**expire_time** | **int** |  | [optional] 
**legs** | [**List[CreateBlockOrderExecuteV1RespLegsInner]**](CreateBlockOrderExecuteV1RespLegsInner.md) |  | [optional] 
**liquidity** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from binance.options.models.options_create_block_order_create_v1_resp import OptionsCreateBlockOrderCreateV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsCreateBlockOrderCreateV1Resp from a JSON string
options_create_block_order_create_v1_resp_instance = OptionsCreateBlockOrderCreateV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsCreateBlockOrderCreateV1Resp.to_json())

# convert the object into a dict
options_create_block_order_create_v1_resp_dict = options_create_block_order_create_v1_resp_instance.to_dict()
# create an instance of OptionsCreateBlockOrderCreateV1Resp from a dict
options_create_block_order_create_v1_resp_from_dict = OptionsCreateBlockOrderCreateV1Resp.from_dict(options_create_block_order_create_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


