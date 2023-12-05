# Pin

ピン情報(メッセージ本体付き)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ピン留めしたユーザーUUID | 
**pinned_at** | **datetime** | ピン留めされた日時 | 
**message** | [**Message**](Message.md) |  | 

## Example

```python
from traq.models.pin import Pin

# TODO update the JSON string below
json = "{}"
# create an instance of Pin from a JSON string
pin_instance = Pin.from_json(json)
# print the JSON string representation of the object
print Pin.to_json()

# convert the object into a dict
pin_dict = pin_instance.to_dict()
# create an instance of Pin from a dict
pin_form_dict = pin.from_dict(pin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


