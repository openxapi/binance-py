# SubaccountGetManagedSubaccountMarginAssetV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**margin_level** | **str** |  | [optional] 
**total_asset_of_btc** | **str** |  | [optional] 
**total_liability_of_btc** | **str** |  | [optional] 
**total_net_asset_of_btc** | **str** |  | [optional] 
**user_assets** | [**List[SubaccountGetManagedSubaccountMarginAssetV1RespUserAssetsInner]**](SubaccountGetManagedSubaccountMarginAssetV1RespUserAssetsInner.md) |  | [optional] 

## Example

```python
from binance.subaccount.models.subaccount_get_managed_subaccount_margin_asset_v1_resp import SubaccountGetManagedSubaccountMarginAssetV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountGetManagedSubaccountMarginAssetV1Resp from a JSON string
subaccount_get_managed_subaccount_margin_asset_v1_resp_instance = SubaccountGetManagedSubaccountMarginAssetV1Resp.from_json(json)
# print the JSON string representation of the object
print(SubaccountGetManagedSubaccountMarginAssetV1Resp.to_json())

# convert the object into a dict
subaccount_get_managed_subaccount_margin_asset_v1_resp_dict = subaccount_get_managed_subaccount_margin_asset_v1_resp_instance.to_dict()
# create an instance of SubaccountGetManagedSubaccountMarginAssetV1Resp from a dict
subaccount_get_managed_subaccount_margin_asset_v1_resp_from_dict = SubaccountGetManagedSubaccountMarginAssetV1Resp.from_dict(subaccount_get_managed_subaccount_margin_asset_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


