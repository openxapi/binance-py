# OptionsGetBlockOrderOrdersV1RespItem


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
from binance.derivatives.options.models.options_get_block_order_orders_v1_resp_item import OptionsGetBlockOrderOrdersV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetBlockOrderOrdersV1RespItem from a JSON string
options_get_block_order_orders_v1_resp_item_instance = OptionsGetBlockOrderOrdersV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsGetBlockOrderOrdersV1RespItem.to_json())

# convert the object into a dict
options_get_block_order_orders_v1_resp_item_dict = options_get_block_order_orders_v1_resp_item_instance.to_dict()
# create an instance of OptionsGetBlockOrderOrdersV1RespItem from a dict
options_get_block_order_orders_v1_resp_item_from_dict = OptionsGetBlockOrderOrdersV1RespItem.from_dict(options_get_block_order_orders_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


