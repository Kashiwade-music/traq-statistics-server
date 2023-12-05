# PostClientRequest

OAuth2クライアント作成リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | クライアント名 | 
**callback_url** | **str** | コールバックURL | 
**scopes** | [**List[OAuth2Scope]**](OAuth2Scope.md) | 要求スコープの配列 | 
**description** | **str** | 説明 | 

## Example

```python
from traq.models.post_client_request import PostClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientRequest from a JSON string
post_client_request_instance = PostClientRequest.from_json(json)
# print the JSON string representation of the object
print PostClientRequest.to_json()

# convert the object into a dict
post_client_request_dict = post_client_request_instance.to_dict()
# create an instance of PostClientRequest from a dict
post_client_request_form_dict = post_client_request.from_dict(post_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


