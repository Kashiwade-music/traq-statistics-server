# UserSettings

ユーザー設定の情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ユーザーUUID | 
**notify_citation** | **bool** | メッセージ引用通知の設定情報 | 

## Example

```python
from traq.models.user_settings import UserSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettings from a JSON string
user_settings_instance = UserSettings.from_json(json)
# print the JSON string representation of the object
print UserSettings.to_json()

# convert the object into a dict
user_settings_dict = user_settings_instance.to_dict()
# create an instance of UserSettings from a dict
user_settings_form_dict = user_settings.from_dict(user_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


