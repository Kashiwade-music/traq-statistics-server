# ForcedNotificationChangedEvent

チャンネル強制通知状態変更イベント

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | 変更者UUID | 
**force** | **bool** | 変更後強制通知状態 | 

## Example

```python
from traq.models.forced_notification_changed_event import ForcedNotificationChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ForcedNotificationChangedEvent from a JSON string
forced_notification_changed_event_instance = ForcedNotificationChangedEvent.from_json(json)
# print the JSON string representation of the object
print ForcedNotificationChangedEvent.to_json()

# convert the object into a dict
forced_notification_changed_event_dict = forced_notification_changed_event_instance.to_dict()
# create an instance of ForcedNotificationChangedEvent from a dict
forced_notification_changed_event_form_dict = forced_notification_changed_event.from_dict(forced_notification_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


