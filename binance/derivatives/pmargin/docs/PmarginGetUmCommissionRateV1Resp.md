# PmarginGetUmCommissionRateV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_commission_rate** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**taker_commission_rate** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_commission_rate_v1_resp import PmarginGetUmCommissionRateV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmCommissionRateV1Resp from a JSON string
pmargin_get_um_commission_rate_v1_resp_instance = PmarginGetUmCommissionRateV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmCommissionRateV1Resp.to_json())

# convert the object into a dict
pmargin_get_um_commission_rate_v1_resp_dict = pmargin_get_um_commission_rate_v1_resp_instance.to_dict()
# create an instance of PmarginGetUmCommissionRateV1Resp from a dict
pmargin_get_um_commission_rate_v1_resp_from_dict = PmarginGetUmCommissionRateV1Resp.from_dict(pmargin_get_um_commission_rate_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


