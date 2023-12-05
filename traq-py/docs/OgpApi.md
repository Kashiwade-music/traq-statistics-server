# traq.OgpApi

All URIs are relative to *https://q.trap.jp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ogp_cache**](OgpApi.md#delete_ogp_cache) | **DELETE** /ogp/cache | OGP情報のキャッシュを削除
[**get_ogp**](OgpApi.md#get_ogp) | **GET** /ogp | OGP情報を取得


# **delete_ogp_cache**
> delete_ogp_cache(url)

OGP情報のキャッシュを削除

指定されたURLのOGP情報のキャッシュを削除します。

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
    api_instance = traq.OgpApi(api_client)
    url = 'url_example' # str | OGPのキャッシュを削除したいURL

    try:
        # OGP情報のキャッシュを削除
        api_instance.delete_ogp_cache(url)
    except Exception as e:
        print("Exception when calling OgpApi->delete_ogp_cache: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| OGPのキャッシュを削除したいURL | 

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
**204** | No Content |  -  |
**400** | 指定したURLが不正です。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ogp**
> Ogp get_ogp(url)

OGP情報を取得

指定されたURLのOGP情報を取得します。 指定されたURLに対するOGP情報が見つからなかった場合、typeがemptyに設定された空のOGP情報を返します。 

### Example

* OAuth Authentication (OAuth2):
* Bearer Authentication (bearerAuth):

```python
import time
import os
import traq
from traq.models.ogp import Ogp
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
    api_instance = traq.OgpApi(api_client)
    url = 'url_example' # str | OGPを取得したいURL

    try:
        # OGP情報を取得
        api_response = api_instance.get_ogp(url)
        print("The response of OgpApi->get_ogp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OgpApi->get_ogp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| OGPを取得したいURL | 

### Return type

[**Ogp**](Ogp.md)

### Authorization

[OAuth2](../README.md#OAuth2), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | 指定したURLが不正です。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

