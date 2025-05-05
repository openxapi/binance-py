# GetBrokerSubAccountBnbBurnStatusV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_bnb_burn** | **bool** |  | [optional] 
**spot_bnb_burn** | **bool** |  | [optional] 
**sub_account_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_broker_sub_account_bnb_burn_status_v1_resp import GetBrokerSubAccountBnbBurnStatusV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrokerSubAccountBnbBurnStatusV1Resp from a JSON string
get_broker_sub_account_bnb_burn_status_v1_resp_instance = GetBrokerSubAccountBnbBurnStatusV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetBrokerSubAccountBnbBurnStatusV1Resp.to_json())

# convert the object into a dict
get_broker_sub_account_bnb_burn_status_v1_resp_dict = get_broker_sub_account_bnb_burn_status_v1_resp_instance.to_dict()
# create an instance of GetBrokerSubAccountBnbBurnStatusV1Resp from a dict
get_broker_sub_account_bnb_burn_status_v1_resp_from_dict = GetBrokerSubAccountBnbBurnStatusV1Resp.from_dict(get_broker_sub_account_bnb_burn_status_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


