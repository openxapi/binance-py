# GetCountdownCancelAllV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countdown_time** | **int** |  | [optional] 
**underlying** | **str** |  | [optional] 

## Example

```python
from binance.options.models.get_countdown_cancel_all_v1_resp import GetCountdownCancelAllV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetCountdownCancelAllV1Resp from a JSON string
get_countdown_cancel_all_v1_resp_instance = GetCountdownCancelAllV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetCountdownCancelAllV1Resp.to_json())

# convert the object into a dict
get_countdown_cancel_all_v1_resp_dict = get_countdown_cancel_all_v1_resp_instance.to_dict()
# create an instance of GetCountdownCancelAllV1Resp from a dict
get_countdown_cancel_all_v1_resp_from_dict = GetCountdownCancelAllV1Resp.from_dict(get_countdown_cancel_all_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


