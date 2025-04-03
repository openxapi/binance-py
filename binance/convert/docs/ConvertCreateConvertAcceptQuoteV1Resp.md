# ConvertCreateConvertAcceptQuoteV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** |  | [optional] 
**order_id** | **str** |  | [optional] 
**order_status** | **str** |  | [optional] 

## Example

```python
from binance.convert.models.convert_create_convert_accept_quote_v1_resp import ConvertCreateConvertAcceptQuoteV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertCreateConvertAcceptQuoteV1Resp from a JSON string
convert_create_convert_accept_quote_v1_resp_instance = ConvertCreateConvertAcceptQuoteV1Resp.from_json(json)
# print the JSON string representation of the object
print(ConvertCreateConvertAcceptQuoteV1Resp.to_json())

# convert the object into a dict
convert_create_convert_accept_quote_v1_resp_dict = convert_create_convert_accept_quote_v1_resp_instance.to_dict()
# create an instance of ConvertCreateConvertAcceptQuoteV1Resp from a dict
convert_create_convert_accept_quote_v1_resp_from_dict = ConvertCreateConvertAcceptQuoteV1Resp.from_dict(convert_create_convert_accept_quote_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


