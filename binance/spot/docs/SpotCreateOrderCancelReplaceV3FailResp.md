# SpotCreateOrderCancelReplaceV3FailResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | [**SpotCreateOrderCancelReplaceV3Data**](SpotCreateOrderCancelReplaceV3Data.md) |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_cancel_replace_v3_fail_resp import SpotCreateOrderCancelReplaceV3FailResp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderCancelReplaceV3FailResp from a JSON string
spot_create_order_cancel_replace_v3_fail_resp_instance = SpotCreateOrderCancelReplaceV3FailResp.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderCancelReplaceV3FailResp.to_json())

# convert the object into a dict
spot_create_order_cancel_replace_v3_fail_resp_dict = spot_create_order_cancel_replace_v3_fail_resp_instance.to_dict()
# create an instance of SpotCreateOrderCancelReplaceV3FailResp from a dict
spot_create_order_cancel_replace_v3_fail_resp_from_dict = SpotCreateOrderCancelReplaceV3FailResp.from_dict(spot_create_order_cancel_replace_v3_fail_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


