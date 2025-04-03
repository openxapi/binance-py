# UmfuturesGetCommissionRateV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_commission_rate** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**taker_commission_rate** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_commission_rate_v1_resp import UmfuturesGetCommissionRateV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetCommissionRateV1Resp from a JSON string
umfutures_get_commission_rate_v1_resp_instance = UmfuturesGetCommissionRateV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetCommissionRateV1Resp.to_json())

# convert the object into a dict
umfutures_get_commission_rate_v1_resp_dict = umfutures_get_commission_rate_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetCommissionRateV1Resp from a dict
umfutures_get_commission_rate_v1_resp_from_dict = UmfuturesGetCommissionRateV1Resp.from_dict(umfutures_get_commission_rate_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


