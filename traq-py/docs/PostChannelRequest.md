# PostChannelRequest

チャンネル作成リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | チャンネル名 | 
**parent** | **str** | 親チャンネルのUUID ルートに作成する場合はnullを指定 | 

## Example

```python
from traq.models.post_channel_request import PostChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostChannelRequest from a JSON string
post_channel_request_instance = PostChannelRequest.from_json(json)
# print the JSON string representation of the object
print PostChannelRequest.to_json()

# convert the object into a dict
post_channel_request_dict = post_channel_request_instance.to_dict()
# create an instance of PostChannelRequest from a dict
post_channel_request_form_dict = post_channel_request.from_dict(post_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


