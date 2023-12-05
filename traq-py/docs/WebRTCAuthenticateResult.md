# WebRTCAuthenticateResult

skyway用認証リクエストリザルト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer_id** | **str** | ピアID | 
**ttl** | **int** | TTL | 
**timestamp** | **int** | タイムスタンプ | 
**auth_token** | **str** | 認証トークン | 

## Example

```python
from traq.models.web_rtc_authenticate_result import WebRTCAuthenticateResult

# TODO update the JSON string below
json = "{}"
# create an instance of WebRTCAuthenticateResult from a JSON string
web_rtc_authenticate_result_instance = WebRTCAuthenticateResult.from_json(json)
# print the JSON string representation of the object
print WebRTCAuthenticateResult.to_json()

# convert the object into a dict
web_rtc_authenticate_result_dict = web_rtc_authenticate_result_instance.to_dict()
# create an instance of WebRTCAuthenticateResult from a dict
web_rtc_authenticate_result_form_dict = web_rtc_authenticate_result.from_dict(web_rtc_authenticate_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


