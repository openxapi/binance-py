# UmfuturesGetFundingRateV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funding_rate** | **str** |  | [optional] 
**funding_time** | **int** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_funding_rate_v1_resp_item import UmfuturesGetFundingRateV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetFundingRateV1RespItem from a JSON string
umfutures_get_funding_rate_v1_resp_item_instance = UmfuturesGetFundingRateV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetFundingRateV1RespItem.to_json())

# convert the object into a dict
umfutures_get_funding_rate_v1_resp_item_dict = umfutures_get_funding_rate_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetFundingRateV1RespItem from a dict
umfutures_get_funding_rate_v1_resp_item_from_dict = UmfuturesGetFundingRateV1RespItem.from_dict(umfutures_get_funding_rate_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


