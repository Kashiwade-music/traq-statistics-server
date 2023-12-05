# PatchClipFolderRequest

クリップフォルダ情報編集リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | フォルダ名 | [optional] 
**description** | **str** | 説明 | [optional] 

## Example

```python
from traq.models.patch_clip_folder_request import PatchClipFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchClipFolderRequest from a JSON string
patch_clip_folder_request_instance = PatchClipFolderRequest.from_json(json)
# print the JSON string representation of the object
print PatchClipFolderRequest.to_json()

# convert the object into a dict
patch_clip_folder_request_dict = patch_clip_folder_request_instance.to_dict()
# create an instance of PatchClipFolderRequest from a dict
patch_clip_folder_request_form_dict = patch_clip_folder_request.from_dict(patch_clip_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


