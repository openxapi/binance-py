# WalletGetAssetAssetDividendV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[WalletGetAssetAssetDividendV1RespRowsInner]**](WalletGetAssetAssetDividendV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_asset_asset_dividend_v1_resp import WalletGetAssetAssetDividendV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAssetAssetDividendV1Resp from a JSON string
wallet_get_asset_asset_dividend_v1_resp_instance = WalletGetAssetAssetDividendV1Resp.from_json(json)
# print the JSON string representation of the object
print(WalletGetAssetAssetDividendV1Resp.to_json())

# convert the object into a dict
wallet_get_asset_asset_dividend_v1_resp_dict = wallet_get_asset_asset_dividend_v1_resp_instance.to_dict()
# create an instance of WalletGetAssetAssetDividendV1Resp from a dict
wallet_get_asset_asset_dividend_v1_resp_from_dict = WalletGetAssetAssetDividendV1Resp.from_dict(wallet_get_asset_asset_dividend_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


