# MessageClip

メッセージクリップ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** | クリップされているフォルダのID | 
**clipped_at** | **datetime** | クリップされた日時 | 

## Example

```python
from traq.models.message_clip import MessageClip

# TODO update the JSON string below
json = "{}"
# create an instance of MessageClip from a JSON string
message_clip_instance = MessageClip.from_json(json)
# print the JSON string representation of the object
print MessageClip.to_json()

# convert the object into a dict
message_clip_dict = message_clip_instance.to_dict()
# create an instance of MessageClip from a dict
message_clip_form_dict = message_clip.from_dict(message_clip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


