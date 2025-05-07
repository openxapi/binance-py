# GetLoanVipOngoingOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetLoanVipOngoingOrdersV1RespRowsInner]**](GetLoanVipOngoingOrdersV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_ongoing_orders_v1_resp import GetLoanVipOngoingOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipOngoingOrdersV1Resp from a JSON string
get_loan_vip_ongoing_orders_v1_resp_instance = GetLoanVipOngoingOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipOngoingOrdersV1Resp.to_json())

# convert the object into a dict
get_loan_vip_ongoing_orders_v1_resp_dict = get_loan_vip_ongoing_orders_v1_resp_instance.to_dict()
# create an instance of GetLoanVipOngoingOrdersV1Resp from a dict
get_loan_vip_ongoing_orders_v1_resp_from_dict = GetLoanVipOngoingOrdersV1Resp.from_dict(get_loan_vip_ongoing_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


