# GetAssetLedgerTransferCloudMiningQueryByPageV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner]**](GetAssetLedgerTransferCloudMiningQueryByPageV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_asset_ledger_transfer_cloud_mining_query_by_page_v1_resp import GetAssetLedgerTransferCloudMiningQueryByPageV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetLedgerTransferCloudMiningQueryByPageV1Resp from a JSON string
get_asset_ledger_transfer_cloud_mining_query_by_page_v1_resp_instance = GetAssetLedgerTransferCloudMiningQueryByPageV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAssetLedgerTransferCloudMiningQueryByPageV1Resp.to_json())

# convert the object into a dict
get_asset_ledger_transfer_cloud_mining_query_by_page_v1_resp_dict = get_asset_ledger_transfer_cloud_mining_query_by_page_v1_resp_instance.to_dict()
# create an instance of GetAssetLedgerTransferCloudMiningQueryByPageV1Resp from a dict
get_asset_ledger_transfer_cloud_mining_query_by_page_v1_resp_from_dict = GetAssetLedgerTransferCloudMiningQueryByPageV1Resp.from_dict(get_asset_ledger_transfer_cloud_mining_query_by_page_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


