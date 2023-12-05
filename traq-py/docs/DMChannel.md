# DMChannel

ダイレクトメッセージチャンネル

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | チャンネルUUID | 
**user_id** | **str** | 送信先相手のUUID | 

## Example

```python
from traq.models.dm_channel import DMChannel

# TODO update the JSON string below
json = "{}"
# create an instance of DMChannel from a JSON string
dm_channel_instance = DMChannel.from_json(json)
# print the JSON string representation of the object
print DMChannel.to_json()

# convert the object into a dict
dm_channel_dict = dm_channel_instance.to_dict()
# create an instance of DMChannel from a dict
dm_channel_form_dict = dm_channel.from_dict(dm_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


