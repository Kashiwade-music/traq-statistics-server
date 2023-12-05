# ParentChangedEvent

親チャンネル変更イベント

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | 変更者UUID | 
**before** | **str** | 変更前親チャンネルUUID | 
**after** | **str** | 変更後親チャンネルUUID | 

## Example

```python
from traq.models.parent_changed_event import ParentChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ParentChangedEvent from a JSON string
parent_changed_event_instance = ParentChangedEvent.from_json(json)
# print the JSON string representation of the object
print ParentChangedEvent.to_json()

# convert the object into a dict
parent_changed_event_dict = parent_changed_event_instance.to_dict()
# create an instance of ParentChangedEvent from a dict
parent_changed_event_form_dict = parent_changed_event.from_dict(parent_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


