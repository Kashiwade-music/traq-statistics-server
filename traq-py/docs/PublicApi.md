# traq.PublicApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_user_icon**](PublicApi.md#get_public_user_icon) | **GET** /public/icon/{username} | ユーザーのアイコン画像を取得
[**get_server_version**](PublicApi.md#get_server_version) | **GET** /version | バージョンを取得


# **get_public_user_icon**
> bytearray get_public_user_icon(username)

ユーザーのアイコン画像を取得

ユーザーのアイコン画像を取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
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
    api_instance = traq.PublicApi(api_client)
    username = 'username_example' # str | ユーザー名

    try:
        # ユーザーのアイコン画像を取得
        api_response = api_instance.get_public_user_icon(username)
        print("The response of PublicApi->get_public_user_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_public_user_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| ユーザー名 | 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, image/gif, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_version**
> Version get_server_version()

バージョンを取得

サーバーバージョン及びサーバーフラグ情報を取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.version import Version
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
    api_instance = traq.PublicApi(api_client)

    try:
        # バージョンを取得
        api_response = api_instance.get_server_version()
        print("The response of PublicApi->get_server_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_server_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

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

