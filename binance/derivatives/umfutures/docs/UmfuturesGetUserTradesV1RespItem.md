# UmfuturesGetUserTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer** | **bool** |  | [optional] 
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**maker** | **bool** |  | [optional] 
**order_id** | **int** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**quote_qty** | **str** |  | [optional] 
**realized_pnl** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_user_trades_v1_resp_item import UmfuturesGetUserTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetUserTradesV1RespItem from a JSON string
umfutures_get_user_trades_v1_resp_item_instance = UmfuturesGetUserTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetUserTradesV1RespItem.to_json())

# convert the object into a dict
umfutures_get_user_trades_v1_resp_item_dict = umfutures_get_user_trades_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetUserTradesV1RespItem from a dict
umfutures_get_user_trades_v1_resp_item_from_dict = UmfuturesGetUserTradesV1RespItem.from_dict(umfutures_get_user_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


