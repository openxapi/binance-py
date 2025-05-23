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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from binance.spot.models.get_sub_account_spot_summary_v1_resp_spot_sub_user_asset_btc_vo_list_inner import GetSubAccountSpotSummaryV1RespSpotSubUserAssetBtcVoListInner
from typing import Optional, Set
from typing_extensions import Self

class GetSubAccountSpotSummaryV1Resp(BaseModel):
    """
    GetSubAccountSpotSummaryV1Resp
    """ # noqa: E501
    master_account_total_asset: Optional[StrictStr] = Field(default=None, alias="masterAccountTotalAsset")
    spot_sub_user_asset_btc_vo_list: Optional[List[GetSubAccountSpotSummaryV1RespSpotSubUserAssetBtcVoListInner]] = Field(default=None, alias="spotSubUserAssetBtcVoList")
    total_count: Optional[StrictInt] = Field(default=None, alias="totalCount")
    __properties: ClassVar[List[str]] = ["masterAccountTotalAsset", "spotSubUserAssetBtcVoList", "totalCount"]

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
        """Create an instance of GetSubAccountSpotSummaryV1Resp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in spot_sub_user_asset_btc_vo_list (list)
        _items = []
        if self.spot_sub_user_asset_btc_vo_list:
            for _item_spot_sub_user_asset_btc_vo_list in self.spot_sub_user_asset_btc_vo_list:
                if _item_spot_sub_user_asset_btc_vo_list:
                    _items.append(_item_spot_sub_user_asset_btc_vo_list.to_dict())
            _dict['spotSubUserAssetBtcVoList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetSubAccountSpotSummaryV1Resp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "masterAccountTotalAsset": obj.get("masterAccountTotalAsset"),
            "spotSubUserAssetBtcVoList": [GetSubAccountSpotSummaryV1RespSpotSubUserAssetBtcVoListInner.from_dict(_item) for _item in obj["spotSubUserAssetBtcVoList"]] if obj.get("spotSubUserAssetBtcVoList") is not None else None,
            "totalCount": obj.get("totalCount")
        })
        return _obj


