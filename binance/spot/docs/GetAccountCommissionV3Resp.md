# GetAccountCommissionV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | [**GetAccountCommissionV3RespDiscount**](GetAccountCommissionV3RespDiscount.md) |  | [optional] 
**standard_commission** | [**GetAccountCommissionV3RespStandardCommission**](GetAccountCommissionV3RespStandardCommission.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**tax_commission** | [**GetAccountCommissionV3RespStandardCommission**](GetAccountCommissionV3RespStandardCommission.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_account_commission_v3_resp import GetAccountCommissionV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountCommissionV3Resp from a JSON string
get_account_commission_v3_resp_instance = GetAccountCommissionV3Resp.from_json(json)
# print the JSON string representation of the object
print(GetAccountCommissionV3Resp.to_json())

# convert the object into a dict
get_account_commission_v3_resp_dict = get_account_commission_v3_resp_instance.to_dict()
# create an instance of GetAccountCommissionV3Resp from a dict
get_account_commission_v3_resp_from_dict = GetAccountCommissionV3Resp.from_dict(get_account_commission_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


