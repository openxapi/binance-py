# OptionsGetMarginAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**List[OptionsGetMarginAccountV1RespAssetInner]**](OptionsGetMarginAccountV1RespAssetInner.md) |  | [optional] 
**greek** | [**List[OptionsGetAccountV1RespGreekInner]**](OptionsGetAccountV1RespGreekInner.md) |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_margin_account_v1_resp import OptionsGetMarginAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetMarginAccountV1Resp from a JSON string
options_get_margin_account_v1_resp_instance = OptionsGetMarginAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsGetMarginAccountV1Resp.to_json())

# convert the object into a dict
options_get_margin_account_v1_resp_dict = options_get_margin_account_v1_resp_instance.to_dict()
# create an instance of OptionsGetMarginAccountV1Resp from a dict
options_get_margin_account_v1_resp_from_dict = OptionsGetMarginAccountV1Resp.from_dict(options_get_margin_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


