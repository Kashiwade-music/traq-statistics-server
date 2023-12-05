# traq.FileApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](FileApi.md#delete_file) | **DELETE** /files/{fileId} | ファイルを削除
[**get_file**](FileApi.md#get_file) | **GET** /files/{fileId} | ファイルをダウンロード
[**get_file_meta**](FileApi.md#get_file_meta) | **GET** /files/{fileId}/meta | ファイルメタを取得
[**get_files**](FileApi.md#get_files) | **GET** /files | ファイルメタのリストを取得
[**get_thumbnail_image**](FileApi.md#get_thumbnail_image) | **GET** /files/{fileId}/thumbnail | サムネイル画像を取得
[**post_file**](FileApi.md#post_file) | **POST** /files | ファイルをアップロード


# **delete_file**
> delete_file(file_id)

ファイルを削除

指定したファイルを削除します。 指定したファイルの削除権限が必要です。

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
    api_instance = traq.FileApi(api_client)
    file_id = 'file_id_example' # str | ファイルUUID

    try:
        # ファイルを削除
        api_instance.delete_file(file_id)
    except Exception as e:
        print("Exception when calling FileApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| ファイルUUID | 

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
**204** | No Content ファイルが削除できました。 |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> bytearray get_file(file_id, dl=dl)

ファイルをダウンロード

指定したファイル本体を取得します。 指定したファイルへのアクセス権限が必要です。

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
    api_instance = traq.FileApi(api_client)
    file_id = 'file_id_example' # str | ファイルUUID
    dl = 56 # int | 1を指定するとレスポンスにContent-Dispositionヘッダーが付与されます (optional)

    try:
        # ファイルをダウンロード
        api_response = api_instance.get_file(file_id, dl=dl)
        print("The response of FileApi->get_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->get_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| ファイルUUID | 
 **dl** | **int**| 1を指定するとレスポンスにContent-Dispositionヘッダーが付与されます | [optional] 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK ファイル本体を返します。 application/octet-streamで返すことになっていますが、ファイルの形式によって変わります。 |  * Content-Disposition - https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Content-Disposition <br>  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_meta**
> FileInfo get_file_meta(file_id)

ファイルメタを取得

指定したファイルのメタ情報を取得します。 指定したファイルへのアクセス権限が必要です。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.file_info import FileInfo
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
    api_instance = traq.FileApi(api_client)
    file_id = 'file_id_example' # str | ファイルUUID

    try:
        # ファイルメタを取得
        api_response = api_instance.get_file_meta(file_id)
        print("The response of FileApi->get_file_meta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->get_file_meta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| ファイルUUID | 

### Return type

[**FileInfo**](FileInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found ファイルが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> List[FileInfo] get_files(channel_id=channel_id, limit=limit, offset=offset, since=since, until=until, inclusive=inclusive, order=order, mine=mine)

ファイルメタのリストを取得

指定したクエリでファイルメタのリストを取得します。 クエリパラメータ`channelId`, `mine`の少なくともいずれかが必須です。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.file_info import FileInfo
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
    api_instance = traq.FileApi(api_client)
    channel_id = 'channel_id_example' # str | アップロード先チャンネルUUID (optional)
    limit = 50 # int | 取得する件数 (optional)
    offset = 0 # int | 取得するオフセット (optional) (default to 0)
    since = '2016-10-12T11:00:00.000000Z' # datetime | 取得する時間範囲の開始日時 (optional)
    until = '2016-10-12T11:00:00.0000000Z' # datetime | 取得する時間範囲の終了日時 (optional)
    inclusive = False # bool | 範囲の端を含めるかどうか (optional) (default to False)
    order = 'desc' # str | 昇順か降順か (optional) (default to 'desc')
    mine = False # bool | アップロード者が自分のファイルのみを取得するか (optional) (default to False)

    try:
        # ファイルメタのリストを取得
        api_response = api_instance.get_files(channel_id=channel_id, limit=limit, offset=offset, since=since, until=until, inclusive=inclusive, order=order, mine=mine)
        print("The response of FileApi->get_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->get_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| アップロード先チャンネルUUID | [optional] 
 **limit** | **int**| 取得する件数 | [optional] 
 **offset** | **int**| 取得するオフセット | [optional] [default to 0]
 **since** | **datetime**| 取得する時間範囲の開始日時 | [optional] 
 **until** | **datetime**| 取得する時間範囲の終了日時 | [optional] 
 **inclusive** | **bool**| 範囲の端を含めるかどうか | [optional] [default to False]
 **order** | **str**| 昇順か降順か | [optional] [default to &#39;desc&#39;]
 **mine** | **bool**| アップロード者が自分のファイルのみを取得するか | [optional] [default to False]

### Return type

[**List[FileInfo]**](FileInfo.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_image**
> bytearray get_thumbnail_image(file_id, type=type)

サムネイル画像を取得

指定したファイルのサムネイル画像を取得します。 指定したファイルへのアクセス権限が必要です。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.thumbnail_type import ThumbnailType
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
    api_instance = traq.FileApi(api_client)
    file_id = 'file_id_example' # str | ファイルUUID
    type = traq.ThumbnailType() # ThumbnailType | 取得するサムネイルのタイプ (optional)

    try:
        # サムネイル画像を取得
        api_response = api_instance.get_thumbnail_image(file_id, type=type)
        print("The response of FileApi->get_thumbnail_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->get_thumbnail_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| ファイルUUID | 
 **type** | [**ThumbnailType**](.md)| 取得するサムネイルのタイプ | [optional] 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/jpeg

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found ファイルが見つからない、またはサムネイル画像が存在しません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_file**
> FileInfo post_file(file, channel_id)

ファイルをアップロード

指定したチャンネルにファイルをアップロードします。 アーカイブされているチャンネルにはアップロード出来ません。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.file_info import FileInfo
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
    api_instance = traq.FileApi(api_client)
    file = None # bytearray | ファイル本体
    channel_id = 'channel_id_example' # str | アップロード先チャンネルUUID

    try:
        # ファイルをアップロード
        api_response = api_instance.post_file(file, channel_id)
        print("The response of FileApi->post_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->post_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| ファイル本体 | 
 **channel_id** | **str**| アップロード先チャンネルUUID | 

### Return type

[**FileInfo**](FileInfo.md)

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
**411** | Length Required |  -  |
**413** | Request Entity Too Large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

