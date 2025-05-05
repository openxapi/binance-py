# GetSubAccountSpotSummaryV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master_account_total_asset** | **str** |  | [optional] 
**spot_sub_user_asset_btc_vo_list** | [**List[GetSubAccountSpotSummaryV1RespSpotSubUserAssetBtcVoListInner]**](GetSubAccountSpotSummaryV1RespSpotSubUserAssetBtcVoListInner.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.get_sub_account_spot_summary_v1_resp import GetSubAccountSpotSummaryV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubAccountSpotSummaryV1Resp from a JSON string
get_sub_account_spot_summary_v1_resp_instance = GetSubAccountSpotSummaryV1Resp.from_json(json)
# print the JSON string representation of the object
print(GetSubAccountSpotSummaryV1Resp.to_json())

# convert the object into a dict
get_sub_account_spot_summary_v1_resp_dict = get_sub_account_spot_summary_v1_resp_instance.to_dict()
# create an instance of GetSubAccountSpotSummaryV1Resp from a dict
get_sub_account_spot_summary_v1_resp_from_dict = GetSubAccountSpotSummaryV1Resp.from_dict(get_sub_account_spot_summary_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


