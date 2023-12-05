# ClipFolder

クリップフォルダ情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | フォルダUUID | 
**name** | **str** | フォルダ名 | 
**created_at** | **datetime** | 作成日時 | 
**owner_id** | **str** | フォルダ所有者UUID | 
**description** | **str** | 説明 | 

## Example

```python
from traq.models.clip_folder import ClipFolder

# TODO update the JSON string below
json = "{}"
# create an instance of ClipFolder from a JSON string
clip_folder_instance = ClipFolder.from_json(json)
# print the JSON string representation of the object
print ClipFolder.to_json()

# convert the object into a dict
clip_folder_dict = clip_folder_instance.to_dict()
# create an instance of ClipFolder from a dict
clip_folder_form_dict = clip_folder.from_dict(clip_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


