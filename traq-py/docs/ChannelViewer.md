# ChannelViewer

チャンネル閲覧者情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ユーザーUUID | 
**state** | [**ChannelViewState**](ChannelViewState.md) |  | 
**updated_at** | **datetime** | 更新日時 | 

## Example

```python
from traq.models.channel_viewer import ChannelViewer

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelViewer from a JSON string
channel_viewer_instance = ChannelViewer.from_json(json)
# print the JSON string representation of the object
print ChannelViewer.to_json()

# convert the object into a dict
channel_viewer_dict = channel_viewer_instance.to_dict()
# create an instance of ChannelViewer from a dict
channel_viewer_form_dict = channel_viewer.from_dict(channel_viewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


