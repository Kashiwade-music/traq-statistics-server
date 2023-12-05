# PostUserGroupRequest

ユーザーグループ作成リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | グループ名 | 
**description** | **str** | 説明 | 
**type** | **str** | グループタイプ | 

## Example

```python
from traq.models.post_user_group_request import PostUserGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUserGroupRequest from a JSON string
post_user_group_request_instance = PostUserGroupRequest.from_json(json)
# print the JSON string representation of the object
print PostUserGroupRequest.to_json()

# convert the object into a dict
post_user_group_request_dict = post_user_group_request_instance.to_dict()
# create an instance of PostUserGroupRequest from a dict
post_user_group_request_form_dict = post_user_group_request.from_dict(post_user_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


