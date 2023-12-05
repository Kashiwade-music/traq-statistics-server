# VisibilityChangedEvent

チャンネル可視状態変更イベント

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | 変更者UUID | 
**visibility** | **bool** | 変更後可視状態 | 

## Example

```python
from traq.models.visibility_changed_event import VisibilityChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VisibilityChangedEvent from a JSON string
visibility_changed_event_instance = VisibilityChangedEvent.from_json(json)
# print the JSON string representation of the object
print VisibilityChangedEvent.to_json()

# convert the object into a dict
visibility_changed_event_dict = visibility_changed_event_instance.to_dict()
# create an instance of VisibilityChangedEvent from a dict
visibility_changed_event_form_dict = visibility_changed_event.from_dict(visibility_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


