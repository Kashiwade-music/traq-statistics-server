# PutChannelTopicRequest

チャンネルトピック編集リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | トピック | 

## Example

```python
from traq.models.put_channel_topic_request import PutChannelTopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutChannelTopicRequest from a JSON string
put_channel_topic_request_instance = PutChannelTopicRequest.from_json(json)
# print the JSON string representation of the object
print PutChannelTopicRequest.to_json()

# convert the object into a dict
put_channel_topic_request_dict = put_channel_topic_request_instance.to_dict()
# create an instance of PutChannelTopicRequest from a dict
put_channel_topic_request_form_dict = put_channel_topic_request.from_dict(put_channel_topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


