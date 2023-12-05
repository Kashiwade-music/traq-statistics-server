# PatchUserTagRequest

ユーザーのタグの編集リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_locked** | **bool** | タグのロック状態 | 

## Example

```python
from traq.models.patch_user_tag_request import PatchUserTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchUserTagRequest from a JSON string
patch_user_tag_request_instance = PatchUserTagRequest.from_json(json)
# print the JSON string representation of the object
print PatchUserTagRequest.to_json()

# convert the object into a dict
patch_user_tag_request_dict = patch_user_tag_request_instance.to_dict()
# create an instance of PatchUserTagRequest from a dict
patch_user_tag_request_form_dict = patch_user_tag_request.from_dict(patch_user_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


