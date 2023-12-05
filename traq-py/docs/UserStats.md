# UserStats

ユーザー統計情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_message_count** | **int** | ユーザーの総投稿メッセージ数(削除されたものも含む) | 
**stamps** | [**List[UserStatsStamp]**](UserStatsStamp.md) | ユーザーのスタンプ統計情報 | 
**datetime** | **datetime** | 統計情報日時 | 

## Example

```python
from traq.models.user_stats import UserStats

# TODO update the JSON string below
json = "{}"
# create an instance of UserStats from a JSON string
user_stats_instance = UserStats.from_json(json)
# print the JSON string representation of the object
print UserStats.to_json()

# convert the object into a dict
user_stats_dict = user_stats_instance.to_dict()
# create an instance of UserStats from a dict
user_stats_form_dict = user_stats.from_dict(user_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


