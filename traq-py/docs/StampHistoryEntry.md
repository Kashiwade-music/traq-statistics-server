# StampHistoryEntry

スタンプ履歴の1項目

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stamp_id** | **str** | スタンプUUID | 
**datetime** | **datetime** | 使用日時 | 

## Example

```python
from traq.models.stamp_history_entry import StampHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StampHistoryEntry from a JSON string
stamp_history_entry_instance = StampHistoryEntry.from_json(json)
# print the JSON string representation of the object
print StampHistoryEntry.to_json()

# convert the object into a dict
stamp_history_entry_dict = stamp_history_entry_instance.to_dict()
# create an instance of StampHistoryEntry from a dict
stamp_history_entry_form_dict = stamp_history_entry.from_dict(stamp_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


