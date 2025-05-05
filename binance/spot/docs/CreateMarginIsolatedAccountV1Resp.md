# CreateMarginIsolatedAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_margin_isolated_account_v1_resp import CreateMarginIsolatedAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMarginIsolatedAccountV1Resp from a JSON string
create_margin_isolated_account_v1_resp_instance = CreateMarginIsolatedAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateMarginIsolatedAccountV1Resp.to_json())

# convert the object into a dict
create_margin_isolated_account_v1_resp_dict = create_margin_isolated_account_v1_resp_instance.to_dict()
# create an instance of CreateMarginIsolatedAccountV1Resp from a dict
create_margin_isolated_account_v1_resp_from_dict = CreateMarginIsolatedAccountV1Resp.from_dict(create_margin_isolated_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


