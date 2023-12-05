# PatchGroupMemberRequest

ユーザーグループメンバー編集リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | ユーザーの役割 | 

## Example

```python
from traq.models.patch_group_member_request import PatchGroupMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchGroupMemberRequest from a JSON string
patch_group_member_request_instance = PatchGroupMemberRequest.from_json(json)
# print the JSON string representation of the object
print PatchGroupMemberRequest.to_json()

# convert the object into a dict
patch_group_member_request_dict = patch_group_member_request_instance.to_dict()
# create an instance of PatchGroupMemberRequest from a dict
patch_group_member_request_form_dict = patch_group_member_request.from_dict(patch_group_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


