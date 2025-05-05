# GetMarginIsolatedMarginDataV1RespItemDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borrow_limit** | **str** |  | [optional] 
**coin** | **str** |  | [optional] 
**daily_interest** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_isolated_margin_data_v1_resp_item_data_inner import GetMarginIsolatedMarginDataV1RespItemDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginIsolatedMarginDataV1RespItemDataInner from a JSON string
get_margin_isolated_margin_data_v1_resp_item_data_inner_instance = GetMarginIsolatedMarginDataV1RespItemDataInner.from_json(json)
# print the JSON string representation of the object
print(GetMarginIsolatedMarginDataV1RespItemDataInner.to_json())

# convert the object into a dict
get_margin_isolated_margin_data_v1_resp_item_data_inner_dict = get_margin_isolated_margin_data_v1_resp_item_data_inner_instance.to_dict()
# create an instance of GetMarginIsolatedMarginDataV1RespItemDataInner from a dict
get_margin_isolated_margin_data_v1_resp_item_data_inner_from_dict = GetMarginIsolatedMarginDataV1RespItemDataInner.from_dict(get_margin_isolated_margin_data_v1_resp_item_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


