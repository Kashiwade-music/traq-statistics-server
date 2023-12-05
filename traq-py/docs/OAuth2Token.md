# OAuth2Token


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**token_type** | **str** |  | 
**expires_in** | **int** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**id_token** | **str** |  | [optional] 

## Example

```python
from traq.models.o_auth2_token import OAuth2Token

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Token from a JSON string
o_auth2_token_instance = OAuth2Token.from_json(json)
# print the JSON string representation of the object
print OAuth2Token.to_json()

# convert the object into a dict
o_auth2_token_dict = o_auth2_token_instance.to_dict()
# create an instance of OAuth2Token from a dict
o_auth2_token_form_dict = o_auth2_token.from_dict(o_auth2_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


