# Stamp

スタンプ情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | スタンプUUID | 
**name** | **str** | スタンプ名 | 
**creator_id** | **str** | 作成者UUID | 
**created_at** | **datetime** | 作成日時 | 
**updated_at** | **datetime** | 更新日時 | 
**file_id** | **str** | ファイルUUID | 
**is_unicode** | **bool** | Unicode絵文字か | 

## Example

```python
from traq.models.stamp import Stamp

# TODO update the JSON string below
json = "{}"
# create an instance of Stamp from a JSON string
stamp_instance = Stamp.from_json(json)
# print the JSON string representation of the object
print Stamp.to_json()

# convert the object into a dict
stamp_dict = stamp_instance.to_dict()
# create an instance of Stamp from a dict
stamp_form_dict = stamp.from_dict(stamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


