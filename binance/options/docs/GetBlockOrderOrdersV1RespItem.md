# GetBlockOrderOrdersV1RespItem


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
from binance.options.models.get_block_order_orders_v1_resp_item import GetBlockOrderOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockOrderOrdersV1RespItem from a JSON string
get_block_order_orders_v1_resp_item_instance = GetBlockOrderOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetBlockOrderOrdersV1RespItem.to_json())

# convert the object into a dict
get_block_order_orders_v1_resp_item_dict = get_block_order_orders_v1_resp_item_instance.to_dict()
# create an instance of GetBlockOrderOrdersV1RespItem from a dict
get_block_order_orders_v1_resp_item_from_dict = GetBlockOrderOrdersV1RespItem.from_dict(get_block_order_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


