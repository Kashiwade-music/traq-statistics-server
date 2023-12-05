# UserGroup

ユーザーグループ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | グループUUID | 
**name** | **str** | グループ名 | 
**description** | **str** | グループ説明 | 
**type** | **str** | グループタイプ | 
**icon** | **str** | グループアイコンUUID | 
**members** | [**List[UserGroupMember]**](UserGroupMember.md) | グループメンバーの配列 | 
**created_at** | **datetime** | 作成日時 | 
**updated_at** | **datetime** | 更新日時 | 
**admins** | **List[str]** | グループ管理者のUUIDの配列 | 

## Example

```python
from traq.models.user_group import UserGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroup from a JSON string
user_group_instance = UserGroup.from_json(json)
# print the JSON string representation of the object
print UserGroup.to_json()

# convert the object into a dict
user_group_dict = user_group_instance.to_dict()
# create an instance of UserGroup from a dict
user_group_form_dict = user_group.from_dict(user_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


