# MarginGetMarginAccountV1RespUserAssetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**borrowed** | **str** |  | [optional] 
**free** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**locked** | **str** |  | [optional] 
**net_asset** | **str** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_account_v1_resp_user_assets_inner import MarginGetMarginAccountV1RespUserAssetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginAccountV1RespUserAssetsInner from a JSON string
margin_get_margin_account_v1_resp_user_assets_inner_instance = MarginGetMarginAccountV1RespUserAssetsInner.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginAccountV1RespUserAssetsInner.to_json())

# convert the object into a dict
margin_get_margin_account_v1_resp_user_assets_inner_dict = margin_get_margin_account_v1_resp_user_assets_inner_instance.to_dict()
# create an instance of MarginGetMarginAccountV1RespUserAssetsInner from a dict
margin_get_margin_account_v1_resp_user_assets_inner_from_dict = MarginGetMarginAccountV1RespUserAssetsInner.from_dict(margin_get_margin_account_v1_resp_user_assets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


