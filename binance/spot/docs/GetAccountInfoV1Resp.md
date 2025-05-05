# GetAccountInfoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_future_enabled** | **bool** |  | [optional] 
**is_margin_enabled** | **bool** |  | [optional] 
**is_options_enabled** | **bool** |  | [optional] 
**is_portfolio_margin_retail_enabled** | **bool** |  | [optional] 
**vip_level** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_account_info_v1_resp import GetAccountInfoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountInfoV1Resp from a JSON string
get_account_info_v1_resp_instance = GetAccountInfoV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetAccountInfoV1Resp.to_json())

# convert the object into a dict
get_account_info_v1_resp_dict = get_account_info_v1_resp_instance.to_dict()
# create an instance of GetAccountInfoV1Resp from a dict
get_account_info_v1_resp_from_dict = GetAccountInfoV1Resp.from_dict(get_account_info_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


