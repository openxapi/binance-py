# SpotGetTickerPriceV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_ticker_price_v3_resp_item import SpotGetTickerPriceV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetTickerPriceV3RespItem from a JSON string
spot_get_ticker_price_v3_resp_item_instance = SpotGetTickerPriceV3RespItem.from_json(json)
# print the JSON string representation of the object
print(SpotGetTickerPriceV3RespItem.to_json())

# convert the object into a dict
spot_get_ticker_price_v3_resp_item_dict = spot_get_ticker_price_v3_resp_item_instance.to_dict()
# create an instance of SpotGetTickerPriceV3RespItem from a dict
spot_get_ticker_price_v3_resp_item_from_dict = SpotGetTickerPriceV3RespItem.from_dict(spot_get_ticker_price_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


