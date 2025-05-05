# GetManagedSubaccountMarginAssetV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**margin_level** | **str** |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 
**total_liability_of_btc** | **str** |  | [optional] 
**total_net_asset_of_btc** | **str** |  | [optional] 
**user_assets** | [**List[GetManagedSubaccountMarginAssetV1RespUserAssetsInner]**](GetManagedSubaccountMarginAssetV1RespUserAssetsInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_managed_subaccount_margin_asset_v1_resp import GetManagedSubaccountMarginAssetV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedSubaccountMarginAssetV1Resp from a JSON string
get_managed_subaccount_margin_asset_v1_resp_instance = GetManagedSubaccountMarginAssetV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetManagedSubaccountMarginAssetV1Resp.to_json())

# convert the object into a dict
get_managed_subaccount_margin_asset_v1_resp_dict = get_managed_subaccount_margin_asset_v1_resp_instance.to_dict()
# create an instance of GetManagedSubaccountMarginAssetV1Resp from a dict
get_managed_subaccount_margin_asset_v1_resp_from_dict = GetManagedSubaccountMarginAssetV1Resp.from_dict(get_managed_subaccount_margin_asset_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


