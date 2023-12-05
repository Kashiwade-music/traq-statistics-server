# PutChannelSubscribeLevelRequest

チャンネル購読レベル変更リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**ChannelSubscribeLevel**](ChannelSubscribeLevel.md) |  | 

## Example

```python
from traq.models.put_channel_subscribe_level_request import PutChannelSubscribeLevelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutChannelSubscribeLevelRequest from a JSON string
put_channel_subscribe_level_request_instance = PutChannelSubscribeLevelRequest.from_json(json)
# print the JSON string representation of the object
print PutChannelSubscribeLevelRequest.to_json()

# convert the object into a dict
put_channel_subscribe_level_request_dict = put_channel_subscribe_level_request_instance.to_dict()
# create an instance of PutChannelSubscribeLevelRequest from a dict
put_channel_subscribe_level_request_form_dict = put_channel_subscribe_level_request.from_dict(put_channel_subscribe_level_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


