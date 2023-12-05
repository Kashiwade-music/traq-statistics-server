# PostWebRTCAuthenticateRequest

skyway用認証リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer_id** | **str** | ピアID | 

## Example

```python
from traq.models.post_web_rtc_authenticate_request import PostWebRTCAuthenticateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostWebRTCAuthenticateRequest from a JSON string
post_web_rtc_authenticate_request_instance = PostWebRTCAuthenticateRequest.from_json(json)
# print the JSON string representation of the object
print PostWebRTCAuthenticateRequest.to_json()

# convert the object into a dict
post_web_rtc_authenticate_request_dict = post_web_rtc_authenticate_request_instance.to_dict()
# create an instance of PostWebRTCAuthenticateRequest from a dict
post_web_rtc_authenticate_request_form_dict = post_web_rtc_authenticate_request.from_dict(post_web_rtc_authenticate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


