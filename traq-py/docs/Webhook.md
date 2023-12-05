# Webhook

Webhook情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | WebhookUUID | 
**bot_user_id** | **str** | WebhookユーザーUUID | 
**display_name** | **str** | Webhookユーザー表示名 | 
**description** | **str** | 説明 | 
**secure** | **bool** | セキュアWebhookかどうか | 
**channel_id** | **str** | デフォルトの投稿先チャンネルUUID | 
**owner_id** | **str** | オーナーUUID | 
**created_at** | **datetime** | 作成日時 | 
**updated_at** | **datetime** | 更新日時 | 

## Example

```python
from traq.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print Webhook.to_json()

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_form_dict = webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


