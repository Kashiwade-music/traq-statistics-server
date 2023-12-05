# PatchStampPaletteRequest

スタンプパレット情報変更リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | パレット名 | [optional] 
**description** | **str** | 説明 | [optional] 
**stamps** | **List[str]** | パレット内のスタンプUUIDの配列 | [optional] 

## Example

```python
from traq.models.patch_stamp_palette_request import PatchStampPaletteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchStampPaletteRequest from a JSON string
patch_stamp_palette_request_instance = PatchStampPaletteRequest.from_json(json)
# print the JSON string representation of the object
print PatchStampPaletteRequest.to_json()

# convert the object into a dict
patch_stamp_palette_request_dict = patch_stamp_palette_request_instance.to_dict()
# create an instance of PatchStampPaletteRequest from a dict
patch_stamp_palette_request_form_dict = patch_stamp_palette_request.from_dict(patch_stamp_palette_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


