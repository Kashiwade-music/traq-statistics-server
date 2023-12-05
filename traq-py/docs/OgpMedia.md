# OgpMedia

OGPに含まれる画像の情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**secure_url** | **str** |  | 
**type** | **str** |  | 
**width** | **int** |  | 
**height** | **int** |  | 

## Example

```python
from traq.models.ogp_media import OgpMedia

# TODO update the JSON string below
json = "{}"
# create an instance of OgpMedia from a JSON string
ogp_media_instance = OgpMedia.from_json(json)
# print the JSON string representation of the object
print OgpMedia.to_json()

# convert the object into a dict
ogp_media_dict = ogp_media_instance.to_dict()
# create an instance of OgpMedia from a dict
ogp_media_form_dict = ogp_media.from_dict(ogp_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


