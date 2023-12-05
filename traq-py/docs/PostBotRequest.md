# PostBotRequest

BOT作成リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | BOTユーザーID 自動的に接頭辞\&quot;BOT_\&quot;が付与されます | 
**display_name** | **str** | BOTユーザー表示名 | 
**description** | **str** | BOTの説明 | 
**mode** | [**BotMode**](BotMode.md) |  | 
**endpoint** | **str** | BOTサーバーエンドポイント BOT動作モードがHTTPの場合必須です | [optional] 

## Example

```python
from traq.models.post_bot_request import PostBotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostBotRequest from a JSON string
post_bot_request_instance = PostBotRequest.from_json(json)
# print the JSON string representation of the object
print PostBotRequest.to_json()

# convert the object into a dict
post_bot_request_dict = post_bot_request_instance.to_dict()
# create an instance of PostBotRequest from a dict
post_bot_request_form_dict = post_bot_request.from_dict(post_bot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


