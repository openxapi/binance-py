# SpotGetAccountCommissionV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | [**SpotCreateOrderTestV3RespDiscount**](SpotCreateOrderTestV3RespDiscount.md) |  | [optional] 
**standard_commission** | [**SpotGetAccountCommissionV3RespStandardCommission**](SpotGetAccountCommissionV3RespStandardCommission.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**tax_commission** | [**SpotGetAccountCommissionV3RespStandardCommission**](SpotGetAccountCommissionV3RespStandardCommission.md) |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_account_commission_v3_resp import SpotGetAccountCommissionV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetAccountCommissionV3Resp from a JSON string
spot_get_account_commission_v3_resp_instance = SpotGetAccountCommissionV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotGetAccountCommissionV3Resp.to_json())

# convert the object into a dict
spot_get_account_commission_v3_resp_dict = spot_get_account_commission_v3_resp_instance.to_dict()
# create an instance of SpotGetAccountCommissionV3Resp from a dict
spot_get_account_commission_v3_resp_from_dict = SpotGetAccountCommissionV3Resp.from_dict(spot_get_account_commission_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


