# GetFiatPaymentsV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**data** | [**List[GetFiatPaymentsV1RespDataInner]**](GetFiatPaymentsV1RespDataInner.md) |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_fiat_payments_v1_resp import GetFiatPaymentsV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetFiatPaymentsV1Resp from a JSON string
get_fiat_payments_v1_resp_instance = GetFiatPaymentsV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetFiatPaymentsV1Resp.to_json())

# convert the object into a dict
get_fiat_payments_v1_resp_dict = get_fiat_payments_v1_resp_instance.to_dict()
# create an instance of GetFiatPaymentsV1Resp from a dict
get_fiat_payments_v1_resp_from_dict = GetFiatPaymentsV1Resp.from_dict(get_fiat_payments_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


