# GetMiningHashTransferProfitDetailsV1RespData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** |  | [optional] 
**profit_transfer_details** | [**List[GetMiningHashTransferProfitDetailsV1RespDataProfitTransferDetailsInner]**](GetMiningHashTransferProfitDetailsV1RespDataProfitTransferDetailsInner.md) |  | [optional] 
**total_num** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_mining_hash_transfer_profit_details_v1_resp_data import GetMiningHashTransferProfitDetailsV1RespData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiningHashTransferProfitDetailsV1RespData from a JSON string
get_mining_hash_transfer_profit_details_v1_resp_data_instance = GetMiningHashTransferProfitDetailsV1RespData.from_json(json)
# print the JSON string representation of the object
print(GetMiningHashTransferProfitDetailsV1RespData.to_json())

# convert the object into a dict
get_mining_hash_transfer_profit_details_v1_resp_data_dict = get_mining_hash_transfer_profit_details_v1_resp_data_instance.to_dict()
# create an instance of GetMiningHashTransferProfitDetailsV1RespData from a dict
get_mining_hash_transfer_profit_details_v1_resp_data_from_dict = GetMiningHashTransferProfitDetailsV1RespData.from_dict(get_mining_hash_transfer_profit_details_v1_resp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


