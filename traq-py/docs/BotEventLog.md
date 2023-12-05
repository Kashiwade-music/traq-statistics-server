# BotEventLog

BOTイベントログ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_id** | **str** | BOT UUID | 
**request_id** | **str** | リクエストUUID | 
**event** | **str** | イベントタイプ | 
**result** | [**BotEventResult**](BotEventResult.md) |  | [optional] 
**code** | **int** | ステータスコード | 
**datetime** | **datetime** | イベント日時 | 

## Example

```python
from traq.models.bot_event_log import BotEventLog

# TODO update the JSON string below
json = "{}"
# create an instance of BotEventLog from a JSON string
bot_event_log_instance = BotEventLog.from_json(json)
# print the JSON string representation of the object
print BotEventLog.to_json()

# convert the object into a dict
bot_event_log_dict = bot_event_log_instance.to_dict()
# create an instance of BotEventLog from a dict
bot_event_log_form_dict = bot_event_log.from_dict(bot_event_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


