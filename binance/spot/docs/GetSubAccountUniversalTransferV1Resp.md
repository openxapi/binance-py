# GetSubAccountUniversalTransferV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[GetSubAccountUniversalTransferV1RespResultInner]**](GetSubAccountUniversalTransferV1RespResultInner.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_universal_transfer_v1_resp import GetSubAccountUniversalTransferV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountUniversalTransferV1Resp from a JSON string
get_sub_account_universal_transfer_v1_resp_instance = GetSubAccountUniversalTransferV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountUniversalTransferV1Resp.to_json())

# convert the object into a dict
get_sub_account_universal_transfer_v1_resp_dict = get_sub_account_universal_transfer_v1_resp_instance.to_dict()
# create an instance of GetSubAccountUniversalTransferV1Resp from a dict
get_sub_account_universal_transfer_v1_resp_from_dict = GetSubAccountUniversalTransferV1Resp.from_dict(get_sub_account_universal_transfer_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


