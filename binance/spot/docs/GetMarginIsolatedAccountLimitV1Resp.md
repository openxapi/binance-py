# GetMarginIsolatedAccountLimitV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_account** | **int** |  | [optional] 
**max_account** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_isolated_account_limit_v1_resp import GetMarginIsolatedAccountLimitV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginIsolatedAccountLimitV1Resp from a JSON string
get_margin_isolated_account_limit_v1_resp_instance = GetMarginIsolatedAccountLimitV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMarginIsolatedAccountLimitV1Resp.to_json())

# convert the object into a dict
get_margin_isolated_account_limit_v1_resp_dict = get_margin_isolated_account_limit_v1_resp_instance.to_dict()
# create an instance of GetMarginIsolatedAccountLimitV1Resp from a dict
get_margin_isolated_account_limit_v1_resp_from_dict = GetMarginIsolatedAccountLimitV1Resp.from_dict(get_margin_isolated_account_limit_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


