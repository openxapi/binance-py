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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from binance.options.models.get_account_v1_resp_asset_inner import GetAccountV1RespAssetInner
from binance.options.models.get_account_v1_resp_greek_inner import GetAccountV1RespGreekInner
from typing import Optional, Set
from typing_extensions import Self

class GetAccountV1Resp(BaseModel):
    """
    GetAccountV1Resp
    """ # noqa: E501
    asset: Optional[List[GetAccountV1RespAssetInner]] = None
    greek: Optional[List[GetAccountV1RespGreekInner]] = None
    risk_level: Optional[StrictStr] = Field(default=None, alias="riskLevel")
    time: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["asset", "greek", "riskLevel", "time"]

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
        """Create an instance of GetAccountV1Resp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in asset (list)
        _items = []
        if self.asset:
            for _item_asset in self.asset:
                if _item_asset:
                    _items.append(_item_asset.to_dict())
            _dict['asset'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in greek (list)
        _items = []
        if self.greek:
            for _item_greek in self.greek:
                if _item_greek:
                    _items.append(_item_greek.to_dict())
            _dict['greek'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetAccountV1Resp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asset": [GetAccountV1RespAssetInner.from_dict(_item) for _item in obj["asset"]] if obj.get("asset") is not None else None,
            "greek": [GetAccountV1RespGreekInner.from_dict(_item) for _item in obj["greek"]] if obj.get("greek") is not None else None,
            "riskLevel": obj.get("riskLevel"),
            "time": obj.get("time")
        })
        return _obj


