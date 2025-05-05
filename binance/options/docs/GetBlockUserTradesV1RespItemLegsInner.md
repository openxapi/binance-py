# GetBlockUserTradesV1RespItemLegsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission** | **float** |  | [optional] 
**create_time** | **int** |  | [optional] 
**executed_amount** | **float** |  | [optional] 
**executed_qty** | **float** |  | [optional] 
**fee** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**liquidity** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**order_price** | **float** |  | [optional] 
**order_quantity** | **float** |  | [optional] 
**order_side** | **str** |  | [optional] 
**order_status** | **str** |  | [optional] 
**order_type** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**trade_id** | **int** |  | [optional] 
**trade_price** | **float** |  | [optional] 
**trade_qty** | **float** |  | [optional] 
**trade_time** | **int** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.options.models.get_block_user_trades_v1_resp_item_legs_inner import GetBlockUserTradesV1RespItemLegsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockUserTradesV1RespItemLegsInner from a JSON string
get_block_user_trades_v1_resp_item_legs_inner_instance = GetBlockUserTradesV1RespItemLegsInner.from_json(json)
# print the JSON string representation of the object
print(GetBlockUserTradesV1RespItemLegsInner.to_json())

# convert the object into a dict
get_block_user_trades_v1_resp_item_legs_inner_dict = get_block_user_trades_v1_resp_item_legs_inner_instance.to_dict()
# create an instance of GetBlockUserTradesV1RespItemLegsInner from a dict
get_block_user_trades_v1_resp_item_legs_inner_from_dict = GetBlockUserTradesV1RespItemLegsInner.from_dict(get_block_user_trades_v1_resp_item_legs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


