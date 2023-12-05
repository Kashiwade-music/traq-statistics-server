# ChannelTopic

チャンネルトピック

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | トピック | 

## Example

```python
from traq.models.channel_topic import ChannelTopic

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelTopic from a JSON string
channel_topic_instance = ChannelTopic.from_json(json)
# print the JSON string representation of the object
print ChannelTopic.to_json()

# convert the object into a dict
channel_topic_dict = channel_topic_instance.to_dict()
# create an instance of ChannelTopic from a dict
channel_topic_form_dict = channel_topic.from_dict(channel_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


