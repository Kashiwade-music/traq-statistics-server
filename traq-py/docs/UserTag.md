# UserTag

ユーザータグ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **str** | タグUUID | 
**tag** | **str** | タグ文字列 | 
**is_locked** | **bool** | タグがロックされているか | 
**created_at** | **datetime** | タグ付与日時 | 
**updated_at** | **datetime** | タグ更新日時 | 

## Example

```python
from traq.models.user_tag import UserTag

# TODO update the JSON string below
json = "{}"
# create an instance of UserTag from a JSON string
user_tag_instance = UserTag.from_json(json)
# print the JSON string representation of the object
print UserTag.to_json()

# convert the object into a dict
user_tag_dict = user_tag_instance.to_dict()
# create an instance of UserTag from a dict
user_tag_form_dict = user_tag.from_dict(user_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


