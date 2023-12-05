# ThumbnailInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ThumbnailType**](ThumbnailType.md) |  | 
**mime** | **str** | MIMEタイプ | 
**width** | **int** | サムネイル幅 | [optional] 
**height** | **int** | サムネイル高さ | [optional] 

## Example

```python
from traq.models.thumbnail_info import ThumbnailInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ThumbnailInfo from a JSON string
thumbnail_info_instance = ThumbnailInfo.from_json(json)
# print the JSON string representation of the object
print ThumbnailInfo.to_json()

# convert the object into a dict
thumbnail_info_dict = thumbnail_info_instance.to_dict()
# create an instance of ThumbnailInfo from a dict
thumbnail_info_form_dict = thumbnail_info.from_dict(thumbnail_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


