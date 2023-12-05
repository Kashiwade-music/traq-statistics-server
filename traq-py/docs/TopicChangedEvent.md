# TopicChangedEvent

トピック変更イベント

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | 変更者UUID | 
**before** | **str** | 変更前トピック | 
**after** | **str** | 変更後トピック | 

## Example

```python
from traq.models.topic_changed_event import TopicChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TopicChangedEvent from a JSON string
topic_changed_event_instance = TopicChangedEvent.from_json(json)
# print the JSON string representation of the object
print TopicChangedEvent.to_json()

# convert the object into a dict
topic_changed_event_dict = topic_changed_event_instance.to_dict()
# create an instance of TopicChangedEvent from a dict
topic_changed_event_form_dict = topic_changed_event.from_dict(topic_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


