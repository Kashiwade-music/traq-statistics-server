# MyChannelViewState

自身のチャンネル閲覧状態

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | WSセッションの識別子 | 
**channel_id** | **str** | チャンネルUUID | 
**state** | [**ChannelViewState**](ChannelViewState.md) |  | 

## Example

```python
from traq.models.my_channel_view_state import MyChannelViewState

# TODO update the JSON string below
json = "{}"
# create an instance of MyChannelViewState from a JSON string
my_channel_view_state_instance = MyChannelViewState.from_json(json)
# print the JSON string representation of the object
print MyChannelViewState.to_json()

# convert the object into a dict
my_channel_view_state_dict = my_channel_view_state_instance.to_dict()
# create an instance of MyChannelViewState from a dict
my_channel_view_state_form_dict = my_channel_view_state.from_dict(my_channel_view_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


