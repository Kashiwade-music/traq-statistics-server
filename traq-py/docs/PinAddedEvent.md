# PinAddedEvent

ピン追加イベント

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | 変更者UUID | 
**message_id** | **str** | メッセージUUID | 

## Example

```python
from traq.models.pin_added_event import PinAddedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PinAddedEvent from a JSON string
pin_added_event_instance = PinAddedEvent.from_json(json)
# print the JSON string representation of the object
print PinAddedEvent.to_json()

# convert the object into a dict
pin_added_event_dict = pin_added_event_instance.to_dict()
# create an instance of PinAddedEvent from a dict
pin_added_event_form_dict = pin_added_event.from_dict(pin_added_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


