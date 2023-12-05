# PostClipFolderMessageRequest

クリップ追加リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | メッセージUUID | 

## Example

```python
from traq.models.post_clip_folder_message_request import PostClipFolderMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClipFolderMessageRequest from a JSON string
post_clip_folder_message_request_instance = PostClipFolderMessageRequest.from_json(json)
# print the JSON string representation of the object
print PostClipFolderMessageRequest.to_json()

# convert the object into a dict
post_clip_folder_message_request_dict = post_clip_folder_message_request_instance.to_dict()
# create an instance of PostClipFolderMessageRequest from a dict
post_clip_folder_message_request_form_dict = post_clip_folder_message_request.from_dict(post_clip_folder_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


