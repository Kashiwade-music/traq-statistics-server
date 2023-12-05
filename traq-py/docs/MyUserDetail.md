# MyUserDetail

自分のユーザー詳細情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ユーザーUUID | 
**bio** | **str** | 自己紹介(biography) | 
**groups** | **List[str]** | 所属グループのUUIDの配列 | 
**tags** | [**List[UserTag]**](UserTag.md) | タグリスト | 
**updated_at** | **datetime** | 更新日時 | 
**last_online** | **datetime** | 最終オンライン日時 | 
**twitter_id** | **str** | Twitter ID | 
**name** | **str** | ユーザー名 | 
**display_name** | **str** | ユーザー表示名 | 
**icon_file_id** | **str** | アイコンファイルUUID | 
**bot** | **bool** | BOTかどうか | 
**state** | [**UserAccountState**](UserAccountState.md) |  | 
**permissions** | [**List[UserPermission]**](UserPermission.md) | 所有している権限の配列 | 
**home_channel** | **str** | ホームチャンネル | 

## Example

```python
from traq.models.my_user_detail import MyUserDetail

# TODO update the JSON string below
json = "{}"
# create an instance of MyUserDetail from a JSON string
my_user_detail_instance = MyUserDetail.from_json(json)
# print the JSON string representation of the object
print MyUserDetail.to_json()

# convert the object into a dict
my_user_detail_dict = my_user_detail_instance.to_dict()
# create an instance of MyUserDetail from a dict
my_user_detail_form_dict = my_user_detail.from_dict(my_user_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


