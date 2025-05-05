# CreateConvertAcceptQuoteV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** |  | [optional] 
**order_id** | **str** |  | [optional] 
**order_status** | **str** |  | [optional] 

## Example

```python
from binance.spot.models.create_convert_accept_quote_v1_resp import CreateConvertAcceptQuoteV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConvertAcceptQuoteV1Resp from a JSON string
create_convert_accept_quote_v1_resp_instance = CreateConvertAcceptQuoteV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateConvertAcceptQuoteV1Resp.to_json())

# convert the object into a dict
create_convert_accept_quote_v1_resp_dict = create_convert_accept_quote_v1_resp_instance.to_dict()
# create an instance of CreateConvertAcceptQuoteV1Resp from a dict
create_convert_accept_quote_v1_resp_from_dict = CreateConvertAcceptQuoteV1Resp.from_dict(create_convert_accept_quote_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


