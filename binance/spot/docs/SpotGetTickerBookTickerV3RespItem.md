# SpotGetTickerBookTickerV3RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_price** | **str** |  | [optional] 
**ask_qty** | **str** |  | [optional] 
**bid_price** | **str** |  | [optional] 
**bid_qty** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_ticker_book_ticker_v3_resp_item import SpotGetTickerBookTickerV3RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetTickerBookTickerV3RespItem from a JSON string
spot_get_ticker_book_ticker_v3_resp_item_instance = SpotGetTickerBookTickerV3RespItem.from_json(json)
# print the JSON string representation of the object
print(SpotGetTickerBookTickerV3RespItem.to_json())

# convert the object into a dict
spot_get_ticker_book_ticker_v3_resp_item_dict = spot_get_ticker_book_ticker_v3_resp_item_instance.to_dict()
# create an instance of SpotGetTickerBookTickerV3RespItem from a dict
spot_get_ticker_book_ticker_v3_resp_item_from_dict = SpotGetTickerBookTickerV3RespItem.from_dict(spot_get_ticker_book_ticker_v3_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


