# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SpotGetHistoricalTradesV3RespItem(BaseModel):
    """
    SpotGetHistoricalTradesV3RespItem
    """ # noqa: E501
    id: Optional[StrictInt] = None
    is_best_match: Optional[StrictBool] = Field(default=None, alias="isBestMatch")
    is_buyer_maker: Optional[StrictBool] = Field(default=None, alias="isBuyerMaker")
    price: Optional[StrictStr] = None
    qty: Optional[StrictStr] = None
    quote_qty: Optional[StrictStr] = Field(default=None, alias="quoteQty")
    time: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "isBestMatch", "isBuyerMaker", "price", "qty", "quoteQty", "time"]

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
        """Create an instance of SpotGetHistoricalTradesV3RespItem from a JSON string"""
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
        """Create an instance of SpotGetHistoricalTradesV3RespItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "isBestMatch": obj.get("isBestMatch"),
            "isBuyerMaker": obj.get("isBuyerMaker"),
            "price": obj.get("price"),
            "qty": obj.get("qty"),
            "quoteQty": obj.get("quoteQty"),
            "time": obj.get("time")
        })
        return _obj


