# OptionsDeleteAllOpenOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_delete_all_open_orders_v1_resp import OptionsDeleteAllOpenOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsDeleteAllOpenOrdersV1Resp from a JSON string
options_delete_all_open_orders_v1_resp_instance = OptionsDeleteAllOpenOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsDeleteAllOpenOrdersV1Resp.to_json())

# convert the object into a dict
options_delete_all_open_orders_v1_resp_dict = options_delete_all_open_orders_v1_resp_instance.to_dict()
# create an instance of OptionsDeleteAllOpenOrdersV1Resp from a dict
options_delete_all_open_orders_v1_resp_from_dict = OptionsDeleteAllOpenOrdersV1Resp.from_dict(options_delete_all_open_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


