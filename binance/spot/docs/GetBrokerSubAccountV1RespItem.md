# GetBrokerSubAccountV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**maker_commission** | **float** |  | [optional] 
**margin_maker_commission** | **int** |  | [optional] 
**margin_taker_commission** | **int** |  | [optional] 
**subaccount_id** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**taker_commission** | **float** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_sub_account_v1_resp_item import GetBrokerSubAccountV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerSubAccountV1RespItem from a JSON string
get_broker_sub_account_v1_resp_item_instance = GetBrokerSubAccountV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetBrokerSubAccountV1RespItem.to_json())

# convert the object into a dict
get_broker_sub_account_v1_resp_item_dict = get_broker_sub_account_v1_resp_item_instance.to_dict()
# create an instance of GetBrokerSubAccountV1RespItem from a dict
get_broker_sub_account_v1_resp_item_from_dict = GetBrokerSubAccountV1RespItem.from_dict(get_broker_sub_account_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


