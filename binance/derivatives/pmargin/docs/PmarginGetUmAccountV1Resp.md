# PmarginGetUmAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[PmarginGetCmAccountV1RespAssetsInner]**](PmarginGetCmAccountV1RespAssetsInner.md) |  | [optional] 
**positions** | [**List[PmarginGetUmAccountV1RespPositionsInner]**](PmarginGetUmAccountV1RespPositionsInner.md) |  | [optional] 

## Example

```python
from binance.derivatives.pmargin.models.pmargin_get_um_account_v1_resp import PmarginGetUmAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginGetUmAccountV1Resp from a JSON string
pmargin_get_um_account_v1_resp_instance = PmarginGetUmAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginGetUmAccountV1Resp.to_json())

# convert the object into a dict
pmargin_get_um_account_v1_resp_dict = pmargin_get_um_account_v1_resp_instance.to_dict()
# create an instance of PmarginGetUmAccountV1Resp from a dict
pmargin_get_um_account_v1_resp_from_dict = PmarginGetUmAccountV1Resp.from_dict(pmargin_get_um_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


