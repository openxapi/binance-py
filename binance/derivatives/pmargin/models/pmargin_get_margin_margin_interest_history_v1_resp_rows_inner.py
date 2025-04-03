# coding: utf-8

"""
    Binance Portfolio Margin API

    OpenAPI specification for Binance exchange - Pmargin API

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

class PmarginGetMarginMarginInterestHistoryV1RespRowsInner(BaseModel):
    """
    PmarginGetMarginMarginInterestHistoryV1RespRowsInner
    """ # noqa: E501
    asset: Optional[StrictStr] = None
    interest: Optional[StrictStr] = None
    interest_accured_time: Optional[StrictInt] = Field(default=None, alias="interestAccuredTime")
    interest_rate: Optional[StrictStr] = Field(default=None, alias="interestRate")
    principal: Optional[StrictStr] = None
    raw_asset: Optional[StrictStr] = Field(default=None, alias="rawAsset")
    tx_id: Optional[StrictInt] = Field(default=None, alias="txId")
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["asset", "interest", "interestAccuredTime", "interestRate", "principal", "rawAsset", "txId", "type"]

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
        """Create an instance of PmarginGetMarginMarginInterestHistoryV1RespRowsInner from a JSON string"""
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
        """Create an instance of PmarginGetMarginMarginInterestHistoryV1RespRowsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asset": obj.get("asset"),
            "interest": obj.get("interest"),
            "interestAccuredTime": obj.get("interestAccuredTime"),
            "interestRate": obj.get("interestRate"),
            "principal": obj.get("principal"),
            "rawAsset": obj.get("rawAsset"),
            "txId": obj.get("txId"),
            "type": obj.get("type")
        })
        return _obj


