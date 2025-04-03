# SpotGetAccountCommissionV3RespStandardCommission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer** | **str** |  | [optional] 
**maker** | **str** |  | [optional] 
**seller** | **str** |  | [optional] 
**taker** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_get_account_commission_v3_resp_standard_commission import SpotGetAccountCommissionV3RespStandardCommission

# TODO update the JSON string below
json = "{}"
# create an instance of SpotGetAccountCommissionV3RespStandardCommission from a JSON string
spot_get_account_commission_v3_resp_standard_commission_instance = SpotGetAccountCommissionV3RespStandardCommission.from_json(json)
# print the JSON string representation of the object
print(SpotGetAccountCommissionV3RespStandardCommission.to_json())

# convert the object into a dict
spot_get_account_commission_v3_resp_standard_commission_dict = spot_get_account_commission_v3_resp_standard_commission_instance.to_dict()
# create an instance of SpotGetAccountCommissionV3RespStandardCommission from a dict
spot_get_account_commission_v3_resp_standard_commission_from_dict = SpotGetAccountCommissionV3RespStandardCommission.from_dict(spot_get_account_commission_v3_resp_standard_commission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


