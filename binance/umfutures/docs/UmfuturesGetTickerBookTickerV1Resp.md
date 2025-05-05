# UmfuturesGetTickerBookTickerV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_price** | **str** |  | [optional] 
**ask_qty** | **str** |  | [optional] 
**bid_price** | **str** |  | [optional] 
**bid_qty** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.umfutures_get_ticker_book_ticker_v1_resp import UmfuturesGetTickerBookTickerV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetTickerBookTickerV1Resp from a JSON string
umfutures_get_ticker_book_ticker_v1_resp_instance = UmfuturesGetTickerBookTickerV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetTickerBookTickerV1Resp.to_json())

# convert the object into a dict
umfutures_get_ticker_book_ticker_v1_resp_dict = umfutures_get_ticker_book_ticker_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetTickerBookTickerV1Resp from a dict
umfutures_get_ticker_book_ticker_v1_resp_from_dict = UmfuturesGetTickerBookTickerV1Resp.from_dict(umfutures_get_ticker_book_ticker_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


