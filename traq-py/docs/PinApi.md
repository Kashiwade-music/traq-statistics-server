# traq.PinApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pin**](PinApi.md#create_pin) | **POST** /messages/{messageId}/pin | ピン留めする
[**get_channel_pins**](PinApi.md#get_channel_pins) | **GET** /channels/{channelId}/pins | チャンネルピンのリストを取得
[**get_pin**](PinApi.md#get_pin) | **GET** /messages/{messageId}/pin | ピン留めを取得
[**remove_pin**](PinApi.md#remove_pin) | **DELETE** /messages/{messageId}/pin | ピン留めを外す


# **create_pin**
> MessagePin create_pin(message_id)

ピン留めする

指定したメッセージをピン留めします。 アーカイブされているチャンネルのメッセージ・存在しないメッセージ・チャンネル当たりの上限数を超えたメッセージのピン留めはできません。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.message_pin import MessagePin
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
    api_instance = traq.PinApi(api_client)
    message_id = 'message_id_example' # str | メッセージUUID

    try:
        # ピン留めする
        api_response = api_instance.create_pin(message_id)
        print("The response of PinApi->create_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PinApi->create_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID | 

### Return type

[**MessagePin**](MessagePin.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created 指定したメッセージがピン留めされました。 |  -  |
**400** | Bad Request |  -  |
**404** | Not Found メッセージが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_pins**
> List[Pin] get_channel_pins(channel_id)

チャンネルピンのリストを取得

指定したチャンネルにピン留めされているピンメッセージのリストを取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.pin import Pin
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
    api_instance = traq.PinApi(api_client)
    channel_id = 'channel_id_example' # str | チャンネルUUID

    try:
        # チャンネルピンのリストを取得
        api_response = api_instance.get_channel_pins(channel_id)
        print("The response of PinApi->get_channel_pins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PinApi->get_channel_pins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID | 

### Return type

[**List[Pin]**](Pin.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found チャンネルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pin**
> MessagePin get_pin(message_id)

ピン留めを取得

指定したメッセージのピン留め情報を取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.message_pin import MessagePin
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
    api_instance = traq.PinApi(api_client)
    message_id = 'message_id_example' # str | メッセージUUID

    try:
        # ピン留めを取得
        api_response = api_instance.get_pin(message_id)
        print("The response of PinApi->get_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PinApi->get_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID | 

### Return type

[**MessagePin**](MessagePin.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found 指定したメッセージ、またはピン留めが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_pin**
> remove_pin(message_id)

ピン留めを外す

指定したメッセージのピン留めを外します。

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
    api_instance = traq.PinApi(api_client)
    message_id = 'message_id_example' # str | メッセージUUID

    try:
        # ピン留めを外す
        api_instance.remove_pin(message_id)
    except Exception as e:
        print("Exception when calling PinApi->remove_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content 指定したメッセージのピン留めが外されました。 |  -  |
**400** | Bad Request |  -  |
**404** | Not Found 指定したメッセージ、またはピン留めが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

