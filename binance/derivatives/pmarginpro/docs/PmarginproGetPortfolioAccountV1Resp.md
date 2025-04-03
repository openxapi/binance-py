# PmarginproGetPortfolioAccountV1Resp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_equity** | **str** |  | [optional] 
**account_initial_margin** | **str** |  | [optional] 
**account_maint_margin** | **str** |  | [optional] 
**account_status** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**actual_equity** | **str** |  | [optional] 
**total_available_balance** | **str** |  | [optional] 
**uni_mmr** | **str** |  | [optional] 

## Example

```python
from binance.derivatives.pmarginpro.models.pmarginpro_get_portfolio_account_v1_resp import PmarginproGetPortfolioAccountV1Resp

# TODO update the JSON string below
json = "{}"
# create an instance of PmarginproGetPortfolioAccountV1Resp from a JSON string
pmarginpro_get_portfolio_account_v1_resp_instance = PmarginproGetPortfolioAccountV1Resp.from_json(json)
# print the JSON string representation of the object
print(PmarginproGetPortfolioAccountV1Resp.to_json())

# convert the object into a dict
pmarginpro_get_portfolio_account_v1_resp_dict = pmarginpro_get_portfolio_account_v1_resp_instance.to_dict()
# create an instance of PmarginproGetPortfolioAccountV1Resp from a dict
pmarginpro_get_portfolio_account_v1_resp_from_dict = PmarginproGetPortfolioAccountV1Resp.from_dict(pmarginpro_get_portfolio_account_v1_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


