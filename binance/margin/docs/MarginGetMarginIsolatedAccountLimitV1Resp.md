# MarginGetMarginIsolatedAccountLimitV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_account** | **int** |  | [optional] 
**max_account** | **int** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_isolated_account_limit_v1_resp import MarginGetMarginIsolatedAccountLimitV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginIsolatedAccountLimitV1Resp from a JSON string
margin_get_margin_isolated_account_limit_v1_resp_instance = MarginGetMarginIsolatedAccountLimitV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginIsolatedAccountLimitV1Resp.to_json())

# convert the object into a dict
margin_get_margin_isolated_account_limit_v1_resp_dict = margin_get_margin_isolated_account_limit_v1_resp_instance.to_dict()
# create an instance of MarginGetMarginIsolatedAccountLimitV1Resp from a dict
margin_get_margin_isolated_account_limit_v1_resp_from_dict = MarginGetMarginIsolatedAccountLimitV1Resp.from_dict(margin_get_margin_isolated_account_limit_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


