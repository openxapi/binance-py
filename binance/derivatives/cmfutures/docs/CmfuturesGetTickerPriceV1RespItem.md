# CmfuturesGetTickerPriceV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** |  | [optional] 
**ps** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_ticker_price_v1_resp_item import CmfuturesGetTickerPriceV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetTickerPriceV1RespItem from a JSON string
cmfutures_get_ticker_price_v1_resp_item_instance = CmfuturesGetTickerPriceV1RespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetTickerPriceV1RespItem.to_json())

# convert the object into a dict
cmfutures_get_ticker_price_v1_resp_item_dict = cmfutures_get_ticker_price_v1_resp_item_instance.to_dict()
# create an instance of CmfuturesGetTickerPriceV1RespItem from a dict
cmfutures_get_ticker_price_v1_resp_item_from_dict = CmfuturesGetTickerPriceV1RespItem.from_dict(cmfutures_get_ticker_price_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


