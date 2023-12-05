# UserStatsStamp

ユーザーの特定スタンプ統計情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | スタンプID | 
**count** | **int** | スタンプ数(同一メッセージ上のものは複数カウントしない) | 
**total** | **int** | スタンプ数(同一メッセージ上のものも複数カウントする) | 

## Example

```python
from traq.models.user_stats_stamp import UserStatsStamp

# TODO update the JSON string below
json = "{}"
# create an instance of UserStatsStamp from a JSON string
user_stats_stamp_instance = UserStatsStamp.from_json(json)
# print the JSON string representation of the object
print UserStatsStamp.to_json()

# convert the object into a dict
user_stats_stamp_dict = user_stats_stamp_instance.to_dict()
# create an instance of UserStatsStamp from a dict
user_stats_stamp_form_dict = user_stats_stamp.from_dict(user_stats_stamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


