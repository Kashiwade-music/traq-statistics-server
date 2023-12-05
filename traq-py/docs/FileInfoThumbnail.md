# FileInfoThumbnail

サムネイル情報 サムネイルが存在しない場合はnullになります Deprecated: thumbnailsを参照してください

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime** | **str** | MIMEタイプ | 
**width** | **int** | サムネイル幅 | [optional] 
**height** | **int** | サムネイル高さ | [optional] 

## Example

```python
from traq.models.file_info_thumbnail import FileInfoThumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of FileInfoThumbnail from a JSON string
file_info_thumbnail_instance = FileInfoThumbnail.from_json(json)
# print the JSON string representation of the object
print FileInfoThumbnail.to_json()

# convert the object into a dict
file_info_thumbnail_dict = file_info_thumbnail_instance.to_dict()
# create an instance of FileInfoThumbnail from a dict
file_info_thumbnail_form_dict = file_info_thumbnail.from_dict(file_info_thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


