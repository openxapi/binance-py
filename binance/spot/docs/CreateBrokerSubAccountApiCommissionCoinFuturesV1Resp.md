# CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_adjustment** | **int** |  | [optional] 
**maker_commission** | **int** |  | [optional] 
**pair** | **str** |  | [optional] 
**sub_account_id** | **int** |  | [optional] 
**taker_adjustment** | **int** |  | [optional] 
**taker_commission** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_broker_sub_account_api_commission_coin_futures_v1_resp import CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp from a JSON string
create_broker_sub_account_api_commission_coin_futures_v1_resp_instance = CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp.to_json())

# convert the object into a dict
create_broker_sub_account_api_commission_coin_futures_v1_resp_dict = create_broker_sub_account_api_commission_coin_futures_v1_resp_instance.to_dict()
# create an instance of CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp from a dict
create_broker_sub_account_api_commission_coin_futures_v1_resp_from_dict = CreateBrokerSubAccountApiCommissionCoinFuturesV1Resp.from_dict(create_broker_sub_account_api_commission_coin_futures_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


