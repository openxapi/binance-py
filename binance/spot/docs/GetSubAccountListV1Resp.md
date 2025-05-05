# GetSubAccountListV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_accounts** | [**List[GetSubAccountListV1RespSubAccountsInner]**](GetSubAccountListV1RespSubAccountsInner.md) |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_list_v1_resp import GetSubAccountListV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountListV1Resp from a JSON string
get_sub_account_list_v1_resp_instance = GetSubAccountListV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountListV1Resp.to_json())

# convert the object into a dict
get_sub_account_list_v1_resp_dict = get_sub_account_list_v1_resp_instance.to_dict()
# create an instance of GetSubAccountListV1Resp from a dict
get_sub_account_list_v1_resp_from_dict = GetSubAccountListV1Resp.from_dict(get_sub_account_list_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


