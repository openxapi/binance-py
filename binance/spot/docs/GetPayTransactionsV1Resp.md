# GetPayTransactionsV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**data** | [**List[GetPayTransactionsV1RespDataInner]**](GetPayTransactionsV1RespDataInner.md) |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from binance.spot.models.get_pay_transactions_v1_resp import GetPayTransactionsV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayTransactionsV1Resp from a JSON string
get_pay_transactions_v1_resp_instance = GetPayTransactionsV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetPayTransactionsV1Resp.to_json())

# convert the object into a dict
get_pay_transactions_v1_resp_dict = get_pay_transactions_v1_resp_instance.to_dict()
# create an instance of GetPayTransactionsV1Resp from a dict
get_pay_transactions_v1_resp_from_dict = GetPayTransactionsV1Resp.from_dict(get_pay_transactions_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


