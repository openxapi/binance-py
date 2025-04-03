# coding: utf-8

"""
    Binance Wallet API

    OpenAPI specification for Binance exchange - Wallet API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from binance.wallet.models.wallet_create_asset_dust_btc_v1_resp_details_inner import WalletCreateAssetDustBtcV1RespDetailsInner
from typing import Optional, Set
from typing_extensions import Self

class WalletCreateAssetDustBtcV1Resp(BaseModel):
    """
    WalletCreateAssetDustBtcV1Resp
    """ # noqa: E501
    details: Optional[List[WalletCreateAssetDustBtcV1RespDetailsInner]] = None
    dribblet_percentage: Optional[StrictStr] = Field(default=None, alias="dribbletPercentage")
    total_transfer_bnb: Optional[StrictStr] = Field(default=None, alias="totalTransferBNB")
    total_transfer_btc: Optional[StrictStr] = Field(default=None, alias="totalTransferBtc")
    __properties: ClassVar[List[str]] = ["details", "dribbletPercentage", "totalTransferBNB", "totalTransferBtc"]

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
        """Create an instance of WalletCreateAssetDustBtcV1Resp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in details (list)
        _items = []
        if self.details:
            for _item_details in self.details:
                if _item_details:
                    _items.append(_item_details.to_dict())
            _dict['details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WalletCreateAssetDustBtcV1Resp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "details": [WalletCreateAssetDustBtcV1RespDetailsInner.from_dict(_item) for _item in obj["details"]] if obj.get("details") is not None else None,
            "dribbletPercentage": obj.get("dribbletPercentage"),
            "totalTransferBNB": obj.get("totalTransferBNB"),
            "totalTransferBtc": obj.get("totalTransferBtc")
        })
        return _obj


