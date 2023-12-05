# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from traq.models.o_auth2_scope import OAuth2Scope
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OAuth2ClientDetail(BaseModel):
    """
    OAuth2クライアント詳細情報
    """ # noqa: E501
    id: StrictStr = Field(description="クライアントUUID")
    developer_id: StrictStr = Field(description="クライアント開発者UUID", alias="developerId")
    description: Annotated[str, Field(strict=True, max_length=1000)] = Field(description="説明")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=32)] = Field(description="クライアント名")
    scopes: List[OAuth2Scope] = Field(description="要求スコープの配列")
    callback_url: StrictStr = Field(description="コールバックURL", alias="callbackUrl")
    secret: StrictStr = Field(description="クライアントシークレット")
    __properties: ClassVar[List[str]] = ["id", "developerId", "description", "name", "scopes", "callbackUrl", "secret"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OAuth2ClientDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OAuth2ClientDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "developerId": obj.get("developerId"),
            "description": obj.get("description"),
            "name": obj.get("name"),
            "scopes": obj.get("scopes"),
            "callbackUrl": obj.get("callbackUrl"),
            "secret": obj.get("secret")
        })
        return _obj


