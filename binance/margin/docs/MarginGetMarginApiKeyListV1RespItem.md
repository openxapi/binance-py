# MarginGetMarginApiKeyListV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**api_name** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**permission_mode** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_api_key_list_v1_resp_item import MarginGetMarginApiKeyListV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginApiKeyListV1RespItem from a JSON string
margin_get_margin_api_key_list_v1_resp_item_instance = MarginGetMarginApiKeyListV1RespItem.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginApiKeyListV1RespItem.to_json())

# convert the object into a dict
margin_get_margin_api_key_list_v1_resp_item_dict = margin_get_margin_api_key_list_v1_resp_item_instance.to_dict()
# create an instance of MarginGetMarginApiKeyListV1RespItem from a dict
margin_get_margin_api_key_list_v1_resp_item_from_dict = MarginGetMarginApiKeyListV1RespItem.from_dict(margin_get_margin_api_key_list_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


