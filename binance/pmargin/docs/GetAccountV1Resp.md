# GetAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_equity** | **str** |  | [optional] 
**account_initial_margin** | **str** |  | [optional] 
**account_maint_margin** | **str** |  | [optional] 
**account_status** | **str** |  | [optional] 
**actual_equity** | **str** |  | [optional] 
**total_available_balance** | **str** |  | [optional] 
**total_margin_open_loss** | **str** |  | [optional] 
**uni_mmr** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**virtual_max_withdraw_amount** | **str** |  | [optional] 

## Example

```python
from binance.pmargin.models.get_account_v1_resp import GetAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountV1Resp from a JSON string
get_account_v1_resp_instance = GetAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAccountV1Resp.to_json())

# convert the object into a dict
get_account_v1_resp_dict = get_account_v1_resp_instance.to_dict()
# create an instance of GetAccountV1Resp from a dict
get_account_v1_resp_from_dict = GetAccountV1Resp.from_dict(get_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


