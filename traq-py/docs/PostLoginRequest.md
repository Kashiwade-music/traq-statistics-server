# PostLoginRequest

ログインリクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | ユーザー名 | 
**password** | **str** | パスワード | 

## Example

```python
from traq.models.post_login_request import PostLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoginRequest from a JSON string
post_login_request_instance = PostLoginRequest.from_json(json)
# print the JSON string representation of the object
print PostLoginRequest.to_json()

# convert the object into a dict
post_login_request_dict = post_login_request_instance.to_dict()
# create an instance of PostLoginRequest from a dict
post_login_request_form_dict = post_login_request.from_dict(post_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


