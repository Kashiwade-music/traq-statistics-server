# MessageSearchResult

メッセージ検索結果

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_hits** | **int** | 検索にヒットしたメッセージ件数 | 
**hits** | [**List[Message]**](Message.md) | 検索にヒットしたメッセージの配列 | 

## Example

```python
from traq.models.message_search_result import MessageSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSearchResult from a JSON string
message_search_result_instance = MessageSearchResult.from_json(json)
# print the JSON string representation of the object
print MessageSearchResult.to_json()

# convert the object into a dict
message_search_result_dict = message_search_result_instance.to_dict()
# create an instance of MessageSearchResult from a dict
message_search_result_form_dict = message_search_result.from_dict(message_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


