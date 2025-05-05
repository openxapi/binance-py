# GetAccountCommissionV3RespStandardCommission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer** | **str** |  | [optional] 
**maker** | **str** |  | [optional] 
**seller** | **str** |  | [optional] 
**taker** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_account_commission_v3_resp_standard_commission import GetAccountCommissionV3RespStandardCommission

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountCommissionV3RespStandardCommission from a JSON string
get_account_commission_v3_resp_standard_commission_instance = GetAccountCommissionV3RespStandardCommission.from_json(json)
# print the JSON string representation of the object
print(GetAccountCommissionV3RespStandardCommission.to_json())

# convert the object into a dict
get_account_commission_v3_resp_standard_commission_dict = get_account_commission_v3_resp_standard_commission_instance.to_dict()
# create an instance of GetAccountCommissionV3RespStandardCommission from a dict
get_account_commission_v3_resp_standard_commission_from_dict = GetAccountCommissionV3RespStandardCommission.from_dict(get_account_commission_v3_resp_standard_commission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


