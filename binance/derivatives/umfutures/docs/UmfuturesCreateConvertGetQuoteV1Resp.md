# UmfuturesCreateConvertGetQuoteV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_amount** | **str** |  | [optional] 
**inverse_ratio** | **str** |  | [optional] 
**quote_id** | **str** |  | [optional] 
**ratio** | **str** |  | [optional] 
**to_amount** | **str** |  | [optional] 
**valid_timestamp** | **int** |  | [optional] 

## Example

```python
from binance.derivatives.umfutures.models.umfutures_create_convert_get_quote_v1_resp import UmfuturesCreateConvertGetQuoteV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of UmfuturesCreateConvertGetQuoteV1Resp from a JSON string
umfutures_create_convert_get_quote_v1_resp_instance = UmfuturesCreateConvertGetQuoteV1Resp.from_json(json)
# print the JSON string representation of the object
print(UmfuturesCreateConvertGetQuoteV1Resp.to_json())

# convert the object into a dict
umfutures_create_convert_get_quote_v1_resp_dict = umfutures_create_convert_get_quote_v1_resp_instance.to_dict()
# create an instance of UmfuturesCreateConvertGetQuoteV1Resp from a dict
umfutures_create_convert_get_quote_v1_resp_from_dict = UmfuturesCreateConvertGetQuoteV1Resp.from_dict(umfutures_create_convert_get_quote_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


