# PostClipFolderRequest

クリップフォルダ作成リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | フォルダ名 | 
**description** | **str** | 説明 | 

## Example

```python
from traq.models.post_clip_folder_request import PostClipFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClipFolderRequest from a JSON string
post_clip_folder_request_instance = PostClipFolderRequest.from_json(json)
# print the JSON string representation of the object
print PostClipFolderRequest.to_json()

# convert the object into a dict
post_clip_folder_request_dict = post_clip_folder_request_instance.to_dict()
# create an instance of PostClipFolderRequest from a dict
post_clip_folder_request_form_dict = post_clip_folder_request.from_dict(post_clip_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


