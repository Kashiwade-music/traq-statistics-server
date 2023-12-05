# GetBot200Response


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
**tokens** | [**BotTokens**](BotTokens.md) |  | 
**endpoint** | **str** | BOTサーバーエンドポイント | 
**privileged** | **bool** | 特権BOTかどうか | 
**channels** | **List[str]** | BOTが参加しているチャンネルのUUID配列 | 

## Example

```python
from traq.models.get_bot200_response import GetBot200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBot200Response from a JSON string
get_bot200_response_instance = GetBot200Response.from_json(json)
# print the JSON string representation of the object
print GetBot200Response.to_json()

# convert the object into a dict
get_bot200_response_dict = get_bot200_response_instance.to_dict()
# create an instance of GetBot200Response from a dict
get_bot200_response_form_dict = get_bot200_response.from_dict(get_bot200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


