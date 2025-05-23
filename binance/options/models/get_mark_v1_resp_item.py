# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetMarkV1RespItem(BaseModel):
    """
    GetMarkV1RespItem
    """ # noqa: E501
    ask_iv: Optional[StrictStr] = Field(default=None, alias="askIV")
    bid_iv: Optional[StrictStr] = Field(default=None, alias="bidIV")
    delta: Optional[StrictStr] = None
    gamma: Optional[StrictStr] = None
    high_price_limit: Optional[StrictStr] = Field(default=None, alias="highPriceLimit")
    low_price_limit: Optional[StrictStr] = Field(default=None, alias="lowPriceLimit")
    mark_iv: Optional[StrictStr] = Field(default=None, alias="markIV")
    mark_price: Optional[StrictStr] = Field(default=None, alias="markPrice")
    risk_free_interest: Optional[StrictStr] = Field(default=None, alias="riskFreeInterest")
    symbol: Optional[StrictStr] = None
    theta: Optional[StrictStr] = None
    vega: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["askIV", "bidIV", "delta", "gamma", "highPriceLimit", "lowPriceLimit", "markIV", "markPrice", "riskFreeInterest", "symbol", "theta", "vega"]

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
        """Create an instance of GetMarkV1RespItem from a JSON string"""
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
        """Create an instance of GetMarkV1RespItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "askIV": obj.get("askIV"),
            "bidIV": obj.get("bidIV"),
            "delta": obj.get("delta"),
            "gamma": obj.get("gamma"),
            "highPriceLimit": obj.get("highPriceLimit"),
            "lowPriceLimit": obj.get("lowPriceLimit"),
            "markIV": obj.get("markIV"),
            "markPrice": obj.get("markPrice"),
            "riskFreeInterest": obj.get("riskFreeInterest"),
            "symbol": obj.get("symbol"),
            "theta": obj.get("theta"),
            "vega": obj.get("vega")
        })
        return _obj


