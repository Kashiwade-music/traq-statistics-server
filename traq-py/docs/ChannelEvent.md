# ChannelEvent

チャンネルイベント

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | イベントタイプ | 
**datetime** | **datetime** | イベント日時 | 
**detail** | [**ChannelEventDetail**](ChannelEventDetail.md) |  | 

## Example

```python
from traq.models.channel_event import ChannelEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelEvent from a JSON string
channel_event_instance = ChannelEvent.from_json(json)
# print the JSON string representation of the object
print ChannelEvent.to_json()

# convert the object into a dict
channel_event_dict = channel_event_instance.to_dict()
# create an instance of ChannelEvent from a dict
channel_event_form_dict = channel_event.from_dict(channel_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


