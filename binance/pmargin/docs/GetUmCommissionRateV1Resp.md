# GetUmCommissionRateV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_commission_rate** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**taker_commission_rate** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_um_commission_rate_v1_resp import GetUmCommissionRateV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmCommissionRateV1Resp from a JSON string
get_um_commission_rate_v1_resp_instance = GetUmCommissionRateV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetUmCommissionRateV1Resp.to_json())

# convert the object into a dict
get_um_commission_rate_v1_resp_dict = get_um_commission_rate_v1_resp_instance.to_dict()
# create an instance of GetUmCommissionRateV1Resp from a dict
get_um_commission_rate_v1_resp_from_dict = GetUmCommissionRateV1Resp.from_dict(get_um_commission_rate_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


