# GetBrokerUniversalTransferV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**client_tran_id** | **str** |  | [optional] 
**from_account_type** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**to_account_type** | **str** |  | [optional] 
**to_id** | **str** |  | [optional] 
**txn_id** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_universal_transfer_v1_resp_item import GetBrokerUniversalTransferV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerUniversalTransferV1RespItem from a JSON string
get_broker_universal_transfer_v1_resp_item_instance = GetBrokerUniversalTransferV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetBrokerUniversalTransferV1RespItem.to_json())

# convert the object into a dict
get_broker_universal_transfer_v1_resp_item_dict = get_broker_universal_transfer_v1_resp_item_instance.to_dict()
# create an instance of GetBrokerUniversalTransferV1RespItem from a dict
get_broker_universal_transfer_v1_resp_item_from_dict = GetBrokerUniversalTransferV1RespItem.from_dict(get_broker_universal_transfer_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


