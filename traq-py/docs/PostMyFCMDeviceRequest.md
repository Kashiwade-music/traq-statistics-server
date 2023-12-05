# PostMyFCMDeviceRequest

FCMデバイス登録リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | FCMのデバイストークン | 

## Example

```python
from traq.models.post_my_fcm_device_request import PostMyFCMDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostMyFCMDeviceRequest from a JSON string
post_my_fcm_device_request_instance = PostMyFCMDeviceRequest.from_json(json)
# print the JSON string representation of the object
print PostMyFCMDeviceRequest.to_json()

# convert the object into a dict
post_my_fcm_device_request_dict = post_my_fcm_device_request_instance.to_dict()
# create an instance of PostMyFCMDeviceRequest from a dict
post_my_fcm_device_request_form_dict = post_my_fcm_device_request.from_dict(post_my_fcm_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


