# UmfuturesGetAssetIndexV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_buffer** | **str** |  | [optional] 
**ask_rate** | **str** |  | [optional] 
**auto_exchange_ask_buffer** | **str** |  | [optional] 
**auto_exchange_ask_rate** | **str** |  | [optional] 
**auto_exchange_bid_buffer** | **str** |  | [optional] 
**auto_exchange_bid_rate** | **str** |  | [optional] 
**bid_buffer** | **str** |  | [optional] 
**bid_rate** | **str** |  | [optional] 
**index** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**time** | **int** |  | [optional] 

## Example

```python
from binance.umfutures.models.umfutures_get_asset_index_v1_resp import UmfuturesGetAssetIndexV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetAssetIndexV1Resp from a JSON string
umfutures_get_asset_index_v1_resp_instance = UmfuturesGetAssetIndexV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetAssetIndexV1Resp.to_json())

# convert the object into a dict
umfutures_get_asset_index_v1_resp_dict = umfutures_get_asset_index_v1_resp_instance.to_dict()
# create an instance of UmfuturesGetAssetIndexV1Resp from a dict
umfutures_get_asset_index_v1_resp_from_dict = UmfuturesGetAssetIndexV1Resp.from_dict(umfutures_get_asset_index_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


