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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WalletGetCapitalConfigGetallV1RespItemNetworkListInner(BaseModel):
    """
    WalletGetCapitalConfigGetallV1RespItemNetworkListInner
    """ # noqa: E501
    address_regex: Optional[StrictStr] = Field(default=None, alias="addressRegex")
    busy: Optional[StrictBool] = None
    coin: Optional[StrictStr] = None
    contract_address: Optional[StrictStr] = Field(default=None, alias="contractAddress")
    contract_address_url: Optional[StrictStr] = Field(default=None, alias="contractAddressUrl")
    deposit_desc: Optional[StrictStr] = Field(default=None, alias="depositDesc")
    deposit_enable: Optional[StrictBool] = Field(default=None, alias="depositEnable")
    estimated_arrival_time: Optional[StrictInt] = Field(default=None, alias="estimatedArrivalTime")
    is_default: Optional[StrictBool] = Field(default=None, alias="isDefault")
    memo_regex: Optional[StrictStr] = Field(default=None, alias="memoRegex")
    min_confirm: Optional[StrictInt] = Field(default=None, alias="minConfirm")
    name: Optional[StrictStr] = None
    network: Optional[StrictStr] = None
    same_address: Optional[StrictBool] = Field(default=None, alias="sameAddress")
    special_tips: Optional[StrictStr] = Field(default=None, alias="specialTips")
    un_lock_confirm: Optional[StrictInt] = Field(default=None, alias="unLockConfirm")
    withdraw_desc: Optional[StrictStr] = Field(default=None, alias="withdrawDesc")
    withdraw_enable: Optional[StrictBool] = Field(default=None, alias="withdrawEnable")
    withdraw_fee: Optional[StrictStr] = Field(default=None, alias="withdrawFee")
    withdraw_integer_multiple: Optional[StrictStr] = Field(default=None, alias="withdrawIntegerMultiple")
    withdraw_internal_min: Optional[StrictStr] = Field(default=None, alias="withdrawInternalMin")
    withdraw_max: Optional[StrictStr] = Field(default=None, alias="withdrawMax")
    withdraw_min: Optional[StrictStr] = Field(default=None, alias="withdrawMin")
    __properties: ClassVar[List[str]] = ["addressRegex", "busy", "coin", "contractAddress", "contractAddressUrl", "depositDesc", "depositEnable", "estimatedArrivalTime", "isDefault", "memoRegex", "minConfirm", "name", "network", "sameAddress", "specialTips", "unLockConfirm", "withdrawDesc", "withdrawEnable", "withdrawFee", "withdrawIntegerMultiple", "withdrawInternalMin", "withdrawMax", "withdrawMin"]

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
        """Create an instance of WalletGetCapitalConfigGetallV1RespItemNetworkListInner from a JSON string"""
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
        """Create an instance of WalletGetCapitalConfigGetallV1RespItemNetworkListInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addressRegex": obj.get("addressRegex"),
            "busy": obj.get("busy"),
            "coin": obj.get("coin"),
            "contractAddress": obj.get("contractAddress"),
            "contractAddressUrl": obj.get("contractAddressUrl"),
            "depositDesc": obj.get("depositDesc"),
            "depositEnable": obj.get("depositEnable"),
            "estimatedArrivalTime": obj.get("estimatedArrivalTime"),
            "isDefault": obj.get("isDefault"),
            "memoRegex": obj.get("memoRegex"),
            "minConfirm": obj.get("minConfirm"),
            "name": obj.get("name"),
            "network": obj.get("network"),
            "sameAddress": obj.get("sameAddress"),
            "specialTips": obj.get("specialTips"),
            "unLockConfirm": obj.get("unLockConfirm"),
            "withdrawDesc": obj.get("withdrawDesc"),
            "withdrawEnable": obj.get("withdrawEnable"),
            "withdrawFee": obj.get("withdrawFee"),
            "withdrawIntegerMultiple": obj.get("withdrawIntegerMultiple"),
            "withdrawInternalMin": obj.get("withdrawInternalMin"),
            "withdrawMax": obj.get("withdrawMax"),
            "withdrawMin": obj.get("withdrawMin")
        })
        return _obj


