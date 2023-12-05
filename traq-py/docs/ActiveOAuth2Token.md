# ActiveOAuth2Token

有効なOAuth2トークン情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | トークンUUID | 
**client_id** | **str** | OAuth2クライアントUUID | 
**scopes** | [**List[OAuth2Scope]**](OAuth2Scope.md) | スコープ | 
**issued_at** | **datetime** | 発行日時 | 

## Example

```python
from traq.models.active_o_auth2_token import ActiveOAuth2Token

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveOAuth2Token from a JSON string
active_o_auth2_token_instance = ActiveOAuth2Token.from_json(json)
# print the JSON string representation of the object
print ActiveOAuth2Token.to_json()

# convert the object into a dict
active_o_auth2_token_dict = active_o_auth2_token_instance.to_dict()
# create an instance of ActiveOAuth2Token from a dict
active_o_auth2_token_form_dict = active_o_auth2_token.from_dict(active_o_auth2_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


