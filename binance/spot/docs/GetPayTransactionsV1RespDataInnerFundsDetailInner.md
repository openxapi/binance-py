# GetPayTransactionsV1RespDataInnerFundsDetailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**wallet_asset_cost** | [**List[GetPayTransactionsV1RespDataInnerFundsDetailInnerWalletAssetCostInner]**](GetPayTransactionsV1RespDataInnerFundsDetailInnerWalletAssetCostInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_pay_transactions_v1_resp_data_inner_funds_detail_inner import GetPayTransactionsV1RespDataInnerFundsDetailInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayTransactionsV1RespDataInnerFundsDetailInner from a JSON string
get_pay_transactions_v1_resp_data_inner_funds_detail_inner_instance = GetPayTransactionsV1RespDataInnerFundsDetailInner.from_json(json)
# print the JSON string representation of the object
print(GetPayTransactionsV1RespDataInnerFundsDetailInner.to_json())

# convert the object into a dict
get_pay_transactions_v1_resp_data_inner_funds_detail_inner_dict = get_pay_transactions_v1_resp_data_inner_funds_detail_inner_instance.to_dict()
# create an instance of GetPayTransactionsV1RespDataInnerFundsDetailInner from a dict
get_pay_transactions_v1_resp_data_inner_funds_detail_inner_from_dict = GetPayTransactionsV1RespDataInnerFundsDetailInner.from_dict(get_pay_transactions_v1_resp_data_inner_funds_detail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


