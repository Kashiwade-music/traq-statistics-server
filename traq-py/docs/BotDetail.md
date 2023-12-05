# BotDetail

BOT詳細情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | BOT UUID | 
**updated_at** | **datetime** | 更新日時 | 
**created_at** | **datetime** | 作成日時 | 
**mode** | [**BotMode**](BotMode.md) |  | 
**state** | [**BotState**](BotState.md) |  | 
**subscribe_events** | **List[str]** | BOTが購読しているイベントの配列 | 
**developer_id** | **str** | BOT開発者UUID | 
**description** | **str** | 説明 | 
**bot_user_id** | **str** | BOTユーザーUUID | 
**tokens** | [**BotTokens**](BotTokens.md) |  | 
**endpoint** | **str** | BOTサーバーエンドポイント | 
**privileged** | **bool** | 特権BOTかどうか | 
**channels** | **List[str]** | BOTが参加しているチャンネルのUUID配列 | 

## Example

```python
from traq.models.bot_detail import BotDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BotDetail from a JSON string
bot_detail_instance = BotDetail.from_json(json)
# print the JSON string representation of the object
print BotDetail.to_json()

# convert the object into a dict
bot_detail_dict = bot_detail_instance.to_dict()
# create an instance of BotDetail from a dict
bot_detail_form_dict = bot_detail.from_dict(bot_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


