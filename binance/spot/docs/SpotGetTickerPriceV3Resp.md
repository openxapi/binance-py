# SpotGetTickerPriceV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_ticker_price_v3_resp import SpotGetTickerPriceV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetTickerPriceV3Resp from a JSON string
spot_get_ticker_price_v3_resp_instance = SpotGetTickerPriceV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotGetTickerPriceV3Resp.to_json())

# convert the object into a dict
spot_get_ticker_price_v3_resp_dict = spot_get_ticker_price_v3_resp_instance.to_dict()
# create an instance of SpotGetTickerPriceV3Resp from a dict
spot_get_ticker_price_v3_resp_from_dict = SpotGetTickerPriceV3Resp.from_dict(spot_get_ticker_price_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


