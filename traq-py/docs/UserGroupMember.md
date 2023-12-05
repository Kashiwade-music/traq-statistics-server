# UserGroupMember

ユーザーグループメンバー

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ユーザーUUID | 
**role** | **str** | ユーザーの役割 | 

## Example

```python
from traq.models.user_group_member import UserGroupMember

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupMember from a JSON string
user_group_member_instance = UserGroupMember.from_json(json)
# print the JSON string representation of the object
print UserGroupMember.to_json()

# convert the object into a dict
user_group_member_dict = user_group_member_instance.to_dict()
# create an instance of UserGroupMember from a dict
user_group_member_form_dict = user_group_member.from_dict(user_group_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


