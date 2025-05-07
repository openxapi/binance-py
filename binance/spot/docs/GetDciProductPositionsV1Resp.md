# GetDciProductPositionsV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[GetDciProductPositionsV1RespListInner]**](GetDciProductPositionsV1RespListInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_dci_product_positions_v1_resp import GetDciProductPositionsV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetDciProductPositionsV1Resp from a JSON string
get_dci_product_positions_v1_resp_instance = GetDciProductPositionsV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetDciProductPositionsV1Resp.to_json())

# convert the object into a dict
get_dci_product_positions_v1_resp_dict = get_dci_product_positions_v1_resp_instance.to_dict()
# create an instance of GetDciProductPositionsV1Resp from a dict
get_dci_product_positions_v1_resp_from_dict = GetDciProductPositionsV1Resp.from_dict(get_dci_product_positions_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


