# PatchChannelSubscribersRequest

チャンネル購読者編集リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on** | **List[str]** | 通知をオンにするユーザーのUUID配列 | [optional] 
**off** | **List[str]** | 通知をオフにするユーザーのUUID配列 | [optional] 

## Example

```python
from traq.models.patch_channel_subscribers_request import PatchChannelSubscribersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchChannelSubscribersRequest from a JSON string
patch_channel_subscribers_request_instance = PatchChannelSubscribersRequest.from_json(json)
# print the JSON string representation of the object
print PatchChannelSubscribersRequest.to_json()

# convert the object into a dict
patch_channel_subscribers_request_dict = patch_channel_subscribers_request_instance.to_dict()
# create an instance of PatchChannelSubscribersRequest from a dict
patch_channel_subscribers_request_form_dict = patch_channel_subscribers_request.from_dict(patch_channel_subscribers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


