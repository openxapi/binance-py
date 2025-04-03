# PmarginGetCmAdlQuantileV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adl_quantile** | [**PmarginGetCmAdlQuantileV1RespItemAdlQuantile**](PmarginGetCmAdlQuantileV1RespItemAdlQuantile.md) |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_cm_adl_quantile_v1_resp_item import PmarginGetCmAdlQuantileV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetCmAdlQuantileV1RespItem from a JSON string
pmargin_get_cm_adl_quantile_v1_resp_item_instance = PmarginGetCmAdlQuantileV1RespItem.from_json(json)
# print the JSON string representation of the object
print(PmarginGetCmAdlQuantileV1RespItem.to_json())

# convert the object into a dict
pmargin_get_cm_adl_quantile_v1_resp_item_dict = pmargin_get_cm_adl_quantile_v1_resp_item_instance.to_dict()
# create an instance of PmarginGetCmAdlQuantileV1RespItem from a dict
pmargin_get_cm_adl_quantile_v1_resp_item_from_dict = PmarginGetCmAdlQuantileV1RespItem.from_dict(pmargin_get_cm_adl_quantile_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


