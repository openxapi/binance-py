# MarginGetMarginIsolatedMarginDataV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MarginGetMarginIsolatedMarginDataV1RespItemDataInner]**](MarginGetMarginIsolatedMarginDataV1RespItemDataInner.md) |  | [optional] 
**leverage** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**vip_level** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_isolated_margin_data_v1_resp_item import MarginGetMarginIsolatedMarginDataV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginIsolatedMarginDataV1RespItem from a JSON string
margin_get_margin_isolated_margin_data_v1_resp_item_instance = MarginGetMarginIsolatedMarginDataV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginIsolatedMarginDataV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_isolated_margin_data_v1_resp_item_dict = margin_get_margin_isolated_margin_data_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginIsolatedMarginDataV1RespItem from a dict
margin_get_margin_isolated_margin_data_v1_resp_item_from_dict = MarginGetMarginIsolatedMarginDataV1RespItem.from_dict(margin_get_margin_isolated_margin_data_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


