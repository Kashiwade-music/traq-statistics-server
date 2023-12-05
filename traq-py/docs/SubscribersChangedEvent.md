# SubscribersChangedEvent

購読者変更イベント

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | 変更者UUID | 
**on** | **List[str]** | オンにされたユーザーのUUID配列 | 
**off** | **List[str]** | オフにされたユーザーのUUID配列 | 

## Example

```python
from traq.models.subscribers_changed_event import SubscribersChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribersChangedEvent from a JSON string
subscribers_changed_event_instance = SubscribersChangedEvent.from_json(json)
# print the JSON string representation of the object
print SubscribersChangedEvent.to_json()

# convert the object into a dict
subscribers_changed_event_dict = subscribers_changed_event_instance.to_dict()
# create an instance of SubscribersChangedEvent from a dict
subscribers_changed_event_form_dict = subscribers_changed_event.from_dict(subscribers_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


