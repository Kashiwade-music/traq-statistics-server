# Message

メッセージ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | メッセージUUID | 
**user_id** | **str** | 投稿者UUID | 
**channel_id** | **str** | チャンネルUUID | 
**content** | **str** | メッセージ本文 | 
**created_at** | **datetime** | 投稿日時 | 
**updated_at** | **datetime** | 編集日時 | 
**pinned** | **bool** | ピン留めされているかどうか | 
**stamps** | [**List[MessageStamp]**](MessageStamp.md) | 押されているスタンプの配列 | 
**thread_id** | **str** | スレッドUUID | 

## Example

```python
from traq.models.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print Message.to_json()

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_form_dict = message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


