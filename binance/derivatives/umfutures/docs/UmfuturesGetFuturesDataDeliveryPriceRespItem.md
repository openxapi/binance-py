# UmfuturesGetFuturesDataDeliveryPriceRespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_price** | **float** |  | [optional] 
**delivery_time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_futures_data_delivery_price_resp_item import UmfuturesGetFuturesDataDeliveryPriceRespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetFuturesDataDeliveryPriceRespItem from a JSON string
umfutures_get_futures_data_delivery_price_resp_item_instance = UmfuturesGetFuturesDataDeliveryPriceRespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetFuturesDataDeliveryPriceRespItem.to_json())

# convert the object into a dict
umfutures_get_futures_data_delivery_price_resp_item_dict = umfutures_get_futures_data_delivery_price_resp_item_instance.to_dict()
# create an instance of UmfuturesGetFuturesDataDeliveryPriceRespItem from a dict
umfutures_get_futures_data_delivery_price_resp_item_from_dict = UmfuturesGetFuturesDataDeliveryPriceRespItem.from_dict(umfutures_get_futures_data_delivery_price_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


