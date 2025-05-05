# GetTickerBookTickerV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_price** | **str** |  | [optional] 
**ask_qty** | **str** |  | [optional] 
**bid_price** | **str** |  | [optional] 
**bid_qty** | **str** |  | [optional] 
**last_update_id** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_ticker_book_ticker_v1_resp_item import GetTickerBookTickerV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetTickerBookTickerV1RespItem from a JSON string
get_ticker_book_ticker_v1_resp_item_instance = GetTickerBookTickerV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetTickerBookTickerV1RespItem.to_json())

# convert the object into a dict
get_ticker_book_ticker_v1_resp_item_dict = get_ticker_book_ticker_v1_resp_item_instance.to_dict()
# create an instance of GetTickerBookTickerV1RespItem from a dict
get_ticker_book_ticker_v1_resp_item_from_dict = GetTickerBookTickerV1RespItem.from_dict(get_ticker_book_ticker_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


