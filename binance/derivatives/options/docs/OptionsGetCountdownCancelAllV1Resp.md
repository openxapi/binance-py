# OptionsGetCountdownCancelAllV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countdown_time** | **int** |  | [optional] 
**underlying** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.options.models.options_get_countdown_cancel_all_v1_resp import OptionsGetCountdownCancelAllV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsGetCountdownCancelAllV1Resp from a JSON string
options_get_countdown_cancel_all_v1_resp_instance = OptionsGetCountdownCancelAllV1Resp.from_json(json)
# print the JSON string representation of the object
print(OptionsGetCountdownCancelAllV1Resp.to_json())

# convert the object into a dict
options_get_countdown_cancel_all_v1_resp_dict = options_get_countdown_cancel_all_v1_resp_instance.to_dict()
# create an instance of OptionsGetCountdownCancelAllV1Resp from a dict
options_get_countdown_cancel_all_v1_resp_from_dict = OptionsGetCountdownCancelAllV1Resp.from_dict(options_get_countdown_cancel_all_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


