# CreateBrokerSubAccountApiCommissionV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_commission** | **float** |  | [optional] 
**margin_maker_commission** | **float** |  | [optional] 
**margin_taker_commission** | **float** |  | [optional] 
**sub_account_id** | **str** |  | [optional] 
**taker_commission** | **float** |  | [optional] 

## Example

```python
from binance.spot.models.create_broker_sub_account_api_commission_v1_resp import CreateBrokerSubAccountApiCommissionV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBrokerSubAccountApiCommissionV1Resp from a JSON string
create_broker_sub_account_api_commission_v1_resp_instance = CreateBrokerSubAccountApiCommissionV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateBrokerSubAccountApiCommissionV1Resp.to_json())

# convert the object into a dict
create_broker_sub_account_api_commission_v1_resp_dict = create_broker_sub_account_api_commission_v1_resp_instance.to_dict()
# create an instance of CreateBrokerSubAccountApiCommissionV1Resp from a dict
create_broker_sub_account_api_commission_v1_resp_from_dict = CreateBrokerSubAccountApiCommissionV1Resp.from_dict(create_broker_sub_account_api_commission_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


