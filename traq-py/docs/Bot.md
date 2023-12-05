# Bot

BOT情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | BOT UUID | 
**bot_user_id** | **str** | BOTユーザーUUID | 
**description** | **str** | 説明 | 
**developer_id** | **str** | BOT開発者UUID | 
**subscribe_events** | **List[str]** | BOTが購読しているイベントの配列 | 
**mode** | [**BotMode**](BotMode.md) |  | 
**state** | [**BotState**](BotState.md) |  | 
**created_at** | **datetime** | 作成日時 | 
**updated_at** | **datetime** | 更新日時 | 

## Example

```python
from traq.models.bot import Bot

# TODO update the JSON string below
json = "{}"
# create an instance of Bot from a JSON string
bot_instance = Bot.from_json(json)
# print the JSON string representation of the object
print Bot.to_json()

# convert the object into a dict
bot_dict = bot_instance.to_dict()
# create an instance of Bot from a dict
bot_form_dict = bot.from_dict(bot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


