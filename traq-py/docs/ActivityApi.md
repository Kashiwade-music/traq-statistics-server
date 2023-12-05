# traq.ActivityApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activity_timeline**](ActivityApi.md#get_activity_timeline) | **GET** /activity/timeline | アクテビティタイムラインを取得
[**get_online_users**](ActivityApi.md#get_online_users) | **GET** /activity/onlines | オンラインユーザーリストを取得


# **get_activity_timeline**
> List[ActivityTimelineMessage] get_activity_timeline(limit=limit, all=all, per_channel=per_channel)

アクテビティタイムラインを取得

パブリックチャンネルの直近の投稿メッセージを作成日時の降順で取得します。 `all`が`true`でない場合、購読チャンネルのみのタイムラインを取得します

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.activity_timeline_message import ActivityTimelineMessage
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
    api_instance = traq.ActivityApi(api_client)
    limit = 50 # int | 取得する件数 (optional) (default to 50)
    all = False # bool | 全てのチャンネルのタイムラインを取得する (optional) (default to False)
    per_channel = False # bool | 同じチャンネルのメッセージは最新のもののみ取得するか (optional) (default to False)

    try:
        # アクテビティタイムラインを取得
        api_response = api_instance.get_activity_timeline(limit=limit, all=all, per_channel=per_channel)
        print("The response of ActivityApi->get_activity_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activity_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得する件数 | [optional] [default to 50]
 **all** | **bool**| 全てのチャンネルのタイムラインを取得する | [optional] [default to False]
 **per_channel** | **bool**| 同じチャンネルのメッセージは最新のもののみ取得するか | [optional] [default to False]

### Return type

[**List[ActivityTimelineMessage]**](ActivityTimelineMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_online_users**
> List[str] get_online_users()

オンラインユーザーリストを取得

現在オンラインな(SSEまたはWSが接続中)ユーザーのUUIDのリストを返します。

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
    api_instance = traq.ActivityApi(api_client)

    try:
        # オンラインユーザーリストを取得
        api_response = api_instance.get_online_users()
        print("The response of ActivityApi->get_online_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_online_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

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

