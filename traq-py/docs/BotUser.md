# BotUser

BOTユーザー対

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | BOT UUID | 
**bot_user_id** | **str** | BOTユーザーUUID | 

## Example

```python
from traq.models.bot_user import BotUser

# TODO update the JSON string below
json = "{}"
# create an instance of BotUser from a JSON string
bot_user_instance = BotUser.from_json(json)
# print the JSON string representation of the object
print BotUser.to_json()

# convert the object into a dict
bot_user_dict = bot_user_instance.to_dict()
# create an instance of BotUser from a dict
bot_user_form_dict = bot_user.from_dict(bot_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


