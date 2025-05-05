# GetTickerPriceV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** |  | [optional] 
**ps** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_ticker_price_v1_resp_item import GetTickerPriceV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetTickerPriceV1RespItem from a JSON string
get_ticker_price_v1_resp_item_instance = GetTickerPriceV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetTickerPriceV1RespItem.to_json())

# convert the object into a dict
get_ticker_price_v1_resp_item_dict = get_ticker_price_v1_resp_item_instance.to_dict()
# create an instance of GetTickerPriceV1RespItem from a dict
get_ticker_price_v1_resp_item_from_dict = GetTickerPriceV1RespItem.from_dict(get_ticker_price_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


