# GetCmAdlQuantileV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adl_quantile** | [**GetCmAdlQuantileV1RespItemAdlQuantile**](GetCmAdlQuantileV1RespItemAdlQuantile.md) |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_cm_adl_quantile_v1_resp_item import GetCmAdlQuantileV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetCmAdlQuantileV1RespItem from a JSON string
get_cm_adl_quantile_v1_resp_item_instance = GetCmAdlQuantileV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetCmAdlQuantileV1RespItem.to_json())

# convert the object into a dict
get_cm_adl_quantile_v1_resp_item_dict = get_cm_adl_quantile_v1_resp_item_instance.to_dict()
# create an instance of GetCmAdlQuantileV1RespItem from a dict
get_cm_adl_quantile_v1_resp_item_from_dict = GetCmAdlQuantileV1RespItem.from_dict(get_cm_adl_quantile_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


