# traq.ClipApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clip_message**](ClipApi.md#clip_message) | **POST** /clip-folders/{folderId}/messages | メッセージをクリップフォルダに追加
[**create_clip_folder**](ClipApi.md#create_clip_folder) | **POST** /clip-folders | クリップフォルダを作成
[**delete_clip_folder**](ClipApi.md#delete_clip_folder) | **DELETE** /clip-folders/{folderId} | クリップフォルダを削除
[**edit_clip_folder**](ClipApi.md#edit_clip_folder) | **PATCH** /clip-folders/{folderId} | クリップフォルダ情報を編集
[**get_clip_folder**](ClipApi.md#get_clip_folder) | **GET** /clip-folders/{folderId} | クリップフォルダ情報を取得
[**get_clip_folders**](ClipApi.md#get_clip_folders) | **GET** /clip-folders | クリップフォルダのリストを取得
[**get_clips**](ClipApi.md#get_clips) | **GET** /clip-folders/{folderId}/messages | フォルダ内のクリップのリストを取得
[**get_message_clips**](ClipApi.md#get_message_clips) | **GET** /messages/{messageId}/clips | 自分のクリップを取得
[**unclip_message**](ClipApi.md#unclip_message) | **DELETE** /clip-folders/{folderId}/messages/{messageId} | メッセージをクリップフォルダから除外


# **clip_message**
> ClippedMessage clip_message(folder_id, post_clip_folder_message_request=post_clip_folder_message_request)

メッセージをクリップフォルダに追加

指定したメッセージを指定したクリップフォルダに追加します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.clipped_message import ClippedMessage
from traq.models.post_clip_folder_message_request import PostClipFolderMessageRequest
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
    api_instance = traq.ClipApi(api_client)
    folder_id = 'folder_id_example' # str | クリップフォルダUUID
    post_clip_folder_message_request = traq.PostClipFolderMessageRequest() # PostClipFolderMessageRequest |  (optional)

    try:
        # メッセージをクリップフォルダに追加
        api_response = api_instance.clip_message(folder_id, post_clip_folder_message_request=post_clip_folder_message_request)
        print("The response of ClipApi->clip_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClipApi->clip_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID | 
 **post_clip_folder_message_request** | [**PostClipFolderMessageRequest**](PostClipFolderMessageRequest.md)|  | [optional] 

### Return type

[**ClippedMessage**](ClippedMessage.md)

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
**404** | Not Found クリップフォルダが見つかりません。 |  -  |
**409** | Conflict 既に追加されています。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clip_folder**
> ClipFolder create_clip_folder(post_clip_folder_request=post_clip_folder_request)

クリップフォルダを作成

クリップフォルダを作成します。 既にあるフォルダと同名のフォルダを作成することは可能です。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.clip_folder import ClipFolder
from traq.models.post_clip_folder_request import PostClipFolderRequest
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
    api_instance = traq.ClipApi(api_client)
    post_clip_folder_request = traq.PostClipFolderRequest() # PostClipFolderRequest |  (optional)

    try:
        # クリップフォルダを作成
        api_response = api_instance.create_clip_folder(post_clip_folder_request=post_clip_folder_request)
        print("The response of ClipApi->create_clip_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClipApi->create_clip_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_clip_folder_request** | [**PostClipFolderRequest**](PostClipFolderRequest.md)|  | [optional] 

### Return type

[**ClipFolder**](ClipFolder.md)

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

# **delete_clip_folder**
> delete_clip_folder(folder_id)

クリップフォルダを削除

指定したクリップフォルダを削除します。

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
    api_instance = traq.ClipApi(api_client)
    folder_id = 'folder_id_example' # str | クリップフォルダUUID

    try:
        # クリップフォルダを削除
        api_instance.delete_clip_folder(folder_id)
    except Exception as e:
        print("Exception when calling ClipApi->delete_clip_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID | 

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
**204** | No Content 削除しました。 |  -  |
**404** | Not Found クリップフォルダが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_clip_folder**
> edit_clip_folder(folder_id, patch_clip_folder_request=patch_clip_folder_request)

クリップフォルダ情報を編集

指定したクリップフォルダの情報を編集します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.patch_clip_folder_request import PatchClipFolderRequest
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
    api_instance = traq.ClipApi(api_client)
    folder_id = 'folder_id_example' # str | クリップフォルダUUID
    patch_clip_folder_request = traq.PatchClipFolderRequest() # PatchClipFolderRequest |  (optional)

    try:
        # クリップフォルダ情報を編集
        api_instance.edit_clip_folder(folder_id, patch_clip_folder_request=patch_clip_folder_request)
    except Exception as e:
        print("Exception when calling ClipApi->edit_clip_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID | 
 **patch_clip_folder_request** | [**PatchClipFolderRequest**](PatchClipFolderRequest.md)|  | [optional] 

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
**204** | No Content 編集しました。 |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clip_folder**
> ClipFolder get_clip_folder(folder_id)

クリップフォルダ情報を取得

指定したクリップフォルダの情報を取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.clip_folder import ClipFolder
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
    api_instance = traq.ClipApi(api_client)
    folder_id = 'folder_id_example' # str | クリップフォルダUUID

    try:
        # クリップフォルダ情報を取得
        api_response = api_instance.get_clip_folder(folder_id)
        print("The response of ClipApi->get_clip_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClipApi->get_clip_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID | 

### Return type

[**ClipFolder**](ClipFolder.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found クリップフォルダが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clip_folders**
> List[ClipFolder] get_clip_folders()

クリップフォルダのリストを取得

自身が所有するクリップフォルダのリストを取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.clip_folder import ClipFolder
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
    api_instance = traq.ClipApi(api_client)

    try:
        # クリップフォルダのリストを取得
        api_response = api_instance.get_clip_folders()
        print("The response of ClipApi->get_clip_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClipApi->get_clip_folders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ClipFolder]**](ClipFolder.md)

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

# **get_clips**
> List[ClippedMessage] get_clips(folder_id, limit=limit, offset=offset, order=order)

フォルダ内のクリップのリストを取得

指定したフォルダ内のクリップのリストを取得します。 `order`を指定しない場合、クリップした日時の新しい順で返されます。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.clipped_message import ClippedMessage
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
    api_instance = traq.ClipApi(api_client)
    folder_id = 'folder_id_example' # str | クリップフォルダUUID
    limit = 50 # int | 取得する件数 (optional)
    offset = 0 # int | 取得するオフセット (optional) (default to 0)
    order = 'desc' # str | 昇順か降順か (optional) (default to 'desc')

    try:
        # フォルダ内のクリップのリストを取得
        api_response = api_instance.get_clips(folder_id, limit=limit, offset=offset, order=order)
        print("The response of ClipApi->get_clips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClipApi->get_clips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID | 
 **limit** | **int**| 取得する件数 | [optional] 
 **offset** | **int**| 取得するオフセット | [optional] [default to 0]
 **order** | **str**| 昇順か降順か | [optional] [default to &#39;desc&#39;]

### Return type

[**List[ClippedMessage]**](ClippedMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found クリップフォルダが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_clips**
> List[MessageClip] get_message_clips(message_id)

自分のクリップを取得

対象のメッセージの自分のクリップの一覧を返します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.message_clip import MessageClip
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
    api_instance = traq.ClipApi(api_client)
    message_id = 'message_id_example' # str | メッセージUUID

    try:
        # 自分のクリップを取得
        api_response = api_instance.get_message_clips(message_id)
        print("The response of ClipApi->get_message_clips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClipApi->get_message_clips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID | 

### Return type

[**List[MessageClip]**](MessageClip.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unclip_message**
> unclip_message(folder_id, message_id)

メッセージをクリップフォルダから除外

指定したフォルダから指定したメッセージのクリップを除外します。 既に外されているメッセージを指定した場合は204を返します。

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
    api_instance = traq.ClipApi(api_client)
    folder_id = 'folder_id_example' # str | クリップフォルダUUID
    message_id = 'message_id_example' # str | メッセージUUID

    try:
        # メッセージをクリップフォルダから除外
        api_instance.unclip_message(folder_id, message_id)
    except Exception as e:
        print("Exception when calling ClipApi->unclip_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| クリップフォルダUUID | 
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
**204** | No Content 外しました。 |  -  |
**404** | Not Found クリップフォルダが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

