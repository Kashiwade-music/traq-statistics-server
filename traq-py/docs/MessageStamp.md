# MessageStamp

メッセージに押されたスタンプ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ユーザーUUID | 
**stamp_id** | **str** | スタンプUUID | 
**count** | **int** | スタンプ数 | 
**created_at** | **datetime** | スタンプが最初に押された日時 | 
**updated_at** | **datetime** | スタンプが最後に押された日時 | 

## Example

```python
from traq.models.message_stamp import MessageStamp

# TODO update the JSON string below
json = "{}"
# create an instance of MessageStamp from a JSON string
message_stamp_instance = MessageStamp.from_json(json)
# print the JSON string representation of the object
print MessageStamp.to_json()

# convert the object into a dict
message_stamp_dict = message_stamp_instance.to_dict()
# create an instance of MessageStamp from a dict
message_stamp_form_dict = message_stamp.from_dict(message_stamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


