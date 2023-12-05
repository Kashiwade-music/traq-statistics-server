# NameChangedEvent

チャンネル名変更イベント

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | 変更者UUID | 
**before** | **str** | 変更前チャンネル名 | 
**after** | **str** | 変更後チャンネル名 | 

## Example

```python
from traq.models.name_changed_event import NameChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NameChangedEvent from a JSON string
name_changed_event_instance = NameChangedEvent.from_json(json)
# print the JSON string representation of the object
print NameChangedEvent.to_json()

# convert the object into a dict
name_changed_event_dict = name_changed_event_instance.to_dict()
# create an instance of NameChangedEvent from a dict
name_changed_event_form_dict = name_changed_event.from_dict(name_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


