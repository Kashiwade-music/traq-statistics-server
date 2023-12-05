# PostUserTagRequest

ユーザータグ追加リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | タグ文字列 | 

## Example

```python
from traq.models.post_user_tag_request import PostUserTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUserTagRequest from a JSON string
post_user_tag_request_instance = PostUserTagRequest.from_json(json)
# print the JSON string representation of the object
print PostUserTagRequest.to_json()

# convert the object into a dict
post_user_tag_request_dict = post_user_tag_request_instance.to_dict()
# create an instance of PostUserTagRequest from a dict
post_user_tag_request_form_dict = post_user_tag_request.from_dict(post_user_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


