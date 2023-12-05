# ChildCreatedEvent

子チャンネル作成イベント

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | 作成者UUID | 
**channel_id** | **str** | チャンネルUUID | 

## Example

```python
from traq.models.child_created_event import ChildCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ChildCreatedEvent from a JSON string
child_created_event_instance = ChildCreatedEvent.from_json(json)
# print the JSON string representation of the object
print ChildCreatedEvent.to_json()

# convert the object into a dict
child_created_event_dict = child_created_event_instance.to_dict()
# create an instance of ChildCreatedEvent from a dict
child_created_event_form_dict = child_created_event.from_dict(child_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


