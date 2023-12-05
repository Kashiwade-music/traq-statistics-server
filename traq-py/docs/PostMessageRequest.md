# PostMessageRequest

メッセージ投稿リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | メッセージ本文 | 
**embed** | **bool** | メンション・チャンネルリンクを自動埋め込みするか | [optional] [default to False]

## Example

```python
from traq.models.post_message_request import PostMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostMessageRequest from a JSON string
post_message_request_instance = PostMessageRequest.from_json(json)
# print the JSON string representation of the object
print PostMessageRequest.to_json()

# convert the object into a dict
post_message_request_dict = post_message_request_instance.to_dict()
# create an instance of PostMessageRequest from a dict
post_message_request_form_dict = post_message_request.from_dict(post_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


