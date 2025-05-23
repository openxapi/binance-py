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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from binance.spot.models.spot_symbol_filter import SpotSymbolFilter
from typing import Optional, Set
from typing_extensions import Self

class SpotGetExchangeInfoV3RespSymbolsInner(BaseModel):
    """
    SpotGetExchangeInfoV3RespSymbolsInner
    """ # noqa: E501
    allow_trailing_stop: Optional[StrictBool] = Field(default=None, alias="allowTrailingStop")
    allowed_self_trade_prevention_modes: Optional[List[StrictStr]] = Field(default=None, alias="allowedSelfTradePreventionModes")
    base_asset: Optional[StrictStr] = Field(default=None, alias="baseAsset")
    base_asset_precision: Optional[StrictInt] = Field(default=None, alias="baseAssetPrecision")
    base_commission_precision: Optional[StrictInt] = Field(default=None, alias="baseCommissionPrecision")
    cancel_replace_allowed: Optional[StrictBool] = Field(default=None, alias="cancelReplaceAllowed")
    default_self_trade_prevention_mode: Optional[StrictStr] = Field(default=None, alias="defaultSelfTradePreventionMode")
    filters: Optional[List[SpotSymbolFilter]] = None
    iceberg_allowed: Optional[StrictBool] = Field(default=None, alias="icebergAllowed")
    is_margin_trading_allowed: Optional[StrictBool] = Field(default=None, alias="isMarginTradingAllowed")
    is_spot_trading_allowed: Optional[StrictBool] = Field(default=None, alias="isSpotTradingAllowed")
    oco_allowed: Optional[StrictBool] = Field(default=None, alias="ocoAllowed")
    order_types: Optional[List[StrictStr]] = Field(default=None, alias="orderTypes")
    oto_allowed: Optional[StrictBool] = Field(default=None, alias="otoAllowed")
    permission_sets: Optional[List[List[StrictStr]]] = Field(default=None, alias="permissionSets")
    permissions: Optional[List[StrictStr]] = None
    quote_asset: Optional[StrictStr] = Field(default=None, alias="quoteAsset")
    quote_asset_precision: Optional[StrictInt] = Field(default=None, alias="quoteAssetPrecision")
    quote_commission_precision: Optional[StrictInt] = Field(default=None, alias="quoteCommissionPrecision")
    quote_order_qty_market_allowed: Optional[StrictBool] = Field(default=None, alias="quoteOrderQtyMarketAllowed")
    quote_precision: Optional[StrictInt] = Field(default=None, alias="quotePrecision")
    status: Optional[StrictStr] = None
    symbol: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["allowTrailingStop", "allowedSelfTradePreventionModes", "baseAsset", "baseAssetPrecision", "baseCommissionPrecision", "cancelReplaceAllowed", "defaultSelfTradePreventionMode", "filters", "icebergAllowed", "isMarginTradingAllowed", "isSpotTradingAllowed", "ocoAllowed", "orderTypes", "otoAllowed", "permissionSets", "permissions", "quoteAsset", "quoteAssetPrecision", "quoteCommissionPrecision", "quoteOrderQtyMarketAllowed", "quotePrecision", "status", "symbol"]

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
        """Create an instance of SpotGetExchangeInfoV3RespSymbolsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item_filters in self.filters:
                if _item_filters:
                    _items.append(_item_filters.to_dict())
            _dict['filters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpotGetExchangeInfoV3RespSymbolsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowTrailingStop": obj.get("allowTrailingStop"),
            "allowedSelfTradePreventionModes": obj.get("allowedSelfTradePreventionModes"),
            "baseAsset": obj.get("baseAsset"),
            "baseAssetPrecision": obj.get("baseAssetPrecision"),
            "baseCommissionPrecision": obj.get("baseCommissionPrecision"),
            "cancelReplaceAllowed": obj.get("cancelReplaceAllowed"),
            "defaultSelfTradePreventionMode": obj.get("defaultSelfTradePreventionMode"),
            "filters": [SpotSymbolFilter.from_dict(_item) for _item in obj["filters"]] if obj.get("filters") is not None else None,
            "icebergAllowed": obj.get("icebergAllowed"),
            "isMarginTradingAllowed": obj.get("isMarginTradingAllowed"),
            "isSpotTradingAllowed": obj.get("isSpotTradingAllowed"),
            "ocoAllowed": obj.get("ocoAllowed"),
            "orderTypes": obj.get("orderTypes"),
            "otoAllowed": obj.get("otoAllowed"),
            "permissionSets": obj.get("permissionSets"),
            "permissions": obj.get("permissions"),
            "quoteAsset": obj.get("quoteAsset"),
            "quoteAssetPrecision": obj.get("quoteAssetPrecision"),
            "quoteCommissionPrecision": obj.get("quoteCommissionPrecision"),
            "quoteOrderQtyMarketAllowed": obj.get("quoteOrderQtyMarketAllowed"),
            "quotePrecision": obj.get("quotePrecision"),
            "status": obj.get("status"),
            "symbol": obj.get("symbol")
        })
        return _obj


