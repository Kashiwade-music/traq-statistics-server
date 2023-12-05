# traq.StampApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_message_stamp**](StampApi.md#add_message_stamp) | **POST** /messages/{messageId}/stamps/{stampId} | スタンプを押す
[**change_stamp_image**](StampApi.md#change_stamp_image) | **PUT** /stamps/{stampId}/image | スタンプ画像を変更
[**create_stamp**](StampApi.md#create_stamp) | **POST** /stamps | スタンプを作成
[**create_stamp_palette**](StampApi.md#create_stamp_palette) | **POST** /stamp-palettes | スタンプパレットを作成
[**delete_stamp**](StampApi.md#delete_stamp) | **DELETE** /stamps/{stampId} | スタンプを削除
[**delete_stamp_palette**](StampApi.md#delete_stamp_palette) | **DELETE** /stamp-palettes/{paletteId} | スタンプパレットを削除
[**edit_stamp**](StampApi.md#edit_stamp) | **PATCH** /stamps/{stampId} | スタンプ情報を変更
[**edit_stamp_palette**](StampApi.md#edit_stamp_palette) | **PATCH** /stamp-palettes/{paletteId} | スタンプパレットを編集
[**get_message_stamps**](StampApi.md#get_message_stamps) | **GET** /messages/{messageId}/stamps | メッセージのスタンプリストを取得
[**get_my_stamp_history**](StampApi.md#get_my_stamp_history) | **GET** /users/me/stamp-history | スタンプ履歴を取得
[**get_stamp**](StampApi.md#get_stamp) | **GET** /stamps/{stampId} | スタンプ情報を取得
[**get_stamp_image**](StampApi.md#get_stamp_image) | **GET** /stamps/{stampId}/image | スタンプ画像を取得
[**get_stamp_palette**](StampApi.md#get_stamp_palette) | **GET** /stamp-palettes/{paletteId} | スタンプパレットを取得
[**get_stamp_palettes**](StampApi.md#get_stamp_palettes) | **GET** /stamp-palettes | スタンプパレットのリストを取得
[**get_stamp_stats**](StampApi.md#get_stamp_stats) | **GET** /stamps/{stampId}/stats | スタンプ統計情報を取得
[**get_stamps**](StampApi.md#get_stamps) | **GET** /stamps | スタンプリストを取得
[**remove_message_stamp**](StampApi.md#remove_message_stamp) | **DELETE** /messages/{messageId}/stamps/{stampId} | スタンプを消す


# **add_message_stamp**
> add_message_stamp(message_id, stamp_id, post_message_stamp_request=post_message_stamp_request)

スタンプを押す

指定したメッセージに指定したスタンプを押します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.post_message_stamp_request import PostMessageStampRequest
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
    api_instance = traq.StampApi(api_client)
    message_id = 'message_id_example' # str | メッセージUUID
    stamp_id = 'stamp_id_example' # str | スタンプUUID
    post_message_stamp_request = traq.PostMessageStampRequest() # PostMessageStampRequest |  (optional)

    try:
        # スタンプを押す
        api_instance.add_message_stamp(message_id, stamp_id, post_message_stamp_request=post_message_stamp_request)
    except Exception as e:
        print("Exception when calling StampApi->add_message_stamp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID | 
 **stamp_id** | **str**| スタンプUUID | 
 **post_message_stamp_request** | [**PostMessageStampRequest**](PostMessageStampRequest.md)|  | [optional] 

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
**204** | No Content スタンプを押すことができました。 |  -  |
**400** | Bad Request |  -  |
**404** | Not Found メッセージ、またはスタンプが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_stamp_image**
> change_stamp_image(stamp_id, file)

スタンプ画像を変更

指定したスタンプの画像を変更します。

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
    api_instance = traq.StampApi(api_client)
    stamp_id = 'stamp_id_example' # str | スタンプUUID
    file = None # bytearray | スタンプ画像(1MBまでのpng, jpeg, gif)

    try:
        # スタンプ画像を変更
        api_instance.change_stamp_image(stamp_id, file)
    except Exception as e:
        print("Exception when calling StampApi->change_stamp_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stamp_id** | **str**| スタンプUUID | 
 **file** | **bytearray**| スタンプ画像(1MBまでのpng, jpeg, gif) | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**413** | Request Entity Too Large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stamp**
> Stamp create_stamp(name, file)

スタンプを作成

スタンプを新規作成します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.stamp import Stamp
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
    api_instance = traq.StampApi(api_client)
    name = 'name_example' # str | スタンプ名
    file = None # bytearray | スタンプ画像(1MBまでのpng, jpeg, gif)

    try:
        # スタンプを作成
        api_response = api_instance.create_stamp(name, file)
        print("The response of StampApi->create_stamp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StampApi->create_stamp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| スタンプ名 | 
 **file** | **bytearray**| スタンプ画像(1MBまでのpng, jpeg, gif) | 

### Return type

[**Stamp**](Stamp.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**413** | Request Entity Too Large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stamp_palette**
> StampPalette create_stamp_palette(post_stamp_palette_request=post_stamp_palette_request)

スタンプパレットを作成

スタンプパレットを作成します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.post_stamp_palette_request import PostStampPaletteRequest
from traq.models.stamp_palette import StampPalette
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
    api_instance = traq.StampApi(api_client)
    post_stamp_palette_request = traq.PostStampPaletteRequest() # PostStampPaletteRequest |  (optional)

    try:
        # スタンプパレットを作成
        api_response = api_instance.create_stamp_palette(post_stamp_palette_request=post_stamp_palette_request)
        print("The response of StampApi->create_stamp_palette:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StampApi->create_stamp_palette: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_stamp_palette_request** | [**PostStampPaletteRequest**](PostStampPaletteRequest.md)|  | [optional] 

### Return type

[**StampPalette**](StampPalette.md)

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

# **delete_stamp**
> delete_stamp(stamp_id)

スタンプを削除

指定したスタンプを削除します。 対象のスタンプの削除権限が必要です。

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
    api_instance = traq.StampApi(api_client)
    stamp_id = 'stamp_id_example' # str | スタンプUUID

    try:
        # スタンプを削除
        api_instance.delete_stamp(stamp_id)
    except Exception as e:
        print("Exception when calling StampApi->delete_stamp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stamp_id** | **str**| スタンプUUID | 

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
**204** | No Content スタンプが削除されました。 |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stamp_palette**
> delete_stamp_palette(palette_id)

スタンプパレットを削除

指定したスタンプパレットを削除します。 対象のスタンプパレットの管理権限が必要です。

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
    api_instance = traq.StampApi(api_client)
    palette_id = 'palette_id_example' # str | スタンプパレットUUID

    try:
        # スタンプパレットを削除
        api_instance.delete_stamp_palette(palette_id)
    except Exception as e:
        print("Exception when calling StampApi->delete_stamp_palette: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **palette_id** | **str**| スタンプパレットUUID | 

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
**403** | Forbidden 対象のスタンプパレットを削除する権限がありません。 |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_stamp**
> edit_stamp(stamp_id, patch_stamp_request=patch_stamp_request)

スタンプ情報を変更

指定したスタンプの情報を変更します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.patch_stamp_request import PatchStampRequest
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
    api_instance = traq.StampApi(api_client)
    stamp_id = 'stamp_id_example' # str | スタンプUUID
    patch_stamp_request = traq.PatchStampRequest() # PatchStampRequest |  (optional)

    try:
        # スタンプ情報を変更
        api_instance.edit_stamp(stamp_id, patch_stamp_request=patch_stamp_request)
    except Exception as e:
        print("Exception when calling StampApi->edit_stamp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stamp_id** | **str**| スタンプUUID | 
 **patch_stamp_request** | [**PatchStampRequest**](PatchStampRequest.md)|  | [optional] 

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
**204** | No Content スタンプ情報が変更されました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_stamp_palette**
> edit_stamp_palette(palette_id, patch_stamp_palette_request=patch_stamp_palette_request)

スタンプパレットを編集

指定したスタンプパレットを編集します。 リクエストのスタンプの配列の順番は保存されて変更されます。 対象のスタンプパレットの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.patch_stamp_palette_request import PatchStampPaletteRequest
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
    api_instance = traq.StampApi(api_client)
    palette_id = 'palette_id_example' # str | スタンプパレットUUID
    patch_stamp_palette_request = traq.PatchStampPaletteRequest() # PatchStampPaletteRequest |  (optional)

    try:
        # スタンプパレットを編集
        api_instance.edit_stamp_palette(palette_id, patch_stamp_palette_request=patch_stamp_palette_request)
    except Exception as e:
        print("Exception when calling StampApi->edit_stamp_palette: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **palette_id** | **str**| スタンプパレットUUID | 
 **patch_stamp_palette_request** | [**PatchStampPaletteRequest**](PatchStampPaletteRequest.md)|  | [optional] 

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
**204** | No Content 変更しました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden 対象のスタンプパレットを編集する権限がありません。 |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_stamps**
> List[MessageStamp] get_message_stamps(message_id)

メッセージのスタンプリストを取得

指定したメッセージに押されているスタンプのリストを取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.message_stamp import MessageStamp
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
    api_instance = traq.StampApi(api_client)
    message_id = 'message_id_example' # str | メッセージUUID

    try:
        # メッセージのスタンプリストを取得
        api_response = api_instance.get_message_stamps(message_id)
        print("The response of StampApi->get_message_stamps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StampApi->get_message_stamps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID | 

### Return type

[**List[MessageStamp]**](MessageStamp.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_stamp_history**
> List[StampHistoryEntry] get_my_stamp_history(limit=limit)

スタンプ履歴を取得

自分のスタンプ履歴を最大100件まで取得します。 結果は降順で返されます。  このAPIが返すスタンプ履歴は厳密な履歴ではありません。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.stamp_history_entry import StampHistoryEntry
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
    api_instance = traq.StampApi(api_client)
    limit = 100 # int | 件数 (optional) (default to 100)

    try:
        # スタンプ履歴を取得
        api_response = api_instance.get_my_stamp_history(limit=limit)
        print("The response of StampApi->get_my_stamp_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StampApi->get_my_stamp_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 件数 | [optional] [default to 100]

### Return type

[**List[StampHistoryEntry]**](StampHistoryEntry.md)

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

# **get_stamp**
> Stamp get_stamp(stamp_id)

スタンプ情報を取得

指定したスタンプの情報を取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.stamp import Stamp
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
    api_instance = traq.StampApi(api_client)
    stamp_id = 'stamp_id_example' # str | スタンプUUID

    try:
        # スタンプ情報を取得
        api_response = api_instance.get_stamp(stamp_id)
        print("The response of StampApi->get_stamp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StampApi->get_stamp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stamp_id** | **str**| スタンプUUID | 

### Return type

[**Stamp**](Stamp.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stamp_image**
> bytearray get_stamp_image(stamp_id)

スタンプ画像を取得

指定したIDのスタンプ画像を返します。

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
    api_instance = traq.StampApi(api_client)
    stamp_id = 'stamp_id_example' # str | スタンプUUID

    try:
        # スタンプ画像を取得
        api_response = api_instance.get_stamp_image(stamp_id)
        print("The response of StampApi->get_stamp_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StampApi->get_stamp_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stamp_id** | **str**| スタンプUUID | 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/gif, image/jpeg

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stamp_palette**
> StampPalette get_stamp_palette(palette_id)

スタンプパレットを取得

指定したスタンプパレットの情報を取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.stamp_palette import StampPalette
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
    api_instance = traq.StampApi(api_client)
    palette_id = 'palette_id_example' # str | スタンプパレットUUID

    try:
        # スタンプパレットを取得
        api_response = api_instance.get_stamp_palette(palette_id)
        print("The response of StampApi->get_stamp_palette:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StampApi->get_stamp_palette: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **palette_id** | **str**| スタンプパレットUUID | 

### Return type

[**StampPalette**](StampPalette.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stamp_palettes**
> List[StampPalette] get_stamp_palettes()

スタンプパレットのリストを取得

自身が所有しているスタンプパレットのリストを取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.stamp_palette import StampPalette
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
    api_instance = traq.StampApi(api_client)

    try:
        # スタンプパレットのリストを取得
        api_response = api_instance.get_stamp_palettes()
        print("The response of StampApi->get_stamp_palettes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StampApi->get_stamp_palettes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[StampPalette]**](StampPalette.md)

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

# **get_stamp_stats**
> StampStats get_stamp_stats(stamp_id)

スタンプ統計情報を取得

指定したスタンプの統計情報を取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.stamp_stats import StampStats
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
    api_instance = traq.StampApi(api_client)
    stamp_id = 'stamp_id_example' # str | スタンプUUID

    try:
        # スタンプ統計情報を取得
        api_response = api_instance.get_stamp_stats(stamp_id)
        print("The response of StampApi->get_stamp_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StampApi->get_stamp_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stamp_id** | **str**| スタンプUUID | 

### Return type

[**StampStats**](StampStats.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found スタンプが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stamps**
> List[Stamp] get_stamps(include_unicode=include_unicode, type=type)

スタンプリストを取得

スタンプのリストを取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.stamp import Stamp
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
    api_instance = traq.StampApi(api_client)
    include_unicode = True # bool | Unicode絵文字を含ませるかどうか Deprecated: typeクエリを指定しなければ全てのスタンプを取得できるため、そちらを利用してください  (optional) (default to True)
    type = 'type_example' # str | 取得するスタンプの種類 (optional)

    try:
        # スタンプリストを取得
        api_response = api_instance.get_stamps(include_unicode=include_unicode, type=type)
        print("The response of StampApi->get_stamps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StampApi->get_stamps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_unicode** | **bool**| Unicode絵文字を含ませるかどうか Deprecated: typeクエリを指定しなければ全てのスタンプを取得できるため、そちらを利用してください  | [optional] [default to True]
 **type** | **str**| 取得するスタンプの種類 | [optional] 

### Return type

[**List[Stamp]**](Stamp.md)

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

# **remove_message_stamp**
> remove_message_stamp(message_id, stamp_id)

スタンプを消す

指定したメッセージから指定した自身が押したスタンプを削除します。

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
    api_instance = traq.StampApi(api_client)
    message_id = 'message_id_example' # str | メッセージUUID
    stamp_id = 'stamp_id_example' # str | スタンプUUID

    try:
        # スタンプを消す
        api_instance.remove_message_stamp(message_id, stamp_id)
    except Exception as e:
        print("Exception when calling StampApi->remove_message_stamp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| メッセージUUID | 
 **stamp_id** | **str**| スタンプUUID | 

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
**204** | No Content スタンプを消すことができました。 |  -  |
**404** | Not Found メッセージ、またはスタンプが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

