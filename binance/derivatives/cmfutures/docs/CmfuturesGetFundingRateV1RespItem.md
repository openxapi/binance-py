# CmfuturesGetFundingRateV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funding_rate** | **str** |  | [optional] 
**funding_time** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_funding_rate_v1_resp_item import CmfuturesGetFundingRateV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetFundingRateV1RespItem from a JSON string
cmfutures_get_funding_rate_v1_resp_item_instance = CmfuturesGetFundingRateV1RespItem.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetFundingRateV1RespItem.to_json())

# convert the object into a dict
cmfutures_get_funding_rate_v1_resp_item_dict = cmfutures_get_funding_rate_v1_resp_item_instance.to_dict()
# create an instance of CmfuturesGetFundingRateV1RespItem from a dict
cmfutures_get_funding_rate_v1_resp_item_from_dict = CmfuturesGetFundingRateV1RespItem.from_dict(cmfutures_get_funding_rate_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


