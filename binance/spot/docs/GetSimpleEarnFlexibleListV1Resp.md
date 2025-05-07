# GetSimpleEarnFlexibleListV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[GetSimpleEarnFlexibleListV1RespRowsInner]**](GetSimpleEarnFlexibleListV1RespRowsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_simple_earn_flexible_list_v1_resp import GetSimpleEarnFlexibleListV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSimpleEarnFlexibleListV1Resp from a JSON string
get_simple_earn_flexible_list_v1_resp_instance = GetSimpleEarnFlexibleListV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSimpleEarnFlexibleListV1Resp.to_json())

# convert the object into a dict
get_simple_earn_flexible_list_v1_resp_dict = get_simple_earn_flexible_list_v1_resp_instance.to_dict()
# create an instance of GetSimpleEarnFlexibleListV1Resp from a dict
get_simple_earn_flexible_list_v1_resp_from_dict = GetSimpleEarnFlexibleListV1Resp.from_dict(get_simple_earn_flexible_list_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


