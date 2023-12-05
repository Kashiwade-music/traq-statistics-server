# GetNotifyCitation

メッセージ引用通知の設定情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notify_citation** | **bool** |  | 

## Example

```python
from traq.models.get_notify_citation import GetNotifyCitation

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotifyCitation from a JSON string
get_notify_citation_instance = GetNotifyCitation.from_json(json)
# print the JSON string representation of the object
print GetNotifyCitation.to_json()

# convert the object into a dict
get_notify_citation_dict = get_notify_citation_instance.to_dict()
# create an instance of GetNotifyCitation from a dict
get_notify_citation_form_dict = get_notify_citation.from_dict(get_notify_citation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


