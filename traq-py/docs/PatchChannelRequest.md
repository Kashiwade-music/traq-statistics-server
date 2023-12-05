# PatchChannelRequest

チャンネル情報変更リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | チャンネル名 | [optional] 
**archived** | **bool** | アーカイブされているかどうか | [optional] 
**force** | **bool** | 強制通知チャンネルかどうか | [optional] 
**parent** | **str** | 親チャンネルUUID | [optional] 

## Example

```python
from traq.models.patch_channel_request import PatchChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchChannelRequest from a JSON string
patch_channel_request_instance = PatchChannelRequest.from_json(json)
# print the JSON string representation of the object
print PatchChannelRequest.to_json()

# convert the object into a dict
patch_channel_request_dict = patch_channel_request_instance.to_dict()
# create an instance of PatchChannelRequest from a dict
patch_channel_request_form_dict = patch_channel_request.from_dict(patch_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


