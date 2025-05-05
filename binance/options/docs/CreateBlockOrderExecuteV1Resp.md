# CreateBlockOrderExecuteV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_trade_settlement_key** | **str** |  | [optional] 
**create_time** | **int** |  | [optional] 
**expire_time** | **int** |  | [optional] 
**legs** | [**List[CreateBlockOrderExecuteV1RespLegsInner]**](CreateBlockOrderExecuteV1RespLegsInner.md) |  | [optional] 
**liquidity** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from binance.options.models.create_block_order_execute_v1_resp import CreateBlockOrderExecuteV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlockOrderExecuteV1Resp from a JSON string
create_block_order_execute_v1_resp_instance = CreateBlockOrderExecuteV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateBlockOrderExecuteV1Resp.to_json())

# convert the object into a dict
create_block_order_execute_v1_resp_dict = create_block_order_execute_v1_resp_instance.to_dict()
# create an instance of CreateBlockOrderExecuteV1Resp from a dict
create_block_order_execute_v1_resp_from_dict = CreateBlockOrderExecuteV1Resp.from_dict(create_block_order_execute_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


