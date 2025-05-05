# GetCommissionRateV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_commission_rate** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**taker_commission_rate** | **str** |  | [optional] 

## Example

```python
from binance.umfutures.models.get_commission_rate_v1_resp import GetCommissionRateV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommissionRateV1Resp from a JSON string
get_commission_rate_v1_resp_instance = GetCommissionRateV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetCommissionRateV1Resp.to_json())

# convert the object into a dict
get_commission_rate_v1_resp_dict = get_commission_rate_v1_resp_instance.to_dict()
# create an instance of GetCommissionRateV1Resp from a dict
get_commission_rate_v1_resp_from_dict = GetCommissionRateV1Resp.from_dict(get_commission_rate_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


