# UmfuturesGetTickerPriceV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.umfutures_get_ticker_price_v1_resp_item import UmfuturesGetTickerPriceV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetTickerPriceV1RespItem from a JSON string
umfutures_get_ticker_price_v1_resp_item_instance = UmfuturesGetTickerPriceV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetTickerPriceV1RespItem.to_json())

# convert the object into a dict
umfutures_get_ticker_price_v1_resp_item_dict = umfutures_get_ticker_price_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetTickerPriceV1RespItem from a dict
umfutures_get_ticker_price_v1_resp_item_from_dict = UmfuturesGetTickerPriceV1RespItem.from_dict(umfutures_get_ticker_price_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


