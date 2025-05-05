# CreateBrokerSubAccountBnbBurnMarginInterestV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_bnb_burn** | **bool** |  | [optional] 
**sub_account_id** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_broker_sub_account_bnb_burn_margin_interest_v1_resp import CreateBrokerSubAccountBnbBurnMarginInterestV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBrokerSubAccountBnbBurnMarginInterestV1Resp from a JSON string
create_broker_sub_account_bnb_burn_margin_interest_v1_resp_instance = CreateBrokerSubAccountBnbBurnMarginInterestV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateBrokerSubAccountBnbBurnMarginInterestV1Resp.to_json())

# convert the object into a dict
create_broker_sub_account_bnb_burn_margin_interest_v1_resp_dict = create_broker_sub_account_bnb_burn_margin_interest_v1_resp_instance.to_dict()
# create an instance of CreateBrokerSubAccountBnbBurnMarginInterestV1Resp from a dict
create_broker_sub_account_bnb_burn_margin_interest_v1_resp_from_dict = CreateBrokerSubAccountBnbBurnMarginInterestV1Resp.from_dict(create_broker_sub_account_bnb_burn_margin_interest_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


