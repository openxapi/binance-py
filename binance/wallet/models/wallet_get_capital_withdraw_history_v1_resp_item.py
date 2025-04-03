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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WalletGetCapitalWithdrawHistoryV1RespItem(BaseModel):
    """
    WalletGetCapitalWithdrawHistoryV1RespItem
    """ # noqa: E501
    address: Optional[StrictStr] = None
    amount: Optional[StrictStr] = None
    apply_time: Optional[StrictStr] = Field(default=None, alias="applyTime")
    coin: Optional[StrictStr] = None
    complete_time: Optional[StrictStr] = Field(default=None, alias="completeTime")
    confirm_no: Optional[StrictInt] = Field(default=None, alias="confirmNo")
    id: Optional[StrictStr] = None
    info: Optional[StrictStr] = None
    network: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    transaction_fee: Optional[StrictStr] = Field(default=None, alias="transactionFee")
    transfer_type: Optional[StrictInt] = Field(default=None, alias="transferType")
    tx_id: Optional[StrictStr] = Field(default=None, alias="txId")
    tx_key: Optional[StrictStr] = Field(default=None, alias="txKey")
    wallet_type: Optional[StrictInt] = Field(default=None, alias="walletType")
    withdraw_order_id: Optional[StrictStr] = Field(default=None, alias="withdrawOrderId")
    __properties: ClassVar[List[str]] = ["address", "amount", "applyTime", "coin", "completeTime", "confirmNo", "id", "info", "network", "status", "transactionFee", "transferType", "txId", "txKey", "walletType", "withdrawOrderId"]

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
        """Create an instance of WalletGetCapitalWithdrawHistoryV1RespItem from a JSON string"""
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
        """Create an instance of WalletGetCapitalWithdrawHistoryV1RespItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "amount": obj.get("amount"),
            "applyTime": obj.get("applyTime"),
            "coin": obj.get("coin"),
            "completeTime": obj.get("completeTime"),
            "confirmNo": obj.get("confirmNo"),
            "id": obj.get("id"),
            "info": obj.get("info"),
            "network": obj.get("network"),
            "status": obj.get("status"),
            "transactionFee": obj.get("transactionFee"),
            "transferType": obj.get("transferType"),
            "txId": obj.get("txId"),
            "txKey": obj.get("txKey"),
            "walletType": obj.get("walletType"),
            "withdrawOrderId": obj.get("withdrawOrderId")
        })
        return _obj


