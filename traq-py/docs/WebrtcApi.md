# traq.WebrtcApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_web_rtc_state**](WebrtcApi.md#get_web_rtc_state) | **GET** /webrtc/state | WebRTC状態を取得
[**post_web_rtc_authenticate**](WebrtcApi.md#post_web_rtc_authenticate) | **POST** /webrtc/authenticate | Skyway用認証API


# **get_web_rtc_state**
> List[WebRTCUserState] get_web_rtc_state()

WebRTC状態を取得

現在のWebRTC状態を取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.web_rtc_user_state import WebRTCUserState
from traq.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://q.trap.jp/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = traq.Configuration(
    host = "https://q.trap.jp/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: bearerAuth
configuration = traq.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with traq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = traq.WebrtcApi(api_client)

    try:
        # WebRTC状態を取得
        api_response = api_instance.get_web_rtc_state()
        print("The response of WebrtcApi->get_web_rtc_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebrtcApi->get_web_rtc_state: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WebRTCUserState]**](WebRTCUserState.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_web_rtc_authenticate**
> WebRTCAuthenticateResult post_web_rtc_authenticate(post_web_rtc_authenticate_request=post_web_rtc_authenticate_request)

Skyway用認証API

Skyway WebRTC用の認証API

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.post_web_rtc_authenticate_request import PostWebRTCAuthenticateRequest
from traq.models.web_rtc_authenticate_result import WebRTCAuthenticateResult
from traq.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://q.trap.jp/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = traq.Configuration(
    host = "https://q.trap.jp/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: bearerAuth
configuration = traq.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with traq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = traq.WebrtcApi(api_client)
    post_web_rtc_authenticate_request = traq.PostWebRTCAuthenticateRequest() # PostWebRTCAuthenticateRequest |  (optional)

    try:
        # Skyway用認証API
        api_response = api_instance.post_web_rtc_authenticate(post_web_rtc_authenticate_request=post_web_rtc_authenticate_request)
        print("The response of WebrtcApi->post_web_rtc_authenticate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebrtcApi->post_web_rtc_authenticate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_web_rtc_authenticate_request** | [**PostWebRTCAuthenticateRequest**](PostWebRTCAuthenticateRequest.md)|  | [optional] 

### Return type

[**WebRTCAuthenticateResult**](WebRTCAuthenticateResult.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**503** | Service Unavailable WebRTCは現在機能を停止しています |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

