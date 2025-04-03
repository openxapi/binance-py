# MarginGetMarginBorrowRepayV1RespRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset** | **str** |  | [optional] 
**interest** | **str** |  | [optional] 
**isolated_symbol** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**tx_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from binance.margin.models.margin_get_margin_borrow_repay_v1_resp_rows_inner import MarginGetMarginBorrowRepayV1RespRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarginGetMarginBorrowRepayV1RespRowsInner from a JSON string
margin_get_margin_borrow_repay_v1_resp_rows_inner_instance = MarginGetMarginBorrowRepayV1RespRowsInner.from_json(json)
# print the JSON string representation of the object
print(MarginGetMarginBorrowRepayV1RespRowsInner.to_json())

# convert the object into a dict
margin_get_margin_borrow_repay_v1_resp_rows_inner_dict = margin_get_margin_borrow_repay_v1_resp_rows_inner_instance.to_dict()
# create an instance of MarginGetMarginBorrowRepayV1RespRowsInner from a dict
margin_get_margin_borrow_repay_v1_resp_rows_inner_from_dict = MarginGetMarginBorrowRepayV1RespRowsInner.from_dict(margin_get_margin_borrow_repay_v1_resp_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


