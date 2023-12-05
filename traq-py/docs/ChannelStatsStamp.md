# ChannelStatsStamp

チャンネル上の特定スタンプ統計情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | スタンプID | 
**count** | **int** | スタンプ数(同一メッセージ上のものは複数カウントしない) | 
**total** | **int** | スタンプ数(同一メッセージ上のものも複数カウントする) | 

## Example

```python
from traq.models.channel_stats_stamp import ChannelStatsStamp

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelStatsStamp from a JSON string
channel_stats_stamp_instance = ChannelStatsStamp.from_json(json)
# print the JSON string representation of the object
print ChannelStatsStamp.to_json()

# convert the object into a dict
channel_stats_stamp_dict = channel_stats_stamp_instance.to_dict()
# create an instance of ChannelStatsStamp from a dict
channel_stats_stamp_form_dict = channel_stats_stamp.from_dict(channel_stats_stamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


