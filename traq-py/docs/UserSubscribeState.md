# UserSubscribeState

ユーザーのチャンネル購読状態

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | チャンネルUUID | 
**level** | [**ChannelSubscribeLevel**](ChannelSubscribeLevel.md) |  | 

## Example

```python
from traq.models.user_subscribe_state import UserSubscribeState

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscribeState from a JSON string
user_subscribe_state_instance = UserSubscribeState.from_json(json)
# print the JSON string representation of the object
print UserSubscribeState.to_json()

# convert the object into a dict
user_subscribe_state_dict = user_subscribe_state_instance.to_dict()
# create an instance of UserSubscribeState from a dict
user_subscribe_state_form_dict = user_subscribe_state.from_dict(user_subscribe_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


