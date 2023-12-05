# PatchUserGroupRequest

ユーザーグループ編集リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | グループ名 | [optional] 
**description** | **str** | グループ説明 | [optional] 
**type** | **str** | グループタイプ | [optional] 

## Example

```python
from traq.models.patch_user_group_request import PatchUserGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchUserGroupRequest from a JSON string
patch_user_group_request_instance = PatchUserGroupRequest.from_json(json)
# print the JSON string representation of the object
print PatchUserGroupRequest.to_json()

# convert the object into a dict
patch_user_group_request_dict = patch_user_group_request_instance.to_dict()
# create an instance of PatchUserGroupRequest from a dict
patch_user_group_request_form_dict = patch_user_group_request.from_dict(patch_user_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


