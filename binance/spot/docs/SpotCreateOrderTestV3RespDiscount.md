# SpotCreateOrderTestV3RespDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount** | **str** |  | [optional] 
**discount_asset** | **str** |  | [optional] 
**enabled_for_account** | **bool** |  | [optional] 
**enabled_for_symbol** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_test_v3_resp_discount import SpotCreateOrderTestV3RespDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderTestV3RespDiscount from a JSON string
spot_create_order_test_v3_resp_discount_instance = SpotCreateOrderTestV3RespDiscount.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderTestV3RespDiscount.to_json())

# convert the object into a dict
spot_create_order_test_v3_resp_discount_dict = spot_create_order_test_v3_resp_discount_instance.to_dict()
# create an instance of SpotCreateOrderTestV3RespDiscount from a dict
spot_create_order_test_v3_resp_discount_from_dict = SpotCreateOrderTestV3RespDiscount.from_dict(spot_create_order_test_v3_resp_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


