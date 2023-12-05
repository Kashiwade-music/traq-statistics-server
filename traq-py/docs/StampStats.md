# StampStats

スタンプ統計情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | スタンプ使用総数(同じユーザによって同じメッセージに貼られたものは複数カウントしない) | 
**total_count** | **int** | スタンプ使用総数(全てカウント) | 

## Example

```python
from traq.models.stamp_stats import StampStats

# TODO update the JSON string below
json = "{}"
# create an instance of StampStats from a JSON string
stamp_stats_instance = StampStats.from_json(json)
# print the JSON string representation of the object
print StampStats.to_json()

# convert the object into a dict
stamp_stats_dict = stamp_stats_instance.to_dict()
# create an instance of StampStats from a dict
stamp_stats_form_dict = stamp_stats.from_dict(stamp_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


