# GetClient200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | クライアントUUID | 
**name** | **str** | クライアント名 | 
**description** | **str** | 説明 | 
**developer_id** | **str** | クライアント開発者UUID | 
**scopes** | [**List[OAuth2Scope]**](OAuth2Scope.md) | 要求スコープの配列 | 
**callback_url** | **str** | コールバックURL | 
**secret** | **str** | クライアントシークレット | 

## Example

```python
from traq.models.get_client200_response import GetClient200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClient200Response from a JSON string
get_client200_response_instance = GetClient200Response.from_json(json)
# print the JSON string representation of the object
print GetClient200Response.to_json()

# convert the object into a dict
get_client200_response_dict = get_client200_response_instance.to_dict()
# create an instance of GetClient200Response from a dict
get_client200_response_form_dict = get_client200_response.from_dict(get_client200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


