# GetDciProductListV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[GetDciProductListV1RespListInner]**](GetDciProductListV1RespListInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_dci_product_list_v1_resp import GetDciProductListV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetDciProductListV1Resp from a JSON string
get_dci_product_list_v1_resp_instance = GetDciProductListV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetDciProductListV1Resp.to_json())

# convert the object into a dict
get_dci_product_list_v1_resp_dict = get_dci_product_list_v1_resp_instance.to_dict()
# create an instance of GetDciProductListV1Resp from a dict
get_dci_product_list_v1_resp_from_dict = GetDciProductListV1Resp.from_dict(get_dci_product_list_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


