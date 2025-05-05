# GetAssetAssetDividendV1RespRowsInner


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
from binance.spot.models.get_asset_asset_dividend_v1_resp_rows_inner import GetAssetAssetDividendV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetAssetDividendV1RespRowsInner from a JSON string
get_asset_asset_dividend_v1_resp_rows_inner_instance = GetAssetAssetDividendV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetAssetDividendV1RespRowsInner.to_json())

# convert the object into a dict
get_asset_asset_dividend_v1_resp_rows_inner_dict = get_asset_asset_dividend_v1_resp_rows_inner_instance.to_dict()
# create an instance of GetAssetAssetDividendV1RespRowsInner from a dict
get_asset_asset_dividend_v1_resp_rows_inner_from_dict = GetAssetAssetDividendV1RespRowsInner.from_dict(get_asset_asset_dividend_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


