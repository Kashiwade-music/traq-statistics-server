# PostMessageStampRequest

スタンプを押すリクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | 押す数 | 

## Example

```python
from traq.models.post_message_stamp_request import PostMessageStampRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostMessageStampRequest from a JSON string
post_message_stamp_request_instance = PostMessageStampRequest.from_json(json)
# print the JSON string representation of the object
print PostMessageStampRequest.to_json()

# convert the object into a dict
post_message_stamp_request_dict = post_message_stamp_request_instance.to_dict()
# create an instance of PostMessageStampRequest from a dict
post_message_stamp_request_form_dict = post_message_stamp_request.from_dict(post_message_stamp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


