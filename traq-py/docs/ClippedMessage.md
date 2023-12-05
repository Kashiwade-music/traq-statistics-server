# ClippedMessage

クリップされたメッセージ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**Message**](Message.md) |  | 
**clipped_at** | **datetime** | クリップした日時 | 

## Example

```python
from traq.models.clipped_message import ClippedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ClippedMessage from a JSON string
clipped_message_instance = ClippedMessage.from_json(json)
# print the JSON string representation of the object
print ClippedMessage.to_json()

# convert the object into a dict
clipped_message_dict = clipped_message_instance.to_dict()
# create an instance of ClippedMessage from a dict
clipped_message_form_dict = clipped_message.from_dict(clipped_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


