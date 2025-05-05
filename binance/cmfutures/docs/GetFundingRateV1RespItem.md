# GetFundingRateV1RespItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funding_rate** | **str** |  | [optional] 
**funding_time** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from binance.cmfutures.models.get_funding_rate_v1_resp_item import GetFundingRateV1RespItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetFundingRateV1RespItem from a JSON string
get_funding_rate_v1_resp_item_instance = GetFundingRateV1RespItem.from_json(json)
# print the JSON string representation of the object
print(GetFundingRateV1RespItem.to_json())

# convert the object into a dict
get_funding_rate_v1_resp_item_dict = get_funding_rate_v1_resp_item_instance.to_dict()
# create an instance of GetFundingRateV1RespItem from a dict
get_funding_rate_v1_resp_item_from_dict = GetFundingRateV1RespItem.from_dict(get_funding_rate_v1_resp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


