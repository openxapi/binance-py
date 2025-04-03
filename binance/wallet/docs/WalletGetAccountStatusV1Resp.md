# WalletGetAccountStatusV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 

## Example

```python
from binance.wallet.models.wallet_get_account_status_v1_resp import WalletGetAccountStatusV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of WalletGetAccountStatusV1Resp from a JSON string
wallet_get_account_status_v1_resp_instance = WalletGetAccountStatusV1Resp.from_json(json)
# print the JSON string representation of the object
print(WalletGetAccountStatusV1Resp.to_json())

# convert the object into a dict
wallet_get_account_status_v1_resp_dict = wallet_get_account_status_v1_resp_instance.to_dict()
# create an instance of WalletGetAccountStatusV1Resp from a dict
wallet_get_account_status_v1_resp_from_dict = WalletGetAccountStatusV1Resp.from_dict(wallet_get_account_status_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


