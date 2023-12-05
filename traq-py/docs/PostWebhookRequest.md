# PostWebhookRequest

Webhook作成リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Webhookユーザーの表示名 | 
**description** | **str** | 説明 | 
**channel_id** | **str** | デフォルトの投稿先チャンネルUUID | 
**secret** | **str** | Webhookシークレット | 

## Example

```python
from traq.models.post_webhook_request import PostWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostWebhookRequest from a JSON string
post_webhook_request_instance = PostWebhookRequest.from_json(json)
# print the JSON string representation of the object
print PostWebhookRequest.to_json()

# convert the object into a dict
post_webhook_request_dict = post_webhook_request_instance.to_dict()
# create an instance of PostWebhookRequest from a dict
post_webhook_request_form_dict = post_webhook_request.from_dict(post_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


