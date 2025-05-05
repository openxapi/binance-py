# GetSubAccountMarginAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**margin_level** | **str** |  | [optional] 
**margin_trade_coeff_vo** | [**GetSubAccountMarginAccountV1RespMarginTradeCoeffVo**](GetSubAccountMarginAccountV1RespMarginTradeCoeffVo.md) |  | [optional] 
**margin_user_asset_vo_list** | [**List[GetManagedSubaccountMarginAssetV1RespUserAssetsInner]**](GetManagedSubaccountMarginAssetV1RespUserAssetsInner.md) |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 
**total_liability_of_btc** | **str** |  | [optional] 
**total_net_asset_of_btc** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_margin_account_v1_resp import GetSubAccountMarginAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountMarginAccountV1Resp from a JSON string
get_sub_account_margin_account_v1_resp_instance = GetSubAccountMarginAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountMarginAccountV1Resp.to_json())

# convert the object into a dict
get_sub_account_margin_account_v1_resp_dict = get_sub_account_margin_account_v1_resp_instance.to_dict()
# create an instance of GetSubAccountMarginAccountV1Resp from a dict
get_sub_account_margin_account_v1_resp_from_dict = GetSubAccountMarginAccountV1Resp.from_dict(get_sub_account_margin_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


