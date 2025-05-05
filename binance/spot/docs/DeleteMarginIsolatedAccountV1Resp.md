# DeleteMarginIsolatedAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.delete_margin_isolated_account_v1_resp import DeleteMarginIsolatedAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMarginIsolatedAccountV1Resp from a JSON string
delete_margin_isolated_account_v1_resp_instance = DeleteMarginIsolatedAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(DeleteMarginIsolatedAccountV1Resp.to_json())

# convert the object into a dict
delete_margin_isolated_account_v1_resp_dict = delete_margin_isolated_account_v1_resp_instance.to_dict()
# create an instance of DeleteMarginIsolatedAccountV1Resp from a dict
delete_margin_isolated_account_v1_resp_from_dict = DeleteMarginIsolatedAccountV1Resp.from_dict(delete_margin_isolated_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


