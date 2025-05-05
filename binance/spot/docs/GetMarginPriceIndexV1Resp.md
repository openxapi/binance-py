# GetMarginPriceIndexV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calc_time** | **int** |  | [optional] 
**price** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.get_margin_price_index_v1_resp import GetMarginPriceIndexV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetMarginPriceIndexV1Resp from a JSON string
get_margin_price_index_v1_resp_instance = GetMarginPriceIndexV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetMarginPriceIndexV1Resp.to_json())

# convert the object into a dict
get_margin_price_index_v1_resp_dict = get_margin_price_index_v1_resp_instance.to_dict()
# create an instance of GetMarginPriceIndexV1Resp from a dict
get_margin_price_index_v1_resp_from_dict = GetMarginPriceIndexV1Resp.from_dict(get_margin_price_index_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


