# PatchClientRequest

OAuth2クライアント情報変更リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | クライアント名 | [optional] 
**description** | **str** | 説明 | [optional] 
**callback_url** | **str** | コールバックURL | [optional] 
**developer_id** | **str** | クライアント開発者UUID | [optional] 

## Example

```python
from traq.models.patch_client_request import PatchClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchClientRequest from a JSON string
patch_client_request_instance = PatchClientRequest.from_json(json)
# print the JSON string representation of the object
print PatchClientRequest.to_json()

# convert the object into a dict
patch_client_request_dict = patch_client_request_instance.to_dict()
# create an instance of PatchClientRequest from a dict
patch_client_request_form_dict = patch_client_request.from_dict(patch_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


