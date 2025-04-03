# CmfuturesGetFundingInfoV1RespItem


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
from binance.derivatives.cmfutures.models.cmfutures_get_funding_info_v1_resp_item import CmfuturesGetFundingInfoV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetFundingInfoV1RespItem from a JSON string
cmfutures_get_funding_info_v1_resp_item_instance = CmfuturesGetFundingInfoV1RespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetFundingInfoV1RespItem.to_json())

# convert the object into a dict
cmfutures_get_funding_info_v1_resp_item_dict = cmfutures_get_funding_info_v1_resp_item_instance.to_dict()
# create an instance of CmfuturesGetFundingInfoV1RespItem from a dict
cmfutures_get_funding_info_v1_resp_item_from_dict = CmfuturesGetFundingInfoV1RespItem.from_dict(cmfutures_get_funding_info_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


