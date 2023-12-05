# ChannelEventDetail

イベント内容

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | 作成者UUID | 
**before** | **str** | 変更前親チャンネルUUID | 
**after** | **str** | 変更後親チャンネルUUID | 
**on** | **List[str]** | オンにされたユーザーのUUID配列 | 
**off** | **List[str]** | オフにされたユーザーのUUID配列 | 
**message_id** | **str** | メッセージUUID | 
**visibility** | **bool** | 変更後可視状態 | 
**force** | **bool** | 変更後強制通知状態 | 
**channel_id** | **str** | チャンネルUUID | 

## Example

```python
from traq.models.channel_event_detail import ChannelEventDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelEventDetail from a JSON string
channel_event_detail_instance = ChannelEventDetail.from_json(json)
# print the JSON string representation of the object
print ChannelEventDetail.to_json()

# convert the object into a dict
channel_event_detail_dict = channel_event_detail_instance.to_dict()
# create an instance of ChannelEventDetail from a dict
channel_event_detail_form_dict = channel_event_detail.from_dict(channel_event_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


