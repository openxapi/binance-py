# GetLoanIncomeV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**tran_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_loan_income_v1_resp_item import GetLoanIncomeV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanIncomeV1RespItem from a JSON string
get_loan_income_v1_resp_item_instance = GetLoanIncomeV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetLoanIncomeV1RespItem.to_json())

# convert the object into a dict
get_loan_income_v1_resp_item_dict = get_loan_income_v1_resp_item_instance.to_dict()
# create an instance of GetLoanIncomeV1RespItem from a dict
get_loan_income_v1_resp_item_from_dict = GetLoanIncomeV1RespItem.from_dict(get_loan_income_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


