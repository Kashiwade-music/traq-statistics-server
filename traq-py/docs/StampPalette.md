# StampPalette

スタンプパレット情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | スタンプパレットUUID | 
**name** | **str** | パレット名 | 
**stamps** | **List[str]** | パレット内のスタンプのUUID配列 | 
**creator_id** | **str** | 作成者UUID | 
**created_at** | **datetime** | パレット作成日時 | 
**updated_at** | **datetime** | パレット更新日時 | 
**description** | **str** | パレット説明 | 

## Example

```python
from traq.models.stamp_palette import StampPalette

# TODO update the JSON string below
json = "{}"
# create an instance of StampPalette from a JSON string
stamp_palette_instance = StampPalette.from_json(json)
# print the JSON string representation of the object
print StampPalette.to_json()

# convert the object into a dict
stamp_palette_dict = stamp_palette_instance.to_dict()
# create an instance of StampPalette from a dict
stamp_palette_form_dict = stamp_palette.from_dict(stamp_palette_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


