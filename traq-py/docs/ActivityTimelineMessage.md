# ActivityTimelineMessage

Timelineアクテビティ用メッセージ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | メッセージUUID | 
**user_id** | **str** | 投稿者UUID | 
**channel_id** | **str** | チャンネルUUID | 
**content** | **str** | メッセージ本文 | 
**created_at** | **datetime** | 投稿日時 | 
**updated_at** | **datetime** | 編集日時 | 

## Example

```python
from traq.models.activity_timeline_message import ActivityTimelineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTimelineMessage from a JSON string
activity_timeline_message_instance = ActivityTimelineMessage.from_json(json)
# print the JSON string representation of the object
print ActivityTimelineMessage.to_json()

# convert the object into a dict
activity_timeline_message_dict = activity_timeline_message_instance.to_dict()
# create an instance of ActivityTimelineMessage from a dict
activity_timeline_message_form_dict = activity_timeline_message.from_dict(activity_timeline_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


