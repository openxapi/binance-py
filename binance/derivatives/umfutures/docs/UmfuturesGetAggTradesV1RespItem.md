# UmfuturesGetAggTradesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t** | **int** |  | [optional] 
**a** | **int** |  | [optional] 
**f** | **int** |  | [optional] 
**l** | **int** |  | [optional] 
**m** | **bool** |  | [optional] 
**p** | **str** |  | [optional] 
**q** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_agg_trades_v1_resp_item import UmfuturesGetAggTradesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetAggTradesV1RespItem from a JSON string
umfutures_get_agg_trades_v1_resp_item_instance = UmfuturesGetAggTradesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetAggTradesV1RespItem.to_json())

# convert the object into a dict
umfutures_get_agg_trades_v1_resp_item_dict = umfutures_get_agg_trades_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetAggTradesV1RespItem from a dict
umfutures_get_agg_trades_v1_resp_item_from_dict = UmfuturesGetAggTradesV1RespItem.from_dict(umfutures_get_agg_trades_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


