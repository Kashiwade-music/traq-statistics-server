# PatchWebhookRequest

Webhook情報変更リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Webhookユーザー表示名 | [optional] 
**description** | **str** | 説明 | [optional] 
**channel_id** | **str** | デフォルトの投稿先チャンネルUUID | [optional] 
**secret** | **str** | Webhookシークレット | [optional] 
**owner_id** | **str** | 移譲先のユーザーUUID | [optional] 

## Example

```python
from traq.models.patch_webhook_request import PatchWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchWebhookRequest from a JSON string
patch_webhook_request_instance = PatchWebhookRequest.from_json(json)
# print the JSON string representation of the object
print PatchWebhookRequest.to_json()

# convert the object into a dict
patch_webhook_request_dict = patch_webhook_request_instance.to_dict()
# create an instance of PatchWebhookRequest from a dict
patch_webhook_request_form_dict = patch_webhook_request.from_dict(patch_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


