# CmfuturesGetCommissionRateV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_commission_rate** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**taker_commission_rate** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.cmfutures.models.cmfutures_get_commission_rate_v1_resp import CmfuturesGetCommissionRateV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CmfuturesGetCommissionRateV1Resp from a JSON string
cmfutures_get_commission_rate_v1_resp_instance = CmfuturesGetCommissionRateV1Resp.from_json(json)
# print the JSON string representation of the object
print(CmfuturesGetCommissionRateV1Resp.to_json())

# convert the object into a dict
cmfutures_get_commission_rate_v1_resp_dict = cmfutures_get_commission_rate_v1_resp_instance.to_dict()
# create an instance of CmfuturesGetCommissionRateV1Resp from a dict
cmfutures_get_commission_rate_v1_resp_from_dict = CmfuturesGetCommissionRateV1Resp.from_dict(cmfutures_get_commission_rate_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


