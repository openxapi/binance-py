# MarginGetMarginIsolatedMarginDataV1RespItemDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borrow_limit** | **str** |  | [optional] 
**coin** | **str** |  | [optional] 
**daily_interest** | **str** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_isolated_margin_data_v1_resp_item_data_inner import MarginGetMarginIsolatedMarginDataV1RespItemDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginIsolatedMarginDataV1RespItemDataInner from a JSON string
margin_get_margin_isolated_margin_data_v1_resp_item_data_inner_instance = MarginGetMarginIsolatedMarginDataV1RespItemDataInner.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginIsolatedMarginDataV1RespItemDataInner.to_json())

# convert the object into a dict
margin_get_margin_isolated_margin_data_v1_resp_item_data_inner_dict = margin_get_margin_isolated_margin_data_v1_resp_item_data_inner_instance.to_dict()
# create an instance of MarginGetMarginIsolatedMarginDataV1RespItemDataInner from a dict
margin_get_margin_isolated_margin_data_v1_resp_item_data_inner_from_dict = MarginGetMarginIsolatedMarginDataV1RespItemDataInner.from_dict(margin_get_margin_isolated_margin_data_v1_resp_item_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


