# PmarginGetMarginForceOrdersV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[PmarginGetMarginForceOrdersV1RespRowsInner]**](PmarginGetMarginForceOrdersV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_margin_force_orders_v1_resp import PmarginGetMarginForceOrdersV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetMarginForceOrdersV1Resp from a JSON string
pmargin_get_margin_force_orders_v1_resp_instance = PmarginGetMarginForceOrdersV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetMarginForceOrdersV1Resp.to_json())

# convert the object into a dict
pmargin_get_margin_force_orders_v1_resp_dict = pmargin_get_margin_force_orders_v1_resp_instance.to_dict()
# create an instance of PmarginGetMarginForceOrdersV1Resp from a dict
pmargin_get_margin_force_orders_v1_resp_from_dict = PmarginGetMarginForceOrdersV1Resp.from_dict(pmargin_get_margin_force_orders_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


