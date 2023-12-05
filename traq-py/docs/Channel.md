# Channel

チャンネル

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | チャンネルUUID | 
**parent_id** | **str** | 親チャンネルUUID | 
**archived** | **bool** | チャンネルがアーカイブされているかどうか | 
**force** | **bool** | 強制通知チャンネルかどうか | 
**topic** | **str** | チャンネルトピック | 
**name** | **str** | チャンネル名 | 
**children** | **List[str]** | 子チャンネルのUUID配列 | 

## Example

```python
from traq.models.channel import Channel

# TODO update the JSON string below
json = "{}"
# create an instance of Channel from a JSON string
channel_instance = Channel.from_json(json)
# print the JSON string representation of the object
print Channel.to_json()

# convert the object into a dict
channel_dict = channel_instance.to_dict()
# create an instance of Channel from a dict
channel_form_dict = channel.from_dict(channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


