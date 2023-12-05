# PostStampPaletteRequest

スタンプパレット作成リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stamps** | **List[str]** | パレット内のスタンプのUUID配列 | 
**name** | **str** | パレット名 | 
**description** | **str** | 説明 | 

## Example

```python
from traq.models.post_stamp_palette_request import PostStampPaletteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostStampPaletteRequest from a JSON string
post_stamp_palette_request_instance = PostStampPaletteRequest.from_json(json)
# print the JSON string representation of the object
print PostStampPaletteRequest.to_json()

# convert the object into a dict
post_stamp_palette_request_dict = post_stamp_palette_request_instance.to_dict()
# create an instance of PostStampPaletteRequest from a dict
post_stamp_palette_request_form_dict = post_stamp_palette_request.from_dict(post_stamp_palette_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


