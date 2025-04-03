# UmfuturesGetFundingInfoV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_funding_rate_cap** | **str** |  | [optional] 
**adjusted_funding_rate_floor** | **str** |  | [optional] 
**disclaimer** | **bool** |  | [optional] 
**funding_interval_hours** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_funding_info_v1_resp_item import UmfuturesGetFundingInfoV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetFundingInfoV1RespItem from a JSON string
umfutures_get_funding_info_v1_resp_item_instance = UmfuturesGetFundingInfoV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetFundingInfoV1RespItem.to_json())

# convert the object into a dict
umfutures_get_funding_info_v1_resp_item_dict = umfutures_get_funding_info_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetFundingInfoV1RespItem from a dict
umfutures_get_funding_info_v1_resp_item_from_dict = UmfuturesGetFundingInfoV1RespItem.from_dict(umfutures_get_funding_info_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


