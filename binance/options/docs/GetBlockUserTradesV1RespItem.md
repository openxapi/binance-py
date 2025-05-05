# GetBlockUserTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_trade_settlement_key** | **str** |  | [optional] 
**cross_type** | **str** |  | [optional] 
**legs** | [**List[GetBlockUserTradesV1RespItemLegsInner]**](GetBlockUserTradesV1RespItemLegsInner.md) |  | [optional] 
**parent_order_id** | **str** |  | [optional] 

## Example

```python
from binance.options.models.get_block_user_trades_v1_resp_item import GetBlockUserTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockUserTradesV1RespItem from a JSON string
get_block_user_trades_v1_resp_item_instance = GetBlockUserTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetBlockUserTradesV1RespItem.to_json())

# convert the object into a dict
get_block_user_trades_v1_resp_item_dict = get_block_user_trades_v1_resp_item_instance.to_dict()
# create an instance of GetBlockUserTradesV1RespItem from a dict
get_block_user_trades_v1_resp_item_from_dict = GetBlockUserTradesV1RespItem.from_dict(get_block_user_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


