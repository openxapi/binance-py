# GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_commission** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**sub_account_id** | **int** |  | [optional] 
**taker_commission** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_sub_account_api_commission_coin_futures_v1_resp_item import GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem from a JSON string
get_broker_sub_account_api_commission_coin_futures_v1_resp_item_instance = GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem.to_json())

# convert the object into a dict
get_broker_sub_account_api_commission_coin_futures_v1_resp_item_dict = get_broker_sub_account_api_commission_coin_futures_v1_resp_item_instance.to_dict()
# create an instance of GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem from a dict
get_broker_sub_account_api_commission_coin_futures_v1_resp_item_from_dict = GetBrokerSubAccountApiCommissionCoinFuturesV1RespItem.from_dict(get_broker_sub_account_api_commission_coin_futures_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


