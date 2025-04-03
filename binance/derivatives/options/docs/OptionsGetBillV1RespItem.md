# OptionsGetBillV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**create_date** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_bill_v1_resp_item import OptionsGetBillV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetBillV1RespItem from a JSON string
options_get_bill_v1_resp_item_instance = OptionsGetBillV1RespItem.from_json(json)
# print the JSON string representation of the object
print(OptionsGetBillV1RespItem.to_json())

# convert the object into a dict
options_get_bill_v1_resp_item_dict = options_get_bill_v1_resp_item_instance.to_dict()
# create an instance of OptionsGetBillV1RespItem from a dict
options_get_bill_v1_resp_item_from_dict = OptionsGetBillV1RespItem.from_dict(options_get_bill_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


