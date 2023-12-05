# PostUserGroupAdminRequest

グループ管理者追加リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 追加するユーザーのUUID | 

## Example

```python
from traq.models.post_user_group_admin_request import PostUserGroupAdminRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUserGroupAdminRequest from a JSON string
post_user_group_admin_request_instance = PostUserGroupAdminRequest.from_json(json)
# print the JSON string representation of the object
print PostUserGroupAdminRequest.to_json()

# convert the object into a dict
post_user_group_admin_request_dict = post_user_group_admin_request_instance.to_dict()
# create an instance of PostUserGroupAdminRequest from a dict
post_user_group_admin_request_form_dict = post_user_group_admin_request.from_dict(post_user_group_admin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


