# FileInfo

ファイル情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ファイルUUID | 
**name** | **str** | ファイル名 | 
**mime** | **str** | MIMEタイプ | 
**size** | **int** | ファイルサイズ | 
**md5** | **str** | MD5ハッシュ | 
**is_animated_image** | **bool** | アニメーション画像かどうか | 
**created_at** | **datetime** | アップロード日時 | 
**thumbnails** | [**List[ThumbnailInfo]**](ThumbnailInfo.md) |  | 
**thumbnail** | [**FileInfoThumbnail**](FileInfoThumbnail.md) |  | 
**channel_id** | **str** | 属しているチャンネルUUID | 
**uploader_id** | **str** | アップロード者UUID | 

## Example

```python
from traq.models.file_info import FileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FileInfo from a JSON string
file_info_instance = FileInfo.from_json(json)
# print the JSON string representation of the object
print FileInfo.to_json()

# convert the object into a dict
file_info_dict = file_info_instance.to_dict()
# create an instance of FileInfo from a dict
file_info_form_dict = file_info.from_dict(file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


