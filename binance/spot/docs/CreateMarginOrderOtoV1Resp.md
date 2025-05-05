# CreateMarginOrderOtoV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** |  | [optional] 
**is_isolated** | **bool** |  | [optional] 
**list_client_order_id** | **str** |  | [optional] 
**list_order_status** | **str** |  | [optional] 
**list_status_type** | **str** |  | [optional] 
**order_list_id** | **int** |  | [optional] 
**order_reports** | [**List[CreateMarginOrderOtoV1RespOrderReportsInner]**](CreateMarginOrderOtoV1RespOrderReportsInner.md) |  | [optional] 
**orders** | [**List[CreateMarginOrderOcoV1RespOrdersInner]**](CreateMarginOrderOcoV1RespOrdersInner.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**transaction_time** | **int** |  | [optional] 

## Example

```python
from binance.spot.models.create_margin_order_oto_v1_resp import CreateMarginOrderOtoV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMarginOrderOtoV1Resp from a JSON string
create_margin_order_oto_v1_resp_instance = CreateMarginOrderOtoV1Resp.from_json(json)
# print the JSON string representation of the object
print(CreateMarginOrderOtoV1Resp.to_json())

# convert the object into a dict
create_margin_order_oto_v1_resp_dict = create_margin_order_oto_v1_resp_instance.to_dict()
# create an instance of CreateMarginOrderOtoV1Resp from a dict
create_margin_order_oto_v1_resp_from_dict = CreateMarginOrderOtoV1Resp.from_dict(create_margin_order_oto_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


