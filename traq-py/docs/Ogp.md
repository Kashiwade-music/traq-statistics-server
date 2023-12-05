# Ogp

OGPの情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**url** | **str** |  | 
**images** | [**List[OgpMedia]**](OgpMedia.md) |  | 
**description** | **str** |  | 
**videos** | [**List[OgpMedia]**](OgpMedia.md) |  | 

## Example

```python
from traq.models.ogp import Ogp

# TODO update the JSON string below
json = "{}"
# create an instance of Ogp from a JSON string
ogp_instance = Ogp.from_json(json)
# print the JSON string representation of the object
print Ogp.to_json()

# convert the object into a dict
ogp_dict = ogp_instance.to_dict()
# create an instance of Ogp from a dict
ogp_form_dict = ogp.from_dict(ogp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


