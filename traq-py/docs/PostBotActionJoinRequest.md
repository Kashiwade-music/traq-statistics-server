# PostBotActionJoinRequest

BOTチャンネル参加リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | チャンネルUUID | 

## Example

```python
from traq.models.post_bot_action_join_request import PostBotActionJoinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostBotActionJoinRequest from a JSON string
post_bot_action_join_request_instance = PostBotActionJoinRequest.from_json(json)
# print the JSON string representation of the object
print PostBotActionJoinRequest.to_json()

# convert the object into a dict
post_bot_action_join_request_dict = post_bot_action_join_request_instance.to_dict()
# create an instance of PostBotActionJoinRequest from a dict
post_bot_action_join_request_form_dict = post_bot_action_join_request.from_dict(post_bot_action_join_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


