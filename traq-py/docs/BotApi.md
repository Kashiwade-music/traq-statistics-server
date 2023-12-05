# traq.BotApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_bot**](BotApi.md#activate_bot) | **POST** /bots/{botId}/actions/activate | BOTをアクティベート
[**change_bot_icon**](BotApi.md#change_bot_icon) | **PUT** /bots/{botId}/icon | BOTのアイコン画像を変更
[**connect_bot_ws**](BotApi.md#connect_bot_ws) | **GET** /bots/ws | WebSocket Mode BOT用通知ストリームに接続します
[**create_bot**](BotApi.md#create_bot) | **POST** /bots | BOTを作成
[**delete_bot**](BotApi.md#delete_bot) | **DELETE** /bots/{botId} | BOTを削除
[**edit_bot**](BotApi.md#edit_bot) | **PATCH** /bots/{botId} | BOT情報を変更
[**get_bot**](BotApi.md#get_bot) | **GET** /bots/{botId} | BOT情報を取得
[**get_bot_icon**](BotApi.md#get_bot_icon) | **GET** /bots/{botId}/icon | BOTのアイコン画像を取得
[**get_bot_logs**](BotApi.md#get_bot_logs) | **GET** /bots/{botId}/logs | BOTのイベントログを取得
[**get_bots**](BotApi.md#get_bots) | **GET** /bots | BOTリストを取得
[**get_channel_bots**](BotApi.md#get_channel_bots) | **GET** /channels/{channelId}/bots | チャンネル参加中のBOTのリストを取得
[**inactivate_bot**](BotApi.md#inactivate_bot) | **POST** /bots/{botId}/actions/inactivate | BOTをインアクティベート
[**let_bot_join_channel**](BotApi.md#let_bot_join_channel) | **POST** /bots/{botId}/actions/join | BOTをチャンネルに参加させる
[**let_bot_leave_channel**](BotApi.md#let_bot_leave_channel) | **POST** /bots/{botId}/actions/leave | BOTをチャンネルから退出させる
[**reissue_bot**](BotApi.md#reissue_bot) | **POST** /bots/{botId}/actions/reissue | BOTのトークンを再発行


# **activate_bot**
> activate_bot(bot_id)

BOTをアクティベート

指定したBOTを有効化します。 対象のBOTの管理権限が必要です。

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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID

    try:
        # BOTをアクティベート
        api_instance.activate_bot(bot_id)
    except Exception as e:
        print("Exception when calling BotApi->activate_bot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 

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
**202** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_bot_icon**
> change_bot_icon(bot_id, file)

BOTのアイコン画像を変更

指定したBOTのアイコン画像を変更を変更します。 対象のBOTの管理権限が必要です。

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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID
    file = None # bytearray | アイコン画像(1MBまでのpng, jpeg, gif)

    try:
        # BOTのアイコン画像を変更
        api_instance.change_bot_icon(bot_id, file)
    except Exception as e:
        print("Exception when calling BotApi->change_bot_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 
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
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |
**413** | Request Entity Too Large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_bot_ws**
> connect_bot_ws()

WebSocket Mode BOT用通知ストリームに接続します

# BOT WebSocketプロトコル  ## 送信  `コマンド:引数1:引数2:...` のような形式のTextMessageをサーバーに送信することで、このWebSocketセッションに対する設定が実行できます。  ### `rtcstate`コマンド 自分のWebRTC状態を変更します。 他のコネクションが既に状態を保持している場合、変更することができません。  `rtcstate:{チャンネルID}:({状態}:{セッションID})*`  チャンネルIDにnullもしくは空文字を指定するか、状態にnullもしくは空文字を指定した場合、WebRTC状態はリセットされます。  `rtcstate:null`, `rtcstate:`, `rtcstate:channelId:null`, `rtcstate:channelId:`  コネクションが切断された場合、自分のWebRTC状態はリセットされます。  ## 受信  TextMessageとして各種イベントが`type`、`reqId`、`body`を持つJSONとして非同期に送られます。 `body`の内容はHTTP Modeの場合のRequest Bodyと同様です。 例外として`ERROR`イベントは`reqId`を持ちません。  例: PINGイベント `{\"type\":\"PING\",\"reqId\":\"requestId\",\"body\":{\"eventTime\":\"2019-05-07T04:50:48.582586882Z\"}}`  ### `ERROR`  コマンドの引数が不正などの理由でコマンドが受理されなかった場合に送られます。 非同期に送られるため、必ずしもコマンドとの対応関係を確定できないことに注意してください。 本番環境ではERRORが送られないようにすることが望ましいです。  `{\"type\":\"ERROR\",\"body\":\"message\"}`

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
    api_instance = traq.BotApi(api_client)

    try:
        # WebSocket Mode BOT用通知ストリームに接続します
        api_instance.connect_bot_ws()
    except Exception as e:
        print("Exception when calling BotApi->connect_bot_ws: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**101** | Switching Protocols |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bot**
> BotDetail create_bot(post_bot_request=post_bot_request)

BOTを作成

BOTを作成します。 作成後に購読イベントの設定を行う必要があります。 さらにHTTP Modeの場合はアクティベーションを行う必要があります。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.bot_detail import BotDetail
from traq.models.post_bot_request import PostBotRequest
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
    api_instance = traq.BotApi(api_client)
    post_bot_request = traq.PostBotRequest() # PostBotRequest |  (optional)

    try:
        # BOTを作成
        api_response = api_instance.create_bot(post_bot_request=post_bot_request)
        print("The response of BotApi->create_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotApi->create_bot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_bot_request** | [**PostBotRequest**](PostBotRequest.md)|  | [optional] 

### Return type

[**BotDetail**](BotDetail.md)

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
**409** | Conflict 既に使われている名前です。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bot**
> delete_bot(bot_id)

BOTを削除

指定したBOTを削除します。 対象のBOTの管理権限が必要です。

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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID

    try:
        # BOTを削除
        api_instance.delete_bot(bot_id)
    except Exception as e:
        print("Exception when calling BotApi->delete_bot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_bot**
> edit_bot(bot_id, patch_bot_request=patch_bot_request)

BOT情報を変更

指定したBOTの情報を変更します。 対象のBOTの管理権限が必要です。 BOT開発者UUIDを変更した場合は、変更先ユーザーにBOT管理権限が移譲され、自分自身は権限を失います。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.patch_bot_request import PatchBotRequest
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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID
    patch_bot_request = traq.PatchBotRequest() # PatchBotRequest |  (optional)

    try:
        # BOT情報を変更
        api_instance.edit_bot(bot_id, patch_bot_request=patch_bot_request)
    except Exception as e:
        print("Exception when calling BotApi->edit_bot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 
 **patch_bot_request** | [**PatchBotRequest**](PatchBotRequest.md)|  | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot**
> GetBot200Response get_bot(bot_id, detail=detail)

BOT情報を取得

指定したBOTのBOT情報を取得します。 BOT詳細情報を取得する場合は、対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.get_bot200_response import GetBot200Response
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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID
    detail = False # bool | 詳細情報を含めるかどうか (optional) (default to False)

    try:
        # BOT情報を取得
        api_response = api_instance.get_bot(bot_id, detail=detail)
        print("The response of BotApi->get_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotApi->get_bot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 
 **detail** | **bool**| 詳細情報を含めるかどうか | [optional] [default to False]

### Return type

[**GetBot200Response**](GetBot200Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_icon**
> bytearray get_bot_icon(bot_id)

BOTのアイコン画像を取得

指定したBOTのアイコン画像を取得を取得します。

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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID

    try:
        # BOTのアイコン画像を取得
        api_response = api_instance.get_bot_icon(bot_id)
        print("The response of BotApi->get_bot_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotApi->get_bot_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 

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
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_logs**
> List[BotEventLog] get_bot_logs(bot_id, limit=limit, offset=offset)

BOTのイベントログを取得

指定したBOTのイベントログを取得します。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.bot_event_log import BotEventLog
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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID
    limit = 50 # int | 取得する件数 (optional)
    offset = 0 # int | 取得するオフセット (optional) (default to 0)

    try:
        # BOTのイベントログを取得
        api_response = api_instance.get_bot_logs(bot_id, limit=limit, offset=offset)
        print("The response of BotApi->get_bot_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotApi->get_bot_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 
 **limit** | **int**| 取得する件数 | [optional] 
 **offset** | **int**| 取得するオフセット | [optional] [default to 0]

### Return type

[**List[BotEventLog]**](BotEventLog.md)

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
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bots**
> List[Bot] get_bots(all=all)

BOTリストを取得

BOT情報のリストを取得します。 allを指定しない場合、自分が開発者のBOTのみを返します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.bot import Bot
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
    api_instance = traq.BotApi(api_client)
    all = False # bool | 全てのBOTを取得するかどうか (optional) (default to False)

    try:
        # BOTリストを取得
        api_response = api_instance.get_bots(all=all)
        print("The response of BotApi->get_bots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotApi->get_bots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| 全てのBOTを取得するかどうか | [optional] [default to False]

### Return type

[**List[Bot]**](Bot.md)

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

# **get_channel_bots**
> List[BotUser] get_channel_bots(channel_id)

チャンネル参加中のBOTのリストを取得

指定したチャンネルに参加しているBOTのリストを取得します。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.bot_user import BotUser
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
    api_instance = traq.BotApi(api_client)
    channel_id = 'channel_id_example' # str | チャンネルUUID

    try:
        # チャンネル参加中のBOTのリストを取得
        api_response = api_instance.get_channel_bots(channel_id)
        print("The response of BotApi->get_channel_bots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotApi->get_channel_bots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| チャンネルUUID | 

### Return type

[**List[BotUser]**](BotUser.md)

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

# **inactivate_bot**
> inactivate_bot(bot_id)

BOTをインアクティベート

指定したBOTを無効化します。対象のBOTの管理権限が必要です。

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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID

    try:
        # BOTをインアクティベート
        api_instance.inactivate_bot(bot_id)
    except Exception as e:
        print("Exception when calling BotApi->inactivate_bot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 

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
**204** | No Content BOTがインアクティベートされました。 |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **let_bot_join_channel**
> let_bot_join_channel(bot_id, post_bot_action_join_request=post_bot_action_join_request)

BOTをチャンネルに参加させる

指定したBOTを指定したチャンネルに参加させます。 チャンネルに参加したBOTは、そのチャンネルの各種イベントを受け取るようになります。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.post_bot_action_join_request import PostBotActionJoinRequest
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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID
    post_bot_action_join_request = traq.PostBotActionJoinRequest() # PostBotActionJoinRequest |  (optional)

    try:
        # BOTをチャンネルに参加させる
        api_instance.let_bot_join_channel(bot_id, post_bot_action_join_request=post_bot_action_join_request)
    except Exception as e:
        print("Exception when calling BotApi->let_bot_join_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 
 **post_bot_action_join_request** | [**PostBotActionJoinRequest**](PostBotActionJoinRequest.md)|  | [optional] 

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
**204** | No Content BOTを参加させました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **let_bot_leave_channel**
> let_bot_leave_channel(bot_id, post_bot_action_leave_request=post_bot_action_leave_request)

BOTをチャンネルから退出させる

指定したBOTを指定したチャンネルから退出させます。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.post_bot_action_leave_request import PostBotActionLeaveRequest
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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID
    post_bot_action_leave_request = traq.PostBotActionLeaveRequest() # PostBotActionLeaveRequest |  (optional)

    try:
        # BOTをチャンネルから退出させる
        api_instance.let_bot_leave_channel(bot_id, post_bot_action_leave_request=post_bot_action_leave_request)
    except Exception as e:
        print("Exception when calling BotApi->let_bot_leave_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 
 **post_bot_action_leave_request** | [**PostBotActionLeaveRequest**](PostBotActionLeaveRequest.md)|  | [optional] 

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
**204** | No Content BOTを退出させました。 |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reissue_bot**
> BotTokens reissue_bot(bot_id)

BOTのトークンを再発行

指定したBOTの現在の各種トークンを無効化し、再発行を行います。 対象のBOTの管理権限が必要です。

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.bot_tokens import BotTokens
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
    api_instance = traq.BotApi(api_client)
    bot_id = 'bot_id_example' # str | BOTUUID

    try:
        # BOTのトークンを再発行
        api_response = api_instance.reissue_bot(bot_id)
        print("The response of BotApi->reissue_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotApi->reissue_bot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**| BOTUUID | 

### Return type

[**BotTokens**](BotTokens.md)

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
**404** | Not Found BOTが見つかりません。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

