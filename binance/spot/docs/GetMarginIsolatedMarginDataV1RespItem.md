# GetMarginIsolatedMarginDataV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetMarginIsolatedMarginDataV1RespItemDataInner]**](GetMarginIsolatedMarginDataV1RespItemDataInner.md) |  | [optional] 
**leverage** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**vip_level** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_isolated_margin_data_v1_resp_item import GetMarginIsolatedMarginDataV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginIsolatedMarginDataV1RespItem from a JSON string
get_margin_isolated_margin_data_v1_resp_item_instance = GetMarginIsolatedMarginDataV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetMarginIsolatedMarginDataV1RespItem.to_json())

# convert the object into a dict
get_margin_isolated_margin_data_v1_resp_item_dict = get_margin_isolated_margin_data_v1_resp_item_instance.to_dict()
# create an instance of GetMarginIsolatedMarginDataV1RespItem from a dict
get_margin_isolated_margin_data_v1_resp_item_from_dict = GetMarginIsolatedMarginDataV1RespItem.from_dict(get_margin_isolated_margin_data_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


