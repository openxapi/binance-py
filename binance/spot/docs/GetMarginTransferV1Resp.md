# GetMarginTransferV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetMarginTransferV1RespRowsInner]**](GetMarginTransferV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_transfer_v1_resp import GetMarginTransferV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginTransferV1Resp from a JSON string
get_margin_transfer_v1_resp_instance = GetMarginTransferV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMarginTransferV1Resp.to_json())

# convert the object into a dict
get_margin_transfer_v1_resp_dict = get_margin_transfer_v1_resp_instance.to_dict()
# create an instance of GetMarginTransferV1Resp from a dict
get_margin_transfer_v1_resp_from_dict = GetMarginTransferV1Resp.from_dict(get_margin_transfer_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


