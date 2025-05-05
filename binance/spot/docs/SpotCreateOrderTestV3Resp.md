# SpotCreateOrderTestV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | [**GetAccountCommissionV3RespDiscount**](GetAccountCommissionV3RespDiscount.md) |  | [optional] 
**standard_commission_for_order** | [**SpotCreateOrderTestV3RespStandardCommissionForOrder**](SpotCreateOrderTestV3RespStandardCommissionForOrder.md) |  | [optional] 
**tax_commission_for_order** | [**SpotCreateOrderTestV3RespStandardCommissionForOrder**](SpotCreateOrderTestV3RespStandardCommissionForOrder.md) |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_test_v3_resp import SpotCreateOrderTestV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderTestV3Resp from a JSON string
spot_create_order_test_v3_resp_instance = SpotCreateOrderTestV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderTestV3Resp.to_json())

# convert the object into a dict
spot_create_order_test_v3_resp_dict = spot_create_order_test_v3_resp_instance.to_dict()
# create an instance of SpotCreateOrderTestV3Resp from a dict
spot_create_order_test_v3_resp_from_dict = SpotCreateOrderTestV3Resp.from_dict(spot_create_order_test_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


