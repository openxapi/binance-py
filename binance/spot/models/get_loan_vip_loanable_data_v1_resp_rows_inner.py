# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetLoanVipLoanableDataV1RespRowsInner(BaseModel):
    """
    GetLoanVipLoanableDataV1RespRowsInner
    """ # noqa: E501
    var_30d_daily_interest_rate: Optional[StrictStr] = Field(default=None, alias="_30dDailyInterestRate")
    var_30d_yearly_interest_rate: Optional[StrictStr] = Field(default=None, alias="_30dYearlyInterestRate")
    var_60d_daily_interest_rate: Optional[StrictStr] = Field(default=None, alias="_60dDailyInterestRate")
    var_60d_yearly_interest_rate: Optional[StrictStr] = Field(default=None, alias="_60dYearlyInterestRate")
    flexible_daily_interest_rate: Optional[StrictStr] = Field(default=None, alias="_flexibleDailyInterestRate")
    flexible_yearly_interest_rate: Optional[StrictStr] = Field(default=None, alias="_flexibleYearlyInterestRate")
    loan_coin: Optional[StrictStr] = Field(default=None, alias="loanCoin")
    max_limit: Optional[StrictStr] = Field(default=None, alias="maxLimit")
    min_limit: Optional[StrictStr] = Field(default=None, alias="minLimit")
    vip_level: Optional[StrictInt] = Field(default=None, alias="vipLevel")
    __properties: ClassVar[List[str]] = ["_30dDailyInterestRate", "_30dYearlyInterestRate", "_60dDailyInterestRate", "_60dYearlyInterestRate", "_flexibleDailyInterestRate", "_flexibleYearlyInterestRate", "loanCoin", "maxLimit", "minLimit", "vipLevel"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetLoanVipLoanableDataV1RespRowsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLoanVipLoanableDataV1RespRowsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_30dDailyInterestRate": obj.get("_30dDailyInterestRate"),
            "_30dYearlyInterestRate": obj.get("_30dYearlyInterestRate"),
            "_60dDailyInterestRate": obj.get("_60dDailyInterestRate"),
            "_60dYearlyInterestRate": obj.get("_60dYearlyInterestRate"),
            "_flexibleDailyInterestRate": obj.get("_flexibleDailyInterestRate"),
            "_flexibleYearlyInterestRate": obj.get("_flexibleYearlyInterestRate"),
            "loanCoin": obj.get("loanCoin"),
            "maxLimit": obj.get("maxLimit"),
            "minLimit": obj.get("minLimit"),
            "vipLevel": obj.get("vipLevel")
        })
        return _obj


