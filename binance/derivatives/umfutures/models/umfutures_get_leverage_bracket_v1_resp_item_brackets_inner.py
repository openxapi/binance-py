# coding: utf-8

"""
    Binance USD-M Futures API

    OpenAPI specification for Binance exchange - Umfutures API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class UmfuturesGetLeverageBracketV1RespItemBracketsInner(BaseModel):
    """
    UmfuturesGetLeverageBracketV1RespItemBracketsInner
    """ # noqa: E501
    bracket: Optional[StrictInt] = None
    cum: Optional[StrictInt] = None
    initial_leverage: Optional[StrictInt] = Field(default=None, alias="initialLeverage")
    maint_margin_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maintMarginRatio")
    notional_cap: Optional[StrictInt] = Field(default=None, alias="notionalCap")
    notional_floor: Optional[StrictInt] = Field(default=None, alias="notionalFloor")
    __properties: ClassVar[List[str]] = ["bracket", "cum", "initialLeverage", "maintMarginRatio", "notionalCap", "notionalFloor"]

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
        """Create an instance of UmfuturesGetLeverageBracketV1RespItemBracketsInner from a JSON string"""
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
        """Create an instance of UmfuturesGetLeverageBracketV1RespItemBracketsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bracket": obj.get("bracket"),
            "cum": obj.get("cum"),
            "initialLeverage": obj.get("initialLeverage"),
            "maintMarginRatio": obj.get("maintMarginRatio"),
            "notionalCap": obj.get("notionalCap"),
            "notionalFloor": obj.get("notionalFloor")
        })
        return _obj


