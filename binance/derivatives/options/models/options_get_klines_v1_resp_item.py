# coding: utf-8

"""
    Binance Options API

    OpenAPI specification for Binance exchange - Options API

    The version of the OpenAPI document: 0.1.0
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

class OptionsGetKlinesV1RespItem(BaseModel):
    """
    OptionsGetKlinesV1RespItem
    """ # noqa: E501
    amount: Optional[StrictStr] = None
    close: Optional[StrictStr] = None
    close_time: Optional[StrictInt] = Field(default=None, alias="closeTime")
    high: Optional[StrictStr] = None
    interval: Optional[StrictStr] = None
    low: Optional[StrictStr] = None
    open: Optional[StrictStr] = None
    open_time: Optional[StrictInt] = Field(default=None, alias="openTime")
    taker_amount: Optional[StrictStr] = Field(default=None, alias="takerAmount")
    taker_volume: Optional[StrictStr] = Field(default=None, alias="takerVolume")
    trade_count: Optional[StrictInt] = Field(default=None, alias="tradeCount")
    volume: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["amount", "close", "closeTime", "high", "interval", "low", "open", "openTime", "takerAmount", "takerVolume", "tradeCount", "volume"]

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
        """Create an instance of OptionsGetKlinesV1RespItem from a JSON string"""
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
        """Create an instance of OptionsGetKlinesV1RespItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "close": obj.get("close"),
            "closeTime": obj.get("closeTime"),
            "high": obj.get("high"),
            "interval": obj.get("interval"),
            "low": obj.get("low"),
            "open": obj.get("open"),
            "openTime": obj.get("openTime"),
            "takerAmount": obj.get("takerAmount"),
            "takerVolume": obj.get("takerVolume"),
            "tradeCount": obj.get("tradeCount"),
            "volume": obj.get("volume")
        })
        return _obj


