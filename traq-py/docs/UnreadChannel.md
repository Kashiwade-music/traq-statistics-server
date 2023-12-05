# UnreadChannel

未読チャンネル情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | チャンネルUUID | 
**count** | **int** | 未読メッセージ数 | 
**noticeable** | **bool** | 自分宛てメッセージが含まれているかどうか | 
**since** | **datetime** | チャンネルの最古の未読メッセージの日時 | 
**updated_at** | **datetime** | チャンネルの最新の未読メッセージの日時 | 
**oldest_message_id** | **str** | そのチャンネルの未読の中で最も古いメッセージのid | 

## Example

```python
from traq.models.unread_channel import UnreadChannel

# TODO update the JSON string below
json = "{}"
# create an instance of UnreadChannel from a JSON string
unread_channel_instance = UnreadChannel.from_json(json)
# print the JSON string representation of the object
print UnreadChannel.to_json()

# convert the object into a dict
unread_channel_dict = unread_channel_instance.to_dict()
# create an instance of UnreadChannel from a dict
unread_channel_form_dict = unread_channel.from_dict(unread_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


