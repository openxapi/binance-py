# SpotCreateOrderCancelReplaceV3Data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_response** | [**SpotCreateOrderCancelReplaceV3DataCancelResponse**](SpotCreateOrderCancelReplaceV3DataCancelResponse.md) |  | [optional] 
**cancel_result** | **str** |  | [optional] 
**new_order_response** | [**SpotCreateOrderCancelReplaceV3DataNewOrderResponse**](SpotCreateOrderCancelReplaceV3DataNewOrderResponse.md) |  | [optional] 
**new_order_result** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.spot_create_order_cancel_replace_v3_data import SpotCreateOrderCancelReplaceV3Data

# TODO update the JSON string below
json = "{}"
# create an instance of SpotCreateOrderCancelReplaceV3Data from a JSON string
spot_create_order_cancel_replace_v3_data_instance = SpotCreateOrderCancelReplaceV3Data.from_json(json)
# print the JSON string representation of the object
print(SpotCreateOrderCancelReplaceV3Data.to_json())

# convert the object into a dict
spot_create_order_cancel_replace_v3_data_dict = spot_create_order_cancel_replace_v3_data_instance.to_dict()
# create an instance of SpotCreateOrderCancelReplaceV3Data from a dict
spot_create_order_cancel_replace_v3_data_from_dict = SpotCreateOrderCancelReplaceV3Data.from_dict(spot_create_order_cancel_replace_v3_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


