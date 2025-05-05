# GetAccountCommissionV3RespDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | **str** |  | [optional] 
**discount_asset** | **str** |  | [optional] 
**enabled_for_account** | **bool** |  | [optional] 
**enabled_for_symbol** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.get_account_commission_v3_resp_discount import GetAccountCommissionV3RespDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountCommissionV3RespDiscount from a JSON string
get_account_commission_v3_resp_discount_instance = GetAccountCommissionV3RespDiscount.from_json(json)
# print the JSON string representation of the object
print(GetAccountCommissionV3RespDiscount.to_json())

# convert the object into a dict
get_account_commission_v3_resp_discount_dict = get_account_commission_v3_resp_discount_instance.to_dict()
# create an instance of GetAccountCommissionV3RespDiscount from a dict
get_account_commission_v3_resp_discount_from_dict = GetAccountCommissionV3RespDiscount.from_dict(get_account_commission_v3_resp_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


