# GetIncomeV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**income** | **str** |  | [optional] 
**income_type** | **str** |  | [optional] 
**info** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**trade_id** | **str** |  | [optional] 
**tran_id** | **str** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_income_v1_resp_item import GetIncomeV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetIncomeV1RespItem from a JSON string
get_income_v1_resp_item_instance = GetIncomeV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetIncomeV1RespItem.to_json())

# convert the object into a dict
get_income_v1_resp_item_dict = get_income_v1_resp_item_instance.to_dict()
# create an instance of GetIncomeV1RespItem from a dict
get_income_v1_resp_item_from_dict = GetIncomeV1RespItem.from_dict(get_income_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


