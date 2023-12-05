# OAuth2Client

OAuth2クライアント情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | クライアントUUID | 
**name** | **str** | クライアント名 | 
**description** | **str** | 説明 | 
**developer_id** | **str** | クライアント開発者UUID | 
**scopes** | [**List[OAuth2Scope]**](OAuth2Scope.md) | 要求スコープの配列 | 

## Example

```python
from traq.models.o_auth2_client import OAuth2Client

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Client from a JSON string
o_auth2_client_instance = OAuth2Client.from_json(json)
# print the JSON string representation of the object
print OAuth2Client.to_json()

# convert the object into a dict
o_auth2_client_dict = o_auth2_client_instance.to_dict()
# create an instance of OAuth2Client from a dict
o_auth2_client_form_dict = o_auth2_client.from_dict(o_auth2_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


