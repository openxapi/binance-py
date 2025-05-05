# GetMarginForceOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetMarginForceOrdersV1RespRowsInner]**](GetMarginForceOrdersV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_margin_force_orders_v1_resp import GetMarginForceOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginForceOrdersV1Resp from a JSON string
get_margin_force_orders_v1_resp_instance = GetMarginForceOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMarginForceOrdersV1Resp.to_json())

# convert the object into a dict
get_margin_force_orders_v1_resp_dict = get_margin_force_orders_v1_resp_instance.to_dict()
# create an instance of GetMarginForceOrdersV1Resp from a dict
get_margin_force_orders_v1_resp_from_dict = GetMarginForceOrdersV1Resp.from_dict(get_margin_force_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


