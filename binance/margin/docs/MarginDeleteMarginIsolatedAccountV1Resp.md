# MarginDeleteMarginIsolatedAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.margin.models.margin_delete_margin_isolated_account_v1_resp import MarginDeleteMarginIsolatedAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginDeleteMarginIsolatedAccountV1Resp from a JSON string
margin_delete_margin_isolated_account_v1_resp_instance = MarginDeleteMarginIsolatedAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginDeleteMarginIsolatedAccountV1Resp.to_json())

# convert the object into a dict
margin_delete_margin_isolated_account_v1_resp_dict = margin_delete_margin_isolated_account_v1_resp_instance.to_dict()
# create an instance of MarginDeleteMarginIsolatedAccountV1Resp from a dict
margin_delete_margin_isolated_account_v1_resp_from_dict = MarginDeleteMarginIsolatedAccountV1Resp.from_dict(margin_delete_margin_isolated_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


