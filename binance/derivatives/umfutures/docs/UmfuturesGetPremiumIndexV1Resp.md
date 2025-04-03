# UmfuturesGetPremiumIndexV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_settle_price** | **str** |  | [optional] 
**index_price** | **str** |  | [optional] 
**interest_rate** | **str** |  | [optional] 
**last_funding_rate** | **str** |  | [optional] 
**mark_price** | **str** |  | [optional] 
**next_funding_time** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_premium_index_v1_resp import UmfuturesGetPremiumIndexV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetPremiumIndexV1Resp from a JSON string
umfutures_get_premium_index_v1_resp_instance = UmfuturesGetPremiumIndexV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetPremiumIndexV1Resp.to_json())

# convert the object into a dict
umfutures_get_premium_index_v1_resp_dict = umfutures_get_premium_index_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetPremiumIndexV1Resp from a dict
umfutures_get_premium_index_v1_resp_from_dict = UmfuturesGetPremiumIndexV1Resp.from_dict(umfutures_get_premium_index_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


