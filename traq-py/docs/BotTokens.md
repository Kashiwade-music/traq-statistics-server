# BotTokens

BOTのトークン情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_token** | **str** | Verification Token | 
**access_token** | **str** | BOTアクセストークン | 

## Example

```python
from traq.models.bot_tokens import BotTokens

# TODO update the JSON string below
json = "{}"
# create an instance of BotTokens from a JSON string
bot_tokens_instance = BotTokens.from_json(json)
# print the JSON string representation of the object
print BotTokens.to_json()

# convert the object into a dict
bot_tokens_dict = bot_tokens_instance.to_dict()
# create an instance of BotTokens from a dict
bot_tokens_form_dict = bot_tokens.from_dict(bot_tokens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


