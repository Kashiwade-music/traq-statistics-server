# PostUserRequest

ユーザー登録リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | ユーザー名 | 
**password** | **str** | パスワード | [optional] 

## Example

```python
from traq.models.post_user_request import PostUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUserRequest from a JSON string
post_user_request_instance = PostUserRequest.from_json(json)
# print the JSON string representation of the object
print PostUserRequest.to_json()

# convert the object into a dict
post_user_request_dict = post_user_request_instance.to_dict()
# create an instance of PostUserRequest from a dict
post_user_request_form_dict = post_user_request.from_dict(post_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


