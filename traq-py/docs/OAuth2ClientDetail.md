# OAuth2ClientDetail

OAuth2クライアント詳細情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | クライアントUUID | 
**developer_id** | **str** | クライアント開発者UUID | 
**description** | **str** | 説明 | 
**name** | **str** | クライアント名 | 
**scopes** | [**List[OAuth2Scope]**](OAuth2Scope.md) | 要求スコープの配列 | 
**callback_url** | **str** | コールバックURL | 
**secret** | **str** | クライアントシークレット | 

## Example

```python
from traq.models.o_auth2_client_detail import OAuth2ClientDetail

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientDetail from a JSON string
o_auth2_client_detail_instance = OAuth2ClientDetail.from_json(json)
# print the JSON string representation of the object
print OAuth2ClientDetail.to_json()

# convert the object into a dict
o_auth2_client_detail_dict = o_auth2_client_detail_instance.to_dict()
# create an instance of OAuth2ClientDetail from a dict
o_auth2_client_detail_form_dict = o_auth2_client_detail.from_dict(o_auth2_client_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


