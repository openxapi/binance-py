# GetUmIncomeV1RespItem


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
from binance.pmargin.models.get_um_income_v1_resp_item import GetUmIncomeV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetUmIncomeV1RespItem from a JSON string
get_um_income_v1_resp_item_instance = GetUmIncomeV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetUmIncomeV1RespItem.to_json())

# convert the object into a dict
get_um_income_v1_resp_item_dict = get_um_income_v1_resp_item_instance.to_dict()
# create an instance of GetUmIncomeV1RespItem from a dict
get_um_income_v1_resp_item_from_dict = GetUmIncomeV1RespItem.from_dict(get_um_income_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


