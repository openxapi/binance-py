# GetAccountStatusV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_account_status_v1_resp import GetAccountStatusV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountStatusV1Resp from a JSON string
get_account_status_v1_resp_instance = GetAccountStatusV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAccountStatusV1Resp.to_json())

# convert the object into a dict
get_account_status_v1_resp_dict = get_account_status_v1_resp_instance.to_dict()
# create an instance of GetAccountStatusV1Resp from a dict
get_account_status_v1_resp_from_dict = GetAccountStatusV1Resp.from_dict(get_account_status_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


