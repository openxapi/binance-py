# CmfuturesGetUserTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_qty** | **str** |  | [optional] 
**buyer** | **bool** |  | [optional] 
**commission** | **str** |  | [optional] 
**commission_asset** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**maker** | **bool** |  | [optional] 
**margin_asset** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**position_side** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**realized_pnl** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_user_trades_v1_resp_item import CmfuturesGetUserTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetUserTradesV1RespItem from a JSON string
cmfutures_get_user_trades_v1_resp_item_instance = CmfuturesGetUserTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetUserTradesV1RespItem.to_json())

# convert the object into a dict
cmfutures_get_user_trades_v1_resp_item_dict = cmfutures_get_user_trades_v1_resp_item_instance.to_dict()
# create an instance of CmfuturesGetUserTradesV1RespItem from a dict
cmfutures_get_user_trades_v1_resp_item_from_dict = CmfuturesGetUserTradesV1RespItem.from_dict(cmfutures_get_user_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


