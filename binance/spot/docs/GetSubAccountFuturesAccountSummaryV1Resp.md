# GetSubAccountFuturesAccountSummaryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** |  | [optional] 
**sub_account_list** | [**List[GetSubAccountFuturesAccountSummaryV1RespSubAccountListInner]**](GetSubAccountFuturesAccountSummaryV1RespSubAccountListInner.md) |  | [optional] 
**total_initial_margin** | **str** |  | [optional] 
**total_maintenance_margin** | **str** |  | [optional] 
**total_margin_balance** | **str** |  | [optional] 
**total_open_order_initial_margin** | **str** |  | [optional] 
**total_position_initial_margin** | **str** |  | [optional] 
**total_unrealized_profit** | **str** |  | [optional] 
**total_wallet_balance** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_futures_account_summary_v1_resp import GetSubAccountFuturesAccountSummaryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountFuturesAccountSummaryV1Resp from a JSON string
get_sub_account_futures_account_summary_v1_resp_instance = GetSubAccountFuturesAccountSummaryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountFuturesAccountSummaryV1Resp.to_json())

# convert the object into a dict
get_sub_account_futures_account_summary_v1_resp_dict = get_sub_account_futures_account_summary_v1_resp_instance.to_dict()
# create an instance of GetSubAccountFuturesAccountSummaryV1Resp from a dict
get_sub_account_futures_account_summary_v1_resp_from_dict = GetSubAccountFuturesAccountSummaryV1Resp.from_dict(get_sub_account_futures_account_summary_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


