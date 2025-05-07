# GetDciProductAccountsV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount_in_btc** | **str** |  | [optional] 
**total_amount_in_usdt** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_dci_product_accounts_v1_resp import GetDciProductAccountsV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetDciProductAccountsV1Resp from a JSON string
get_dci_product_accounts_v1_resp_instance = GetDciProductAccountsV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetDciProductAccountsV1Resp.to_json())

# convert the object into a dict
get_dci_product_accounts_v1_resp_dict = get_dci_product_accounts_v1_resp_instance.to_dict()
# create an instance of GetDciProductAccountsV1Resp from a dict
get_dci_product_accounts_v1_resp_from_dict = GetDciProductAccountsV1Resp.from_dict(get_dci_product_accounts_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


