# GetMiningHashTransferProfitDetailsV1RespDataProfitTransferDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algo_name** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**coin_name** | **str** |  | [optional] 
**day** | **int** |  | [optional] 
**hash_rate** | **int** |  | [optional] 
**pool_username** | **str** |  | [optional] 
**to_pool_username** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_hash_transfer_profit_details_v1_resp_data_profit_transfer_details_inner import GetMiningHashTransferProfitDetailsV1RespDataProfitTransferDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningHashTransferProfitDetailsV1RespDataProfitTransferDetailsInner from a JSON string
get_mining_hash_transfer_profit_details_v1_resp_data_profit_transfer_details_inner_instance = GetMiningHashTransferProfitDetailsV1RespDataProfitTransferDetailsInner.from_json(json)
# print the JSON string representation of the object
print(GetMiningHashTransferProfitDetailsV1RespDataProfitTransferDetailsInner.to_json())

# convert the object into a dict
get_mining_hash_transfer_profit_details_v1_resp_data_profit_transfer_details_inner_dict = get_mining_hash_transfer_profit_details_v1_resp_data_profit_transfer_details_inner_instance.to_dict()
# create an instance of GetMiningHashTransferProfitDetailsV1RespDataProfitTransferDetailsInner from a dict
get_mining_hash_transfer_profit_details_v1_resp_data_profit_transfer_details_inner_from_dict = GetMiningHashTransferProfitDetailsV1RespDataProfitTransferDetailsInner.from_dict(get_mining_hash_transfer_profit_details_v1_resp_data_profit_transfer_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


