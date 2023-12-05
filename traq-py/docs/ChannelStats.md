# ChannelStats

チャンネル統計情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_message_count** | **int** | チャンネルの総投稿メッセージ数(削除されたものも含む) | 
**stamps** | [**List[ChannelStatsStamp]**](ChannelStatsStamp.md) | チャンネル上のスタンプ統計情報 | 
**users** | [**List[ChannelStatsUser]**](ChannelStatsUser.md) | チャンネル上のユーザー統計情報 | 
**datetime** | **datetime** | 統計情報日時 | 

## Example

```python
from traq.models.channel_stats import ChannelStats

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelStats from a JSON string
channel_stats_instance = ChannelStats.from_json(json)
# print the JSON string representation of the object
print ChannelStats.to_json()

# convert the object into a dict
channel_stats_dict = channel_stats_instance.to_dict()
# create an instance of ChannelStats from a dict
channel_stats_form_dict = channel_stats.from_dict(channel_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


