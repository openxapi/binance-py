# GetMarginIsolatedAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[GetMarginIsolatedAccountV1RespAssetsInner]**](GetMarginIsolatedAccountV1RespAssetsInner.md) |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 
**total_liability_of_btc** | **str** |  | [optional] 
**total_net_asset_of_btc** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_isolated_account_v1_resp import GetMarginIsolatedAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginIsolatedAccountV1Resp from a JSON string
get_margin_isolated_account_v1_resp_instance = GetMarginIsolatedAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMarginIsolatedAccountV1Resp.to_json())

# convert the object into a dict
get_margin_isolated_account_v1_resp_dict = get_margin_isolated_account_v1_resp_instance.to_dict()
# create an instance of GetMarginIsolatedAccountV1Resp from a dict
get_margin_isolated_account_v1_resp_from_dict = GetMarginIsolatedAccountV1Resp.from_dict(get_margin_isolated_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


