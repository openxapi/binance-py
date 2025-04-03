# PmarginGetCmAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[PmarginGetCmAccountV1RespAssetsInner]**](PmarginGetCmAccountV1RespAssetsInner.md) |  | [optional] 
**positions** | [**List[PmarginGetCmAccountV1RespPositionsInner]**](PmarginGetCmAccountV1RespPositionsInner.md) |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_cm_account_v1_resp import PmarginGetCmAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetCmAccountV1Resp from a JSON string
pmargin_get_cm_account_v1_resp_instance = PmarginGetCmAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetCmAccountV1Resp.to_json())

# convert the object into a dict
pmargin_get_cm_account_v1_resp_dict = pmargin_get_cm_account_v1_resp_instance.to_dict()
# create an instance of PmarginGetCmAccountV1Resp from a dict
pmargin_get_cm_account_v1_resp_from_dict = PmarginGetCmAccountV1Resp.from_dict(pmargin_get_cm_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


