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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from binance.derivatives.pmargin.models.pmargin_get_cm_account_v1_resp_assets_inner import PmarginGetCmAccountV1RespAssetsInner
from binance.derivatives.pmargin.models.pmargin_get_cm_account_v1_resp_positions_inner import PmarginGetCmAccountV1RespPositionsInner
from typing import Optional, Set
from typing_extensions import Self

class PmarginGetCmAccountV1Resp(BaseModel):
    """
    PmarginGetCmAccountV1Resp
    """ # noqa: E501
    assets: Optional[List[PmarginGetCmAccountV1RespAssetsInner]] = None
    positions: Optional[List[PmarginGetCmAccountV1RespPositionsInner]] = None
    __properties: ClassVar[List[str]] = ["assets", "positions"]

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
        """Create an instance of PmarginGetCmAccountV1Resp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in assets (list)
        _items = []
        if self.assets:
            for _item_assets in self.assets:
                if _item_assets:
                    _items.append(_item_assets.to_dict())
            _dict['assets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in positions (list)
        _items = []
        if self.positions:
            for _item_positions in self.positions:
                if _item_positions:
                    _items.append(_item_positions.to_dict())
            _dict['positions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PmarginGetCmAccountV1Resp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assets": [PmarginGetCmAccountV1RespAssetsInner.from_dict(_item) for _item in obj["assets"]] if obj.get("assets") is not None else None,
            "positions": [PmarginGetCmAccountV1RespPositionsInner.from_dict(_item) for _item in obj["positions"]] if obj.get("positions") is not None else None
        })
        return _obj


