# GetLoanVipRequestInterestRateV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**flexible_daily_interest_rate** | **str** |  | [optional] 
**flexible_yearly_interest_rate** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_vip_request_interest_rate_v1_resp_item import GetLoanVipRequestInterestRateV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanVipRequestInterestRateV1RespItem from a JSON string
get_loan_vip_request_interest_rate_v1_resp_item_instance = GetLoanVipRequestInterestRateV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetLoanVipRequestInterestRateV1RespItem.to_json())

# convert the object into a dict
get_loan_vip_request_interest_rate_v1_resp_item_dict = get_loan_vip_request_interest_rate_v1_resp_item_instance.to_dict()
# create an instance of GetLoanVipRequestInterestRateV1RespItem from a dict
get_loan_vip_request_interest_rate_v1_resp_item_from_dict = GetLoanVipRequestInterestRateV1RespItem.from_dict(get_loan_vip_request_interest_rate_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


