# ChannelStatsUser

チャンネル上の特定ユーザー統計情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ユーザーID | 
**message_count** | **int** | メッセージ数 | 

## Example

```python
from traq.models.channel_stats_user import ChannelStatsUser

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelStatsUser from a JSON string
channel_stats_user_instance = ChannelStatsUser.from_json(json)
# print the JSON string representation of the object
print ChannelStatsUser.to_json()

# convert the object into a dict
channel_stats_user_dict = channel_stats_user_instance.to_dict()
# create an instance of ChannelStatsUser from a dict
channel_stats_user_form_dict = channel_stats_user.from_dict(channel_stats_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


