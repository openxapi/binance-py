# UmfuturesGetAdlQuantileV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adl_quantile** | [**UmfuturesGetAdlQuantileV1RespItemAdlQuantile**](UmfuturesGetAdlQuantileV1RespItemAdlQuantile.md) |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_get_adl_quantile_v1_resp_item import UmfuturesGetAdlQuantileV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesGetAdlQuantileV1RespItem from a JSON string
umfutures_get_adl_quantile_v1_resp_item_instance = UmfuturesGetAdlQuantileV1RespItem.from_json(json)
# print the JSON string representation of the object
print(UmfuturesGetAdlQuantileV1RespItem.to_json())

# convert the object into a dict
umfutures_get_adl_quantile_v1_resp_item_dict = umfutures_get_adl_quantile_v1_resp_item_instance.to_dict()
# create an instance of UmfuturesGetAdlQuantileV1RespItem from a dict
umfutures_get_adl_quantile_v1_resp_item_from_dict = UmfuturesGetAdlQuantileV1RespItem.from_dict(umfutures_get_adl_quantile_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


