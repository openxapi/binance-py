# SpotGetTickerBookTickerV3Resp


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
from binance.spot.models.spot_get_ticker_book_ticker_v3_resp import SpotGetTickerBookTickerV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetTickerBookTickerV3Resp from a JSON string
spot_get_ticker_book_ticker_v3_resp_instance = SpotGetTickerBookTickerV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotGetTickerBookTickerV3Resp.to_json())

# convert the object into a dict
spot_get_ticker_book_ticker_v3_resp_dict = spot_get_ticker_book_ticker_v3_resp_instance.to_dict()
# create an instance of SpotGetTickerBookTickerV3Resp from a dict
spot_get_ticker_book_ticker_v3_resp_from_dict = SpotGetTickerBookTickerV3Resp.from_dict(spot_get_ticker_book_ticker_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


