# GetFiatPaymentsV1RespDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** |  | [optional] 
**crypto_currency** | **str** |  | [optional] 
**fiat_currency** | **str** |  | [optional] 
**obtain_amount** | **str** |  | [optional] 
**order_no** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**source_amount** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**total_fee** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_fiat_payments_v1_resp_data_inner import GetFiatPaymentsV1RespDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetFiatPaymentsV1RespDataInner from a JSON string
get_fiat_payments_v1_resp_data_inner_instance = GetFiatPaymentsV1RespDataInner.from_json(json)
# print the JSON string representation of the object
print(GetFiatPaymentsV1RespDataInner.to_json())

# convert the object into a dict
get_fiat_payments_v1_resp_data_inner_dict = get_fiat_payments_v1_resp_data_inner_instance.to_dict()
# create an instance of GetFiatPaymentsV1RespDataInner from a dict
get_fiat_payments_v1_resp_data_inner_from_dict = GetFiatPaymentsV1RespDataInner.from_dict(get_fiat_payments_v1_resp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


