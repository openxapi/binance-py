# MarginGetMarginIsolatedAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[MarginGetMarginIsolatedAccountV1RespAssetsInner]**](MarginGetMarginIsolatedAccountV1RespAssetsInner.md) |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 
**total_liability_of_btc** | **str** |  | [optional] 
**total_net_asset_of_btc** | **str** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_isolated_account_v1_resp import MarginGetMarginIsolatedAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginIsolatedAccountV1Resp from a JSON string
margin_get_margin_isolated_account_v1_resp_instance = MarginGetMarginIsolatedAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginIsolatedAccountV1Resp.to_json())

# convert the object into a dict
margin_get_margin_isolated_account_v1_resp_dict = margin_get_margin_isolated_account_v1_resp_instance.to_dict()
# create an instance of MarginGetMarginIsolatedAccountV1Resp from a dict
margin_get_margin_isolated_account_v1_resp_from_dict = MarginGetMarginIsolatedAccountV1Resp.from_dict(margin_get_margin_isolated_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


