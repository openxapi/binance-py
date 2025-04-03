# WalletGetSpotDelistScheduleV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delist_time** | **int** |  | [optional] 
**symbols** | **List[str]** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_spot_delist_schedule_v1_resp_item import WalletGetSpotDelistScheduleV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetSpotDelistScheduleV1RespItem from a JSON string
wallet_get_spot_delist_schedule_v1_resp_item_instance = WalletGetSpotDelistScheduleV1RespItem.from_json(json)
# print the JSON string representation of the object
print(WalletGetSpotDelistScheduleV1RespItem.to_json())

# convert the object into a dict
wallet_get_spot_delist_schedule_v1_resp_item_dict = wallet_get_spot_delist_schedule_v1_resp_item_instance.to_dict()
# create an instance of WalletGetSpotDelistScheduleV1RespItem from a dict
wallet_get_spot_delist_schedule_v1_resp_item_from_dict = WalletGetSpotDelistScheduleV1RespItem.from_dict(wallet_get_spot_delist_schedule_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


