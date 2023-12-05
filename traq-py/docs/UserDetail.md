# UserDetail

ユーザー詳細情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ユーザーUUID | 
**state** | [**UserAccountState**](UserAccountState.md) |  | 
**bot** | **bool** | BOTかどうか | 
**icon_file_id** | **str** | アイコンファイルUUID | 
**display_name** | **str** | ユーザー表示名 | 
**name** | **str** | ユーザー名 | 
**twitter_id** | **str** | Twitter ID | 
**last_online** | **datetime** | 最終オンライン日時 | 
**updated_at** | **datetime** | 更新日時 | 
**tags** | [**List[UserTag]**](UserTag.md) | タグリスト | 
**groups** | **List[str]** | 所属グループのUUIDの配列 | 
**bio** | **str** | 自己紹介(biography) | 
**home_channel** | **str** | ホームチャンネル | 

## Example

```python
from traq.models.user_detail import UserDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetail from a JSON string
user_detail_instance = UserDetail.from_json(json)
# print the JSON string representation of the object
print UserDetail.to_json()

# convert the object into a dict
user_detail_dict = user_detail_instance.to_dict()
# create an instance of UserDetail from a dict
user_detail_form_dict = user_detail.from_dict(user_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


