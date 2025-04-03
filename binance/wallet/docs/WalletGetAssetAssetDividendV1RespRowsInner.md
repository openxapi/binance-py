# WalletGetAssetAssetDividendV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**div_time** | **int** |  | [optional] 
**en_info** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**tran_id** | **int** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_asset_asset_dividend_v1_resp_rows_inner import WalletGetAssetAssetDividendV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAssetAssetDividendV1RespRowsInner from a JSON string
wallet_get_asset_asset_dividend_v1_resp_rows_inner_instance = WalletGetAssetAssetDividendV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(WalletGetAssetAssetDividendV1RespRowsInner.to_json())

# convert the object into a dict
wallet_get_asset_asset_dividend_v1_resp_rows_inner_dict = wallet_get_asset_asset_dividend_v1_resp_rows_inner_instance.to_dict()
# create an instance of WalletGetAssetAssetDividendV1RespRowsInner from a dict
wallet_get_asset_asset_dividend_v1_resp_rows_inner_from_dict = WalletGetAssetAssetDividendV1RespRowsInner.from_dict(wallet_get_asset_asset_dividend_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


