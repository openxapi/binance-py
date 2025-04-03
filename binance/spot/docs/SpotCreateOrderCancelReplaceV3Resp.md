# SpotCreateOrderCancelReplaceV3Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | [**SpotCreateOrderCancelReplaceV3Data**](SpotCreateOrderCancelReplaceV3Data.md) |  | [optional] 
**msg** | **str** |  | [optional] 
**cancel_response** | [**SpotCreateOrderCancelReplaceV3DataCancelResponse**](SpotCreateOrderCancelReplaceV3DataCancelResponse.md) |  | [optional] 
**cancel_result** | **str** |  | [optional] 
**new_order_response** | [**SpotCreateOrderCancelReplaceV3DataNewOrderResponse**](SpotCreateOrderCancelReplaceV3DataNewOrderResponse.md) |  | [optional] 
**new_order_result** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_cancel_replace_v3_resp import SpotCreateOrderCancelReplaceV3Resp

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderCancelReplaceV3Resp from a JSON string
spot_create_order_cancel_replace_v3_resp_instance = SpotCreateOrderCancelReplaceV3Resp.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderCancelReplaceV3Resp.to_json())

# convert the object into a dict
spot_create_order_cancel_replace_v3_resp_dict = spot_create_order_cancel_replace_v3_resp_instance.to_dict()
# create an instance of SpotCreateOrderCancelReplaceV3Resp from a dict
spot_create_order_cancel_replace_v3_resp_from_dict = SpotCreateOrderCancelReplaceV3Resp.from_dict(spot_create_order_cancel_replace_v3_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


