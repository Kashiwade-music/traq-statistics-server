# traq.WebhookApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_webhook_icon**](WebhookApi.md#change_webhook_icon) | **PUT** /webhooks/{webhookId}/icon | Webhookのアイコンを変更
[**create_webhook**](WebhookApi.md#create_webhook) | **POST** /webhooks | Webhookを新規作成
[**delete_webhook**](WebhookApi.md#delete_webhook) | **DELETE** /webhooks/{webhookId} | Webhookを削除
[**edit_webhook**](WebhookApi.md#edit_webhook) | **PATCH** /webhooks/{webhookId} | Webhook情報を変更
[**get_webhook**](WebhookApi.md#get_webhook) | **GET** /webhooks/{webhookId} | Webhook情報を取得
[**get_webhook_icon**](WebhookApi.md#get_webhook_icon) | **GET** /webhooks/{webhookId}/icon | Webhookのアイコンを取得
[**get_webhook_messages**](WebhookApi.md#get_webhook_messages) | **GET** /webhooks/{webhookId}/messages | Webhookの投稿メッセージのリストを取得
[**get_webhooks**](WebhookApi.md#get_webhooks) | **GET** /webhooks | Webhook情報のリストを取得します
[**post_webhook**](WebhookApi.md#post_webhook) | **POST** /webhooks/{webhookId} | Webhookを送信


# **change_webhook_icon**
> change_webhook_icon(webhook_id, file)

Webhookのアイコンを変更

指定したWebhookのアイコン画像を変更します。

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
    api_instance = traq.WebhookApi(api_client)
    webhook_id = 'webhook_id_example' # str | WebhookUUID
    file = None # bytearray | アイコン画像(1MBまでのpng, jpeg, gif)

    try:
        # Webhookのアイコンを変更
        api_instance.change_webhook_icon(webhook_id, file)
    except Exception as e:
        print("Exception when calling WebhookApi->change_webhook_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| WebhookUUID | 
 **file** | **bytearray**| アイコン画像(1MBまでのpng, jpeg, gif) | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content 変更されました。 |  -  |
**400** | Bad Request |  -  |
**404** | Not Found Webhookが見つかりません。 |  -  |
**413** | Request Entity Too Large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webhook**
> Webhook create_webhook(post_webhook_request=post_webhook_request)

Webhookを新規作成

Webhookを新規作成します。 `secret`が空文字の場合、insecureウェブフックが作成されます。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.post_webhook_request import PostWebhookRequest
from traq.models.webhook import Webhook
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
    api_instance = traq.WebhookApi(api_client)
    post_webhook_request = traq.PostWebhookRequest() # PostWebhookRequest |  (optional)

    try:
        # Webhookを新規作成
        api_response = api_instance.create_webhook(post_webhook_request=post_webhook_request)
        print("The response of WebhookApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_webhook_request** | [**PostWebhookRequest**](PostWebhookRequest.md)|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(webhook_id)

Webhookを削除

指定したWebhookを削除します。 Webhookによって投稿されたメッセージは削除されません。

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
    api_instance = traq.WebhookApi(api_client)
    webhook_id = 'webhook_id_example' # str | WebhookUUID

    try:
        # Webhookを削除
        api_instance.delete_webhook(webhook_id)
    except Exception as e:
        print("Exception when calling WebhookApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| WebhookUUID | 

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
**204** | No Content 削除されました。 |  -  |
**404** | Not Found Webhookが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_webhook**
> edit_webhook(webhook_id, patch_webhook_request=patch_webhook_request)

Webhook情報を変更

指定したWebhookの情報を変更します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.patch_webhook_request import PatchWebhookRequest
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
    api_instance = traq.WebhookApi(api_client)
    webhook_id = 'webhook_id_example' # str | WebhookUUID
    patch_webhook_request = traq.PatchWebhookRequest() # PatchWebhookRequest |  (optional)

    try:
        # Webhook情報を変更
        api_instance.edit_webhook(webhook_id, patch_webhook_request=patch_webhook_request)
    except Exception as e:
        print("Exception when calling WebhookApi->edit_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| WebhookUUID | 
 **patch_webhook_request** | [**PatchWebhookRequest**](PatchWebhookRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content 編集できました。 |  -  |
**400** | Bad Request |  -  |
**404** | Not Found Webhookが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> Webhook get_webhook(webhook_id)

Webhook情報を取得

指定したWebhookの詳細を取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.webhook import Webhook
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
    api_instance = traq.WebhookApi(api_client)
    webhook_id = 'webhook_id_example' # str | WebhookUUID

    try:
        # Webhook情報を取得
        api_response = api_instance.get_webhook(webhook_id)
        print("The response of WebhookApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| WebhookUUID | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found Webhookが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_icon**
> bytearray get_webhook_icon(webhook_id)

Webhookのアイコンを取得

指定したWebhookのアイコン画像を取得します

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
    api_instance = traq.WebhookApi(api_client)
    webhook_id = 'webhook_id_example' # str | WebhookUUID

    try:
        # Webhookのアイコンを取得
        api_response = api_instance.get_webhook_icon(webhook_id)
        print("The response of WebhookApi->get_webhook_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_webhook_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| WebhookUUID | 

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
**404** | Not Found Webhookが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_messages**
> List[Message] get_webhook_messages(webhook_id, limit=limit, offset=offset, since=since, until=until, inclusive=inclusive, order=order)

Webhookの投稿メッセージのリストを取得

指定されたWebhookが投稿したメッセージのリストを返します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.message import Message
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
    api_instance = traq.WebhookApi(api_client)
    webhook_id = 'webhook_id_example' # str | WebhookUUID
    limit = 50 # int | 取得する件数 (optional)
    offset = 0 # int | 取得するオフセット (optional) (default to 0)
    since = '2016-10-12T11:00:00.000000Z' # datetime | 取得する時間範囲の開始日時 (optional)
    until = '2016-10-12T11:00:00.0000000Z' # datetime | 取得する時間範囲の終了日時 (optional)
    inclusive = False # bool | 範囲の端を含めるかどうか (optional) (default to False)
    order = 'desc' # str | 昇順か降順か (optional) (default to 'desc')

    try:
        # Webhookの投稿メッセージのリストを取得
        api_response = api_instance.get_webhook_messages(webhook_id, limit=limit, offset=offset, since=since, until=until, inclusive=inclusive, order=order)
        print("The response of WebhookApi->get_webhook_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_webhook_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| WebhookUUID | 
 **limit** | **int**| 取得する件数 | [optional] 
 **offset** | **int**| 取得するオフセット | [optional] [default to 0]
 **since** | **datetime**| 取得する時間範囲の開始日時 | [optional] 
 **until** | **datetime**| 取得する時間範囲の終了日時 | [optional] 
 **inclusive** | **bool**| 範囲の端を含めるかどうか | [optional] [default to False]
 **order** | **str**| 昇順か降順か | [optional] [default to &#39;desc&#39;]

### Return type

[**List[Message]**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-TRAQ-MORE -  <br>  |
**400** | Bad Request |  -  |
**404** | Not Found Webhookが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> List[Webhook] get_webhooks(all=all)

Webhook情報のリストを取得します

Webhookのリストを取得します。 allがtrueで無い場合は、自分がオーナーのWebhookのリストを返します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.webhook import Webhook
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
    api_instance = traq.WebhookApi(api_client)
    all = False # bool | 全てのWebhookを取得します。権限が必要です。 (optional) (default to False)

    try:
        # Webhook情報のリストを取得します
        api_response = api_instance.get_webhooks(all=all)
        print("The response of WebhookApi->get_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| 全てのWebhookを取得します。権限が必要です。 | [optional] [default to False]

### Return type

[**List[Webhook]**](Webhook.md)

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

# **post_webhook**
> post_webhook(webhook_id, x_traq_signature=x_traq_signature, x_traq_channel_id=x_traq_channel_id, embed=embed, body=body)

Webhookを送信

Webhookにメッセージを投稿します。 secureなウェブフックに対しては`X-TRAQ-Signature`ヘッダーが必須です。 アーカイブされているチャンネルには投稿できません。

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
    api_instance = traq.WebhookApi(api_client)
    webhook_id = 'webhook_id_example' # str | WebhookUUID
    x_traq_signature = 'x_traq_signature_example' # str | リクエストボディシグネチャ(Secretが設定されている場合は必須) (optional)
    x_traq_channel_id = 'x_traq_channel_id_example' # str | 投稿先のチャンネルID(変更する場合) (optional)
    embed = 0 # int | メンション・チャンネルリンクを自動埋め込みする場合に1を指定する (optional) (default to 0)
    body = 'body_example' # str |  (optional)

    try:
        # Webhookを送信
        api_instance.post_webhook(webhook_id, x_traq_signature=x_traq_signature, x_traq_channel_id=x_traq_channel_id, embed=embed, body=body)
    except Exception as e:
        print("Exception when calling WebhookApi->post_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| WebhookUUID | 
 **x_traq_signature** | **str**| リクエストボディシグネチャ(Secretが設定されている場合は必須) | [optional] 
 **x_traq_channel_id** | **str**| 投稿先のチャンネルID(変更する場合) | [optional] 
 **embed** | **int**| メンション・チャンネルリンクを自動埋め込みする場合に1を指定する | [optional] [default to 0]
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

