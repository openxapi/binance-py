# coding: utf-8

"""
    Binance Margin Trading API

    OpenAPI specification for Binance exchange - Margin API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from binance.margin.models.margin_get_margin_isolated_account_v1_resp_assets_inner_base_asset import MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset
from typing import Optional, Set
from typing_extensions import Self

class MarginGetMarginIsolatedAccountV1RespAssetsInner(BaseModel):
    """
    MarginGetMarginIsolatedAccountV1RespAssetsInner
    """ # noqa: E501
    base_asset: Optional[MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset] = Field(default=None, alias="baseAsset")
    enabled: Optional[StrictBool] = None
    index_price: Optional[StrictStr] = Field(default=None, alias="indexPrice")
    isolated_created: Optional[StrictBool] = Field(default=None, alias="isolatedCreated")
    liquidate_price: Optional[StrictStr] = Field(default=None, alias="liquidatePrice")
    liquidate_rate: Optional[StrictStr] = Field(default=None, alias="liquidateRate")
    margin_level: Optional[StrictStr] = Field(default=None, alias="marginLevel")
    margin_level_status: Optional[StrictStr] = Field(default=None, alias="marginLevelStatus")
    margin_ratio: Optional[StrictStr] = Field(default=None, alias="marginRatio")
    quote_asset: Optional[MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset] = Field(default=None, alias="quoteAsset")
    symbol: Optional[StrictStr] = None
    trade_enabled: Optional[StrictBool] = Field(default=None, alias="tradeEnabled")
    __properties: ClassVar[List[str]] = ["baseAsset", "enabled", "indexPrice", "isolatedCreated", "liquidatePrice", "liquidateRate", "marginLevel", "marginLevelStatus", "marginRatio", "quoteAsset", "symbol", "tradeEnabled"]

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
        """Create an instance of MarginGetMarginIsolatedAccountV1RespAssetsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of base_asset
        if self.base_asset:
            _dict['baseAsset'] = self.base_asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quote_asset
        if self.quote_asset:
            _dict['quoteAsset'] = self.quote_asset.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MarginGetMarginIsolatedAccountV1RespAssetsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "baseAsset": MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.from_dict(obj["baseAsset"]) if obj.get("baseAsset") is not None else None,
            "enabled": obj.get("enabled"),
            "indexPrice": obj.get("indexPrice"),
            "isolatedCreated": obj.get("isolatedCreated"),
            "liquidatePrice": obj.get("liquidatePrice"),
            "liquidateRate": obj.get("liquidateRate"),
            "marginLevel": obj.get("marginLevel"),
            "marginLevelStatus": obj.get("marginLevelStatus"),
            "marginRatio": obj.get("marginRatio"),
            "quoteAsset": MarginGetMarginIsolatedAccountV1RespAssetsInnerBaseAsset.from_dict(obj["quoteAsset"]) if obj.get("quoteAsset") is not None else None,
            "symbol": obj.get("symbol"),
            "tradeEnabled": obj.get("tradeEnabled")
        })
        return _obj


