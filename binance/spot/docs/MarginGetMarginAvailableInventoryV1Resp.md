# MarginGetMarginAvailableInventoryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | **Dict[str, str]** |  | [optional] 
**update_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.margin_get_margin_available_inventory_v1_resp import MarginGetMarginAvailableInventoryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginAvailableInventoryV1Resp from a JSON string
margin_get_margin_available_inventory_v1_resp_instance = MarginGetMarginAvailableInventoryV1Resp.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginAvailableInventoryV1Resp.to_json())

# convert the object into a dict
margin_get_margin_available_inventory_v1_resp_dict = margin_get_margin_available_inventory_v1_resp_instance.to_dict()
# create an instance of MarginGetMarginAvailableInventoryV1Resp from a dict
margin_get_margin_available_inventory_v1_resp_from_dict = MarginGetMarginAvailableInventoryV1Resp.from_dict(margin_get_margin_available_inventory_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


