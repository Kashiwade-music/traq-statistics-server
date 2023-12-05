# ChannelList

GET /channelsレスポンス

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public** | [**List[Channel]**](Channel.md) | パブリックチャンネルの配列 | 
**dm** | [**List[DMChannel]**](DMChannel.md) | ダイレクトメッセージチャンネルの配列 | [optional] 

## Example

```python
from traq.models.channel_list import ChannelList

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelList from a JSON string
channel_list_instance = ChannelList.from_json(json)
# print the JSON string representation of the object
print ChannelList.to_json()

# convert the object into a dict
channel_list_dict = channel_list_instance.to_dict()
# create an instance of ChannelList from a dict
channel_list_form_dict = channel_list.from_dict(channel_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


