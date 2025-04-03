# coding: utf-8

"""
    Binance Spot API

    OpenAPI specification for Binance exchange - Spot API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from binance.spot.models.spot_get_ticker_price_v3_resp_item import SpotGetTickerPriceV3RespItem
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

SPOTGETTICKERPRICEV3RESP_ONE_OF_SCHEMAS = ["List[SpotGetTickerPriceV3RespItem]", "SpotGetTickerPriceV3RespItem"]

class SpotGetTickerPriceV3Resp(BaseModel):
    """
    SpotGetTickerPriceV3Resp
    """
    # data type: List[SpotGetTickerPriceV3RespItem]
    oneof_schema_1_validator: Optional[List[SpotGetTickerPriceV3RespItem]] = None
    # data type: SpotGetTickerPriceV3RespItem
    oneof_schema_2_validator: Optional[SpotGetTickerPriceV3RespItem] = None
    actual_instance: Optional[Union[List[SpotGetTickerPriceV3RespItem], SpotGetTickerPriceV3RespItem]] = None
    one_of_schemas: Set[str] = { "List[SpotGetTickerPriceV3RespItem]", "SpotGetTickerPriceV3RespItem" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = SpotGetTickerPriceV3Resp.model_construct()
        error_messages = []
        match = 0
        # validate data type: List[SpotGetTickerPriceV3RespItem]
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: SpotGetTickerPriceV3RespItem
        if not isinstance(v, SpotGetTickerPriceV3RespItem):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SpotGetTickerPriceV3RespItem`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SpotGetTickerPriceV3Resp with oneOf schemas: List[SpotGetTickerPriceV3RespItem], SpotGetTickerPriceV3RespItem. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SpotGetTickerPriceV3Resp with oneOf schemas: List[SpotGetTickerPriceV3RespItem], SpotGetTickerPriceV3RespItem. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into List[SpotGetTickerPriceV3RespItem]
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SpotGetTickerPriceV3RespItem
        try:
            instance.actual_instance = SpotGetTickerPriceV3RespItem.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SpotGetTickerPriceV3Resp with oneOf schemas: List[SpotGetTickerPriceV3RespItem], SpotGetTickerPriceV3RespItem. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SpotGetTickerPriceV3Resp with oneOf schemas: List[SpotGetTickerPriceV3RespItem], SpotGetTickerPriceV3RespItem. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], List[SpotGetTickerPriceV3RespItem], SpotGetTickerPriceV3RespItem]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


