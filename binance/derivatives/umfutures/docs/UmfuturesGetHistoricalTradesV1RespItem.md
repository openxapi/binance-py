# UmfuturesGetHistoricalTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_buyer_maker** | **bool** |  | [optional] 
**price** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**quote_qty** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_historical_trades_v1_resp_item import UmfuturesGetHistoricalTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetHistoricalTradesV1RespItem from a JSON string
umfutures_get_historical_trades_v1_resp_item_instance = UmfuturesGetHistoricalTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetHistoricalTradesV1RespItem.to_json())

# convert the object into a dict
umfutures_get_historical_trades_v1_resp_item_dict = umfutures_get_historical_trades_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetHistoricalTradesV1RespItem from a dict
umfutures_get_historical_trades_v1_resp_item_from_dict = UmfuturesGetHistoricalTradesV1RespItem.from_dict(umfutures_get_historical_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


