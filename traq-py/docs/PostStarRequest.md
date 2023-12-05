# PostStarRequest

スター追加リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | チャンネルUUID | 

## Example

```python
from traq.models.post_star_request import PostStarRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostStarRequest from a JSON string
post_star_request_instance = PostStarRequest.from_json(json)
# print the JSON string representation of the object
print PostStarRequest.to_json()

# convert the object into a dict
post_star_request_dict = post_star_request_instance.to_dict()
# create an instance of PostStarRequest from a dict
post_star_request_form_dict = post_star_request.from_dict(post_star_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


