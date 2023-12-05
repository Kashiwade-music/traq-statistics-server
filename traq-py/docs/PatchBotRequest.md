# PatchBotRequest

BOT情報変更リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | BOTユーザー表示名 | [optional] 
**description** | **str** | BOTの説明 | [optional] 
**privileged** | **bool** | 特権 | [optional] 
**mode** | [**BotMode**](BotMode.md) |  | [optional] 
**endpoint** | **str** | BOTサーバーエンドポイント | [optional] 
**developer_id** | **str** | 移譲先の開発者UUID | [optional] 
**subscribe_events** | **List[str]** | 購読するイベント | [optional] 

## Example

```python
from traq.models.patch_bot_request import PatchBotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchBotRequest from a JSON string
patch_bot_request_instance = PatchBotRequest.from_json(json)
# print the JSON string representation of the object
print PatchBotRequest.to_json()

# convert the object into a dict
patch_bot_request_dict = patch_bot_request_instance.to_dict()
# create an instance of PatchBotRequest from a dict
patch_bot_request_form_dict = patch_bot_request.from_dict(patch_bot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


