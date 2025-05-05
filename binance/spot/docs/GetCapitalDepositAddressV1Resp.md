# GetCapitalDepositAddressV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**coin** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_capital_deposit_address_v1_resp import GetCapitalDepositAddressV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetCapitalDepositAddressV1Resp from a JSON string
get_capital_deposit_address_v1_resp_instance = GetCapitalDepositAddressV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetCapitalDepositAddressV1Resp.to_json())

# convert the object into a dict
get_capital_deposit_address_v1_resp_dict = get_capital_deposit_address_v1_resp_instance.to_dict()
# create an instance of GetCapitalDepositAddressV1Resp from a dict
get_capital_deposit_address_v1_resp_from_dict = GetCapitalDepositAddressV1Resp.from_dict(get_capital_deposit_address_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


