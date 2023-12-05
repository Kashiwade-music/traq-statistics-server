# MessagePin

ピン情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ピン留めしたユーザーUUID | 
**pinned_at** | **datetime** | ピン留めされた日時 | 

## Example

```python
from traq.models.message_pin import MessagePin

# TODO update the JSON string below
json = "{}"
# create an instance of MessagePin from a JSON string
message_pin_instance = MessagePin.from_json(json)
# print the JSON string representation of the object
print MessagePin.to_json()

# convert the object into a dict
message_pin_dict = message_pin_instance.to_dict()
# create an instance of MessagePin from a dict
message_pin_form_dict = message_pin.from_dict(message_pin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


