# GetBrokerSubAccountDepositHistV2RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**address_tag** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**coin** | **str** |  | [optional] 
**confirm_times** | **str** |  | [optional] 
**deposit_id** | **int** |  | [optional] 
**insert_time** | **int** |  | [optional] 
**network** | **str** |  | [optional] 
**self_return_status** | **int** |  | [optional] 
**status** | **int** |  | [optional] 
**sub_account_id** | **str** |  | [optional] 
**transfer_type** | **int** |  | [optional] 
**travel_rule_status** | **int** |  | [optional] 
**tx_id** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_sub_account_deposit_hist_v2_resp_item import GetBrokerSubAccountDepositHistV2RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerSubAccountDepositHistV2RespItem from a JSON string
get_broker_sub_account_deposit_hist_v2_resp_item_instance = GetBrokerSubAccountDepositHistV2RespItem.from_json(json)
# print the JSON string representation of the object
print(GetBrokerSubAccountDepositHistV2RespItem.to_json())

# convert the object into a dict
get_broker_sub_account_deposit_hist_v2_resp_item_dict = get_broker_sub_account_deposit_hist_v2_resp_item_instance.to_dict()
# create an instance of GetBrokerSubAccountDepositHistV2RespItem from a dict
get_broker_sub_account_deposit_hist_v2_resp_item_from_dict = GetBrokerSubAccountDepositHistV2RespItem.from_dict(get_broker_sub_account_deposit_hist_v2_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


