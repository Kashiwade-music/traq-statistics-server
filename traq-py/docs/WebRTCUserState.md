# WebRTCUserState

WebRTC状態

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ユーザーUUID | 
**channel_id** | **str** | チャンネルUUID | 
**sessions** | [**List[WebRTCUserStateSessionsInner]**](WebRTCUserStateSessionsInner.md) | セッションの配列 | 

## Example

```python
from traq.models.web_rtc_user_state import WebRTCUserState

# TODO update the JSON string below
json = "{}"
# create an instance of WebRTCUserState from a JSON string
web_rtc_user_state_instance = WebRTCUserState.from_json(json)
# print the JSON string representation of the object
print WebRTCUserState.to_json()

# convert the object into a dict
web_rtc_user_state_dict = web_rtc_user_state_instance.to_dict()
# create an instance of WebRTCUserState from a dict
web_rtc_user_state_form_dict = web_rtc_user_state.from_dict(web_rtc_user_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


