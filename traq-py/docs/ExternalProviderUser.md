# ExternalProviderUser

外部認証アカウントユーザー

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** | 外部サービス名 | 
**linked_at** | **str** | 紐付けた日時 | 
**external_name** | **str** | 外部アカウント名 | 

## Example

```python
from traq.models.external_provider_user import ExternalProviderUser

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalProviderUser from a JSON string
external_provider_user_instance = ExternalProviderUser.from_json(json)
# print the JSON string representation of the object
print ExternalProviderUser.to_json()

# convert the object into a dict
external_provider_user_dict = external_provider_user_instance.to_dict()
# create an instance of ExternalProviderUser from a dict
external_provider_user_form_dict = external_provider_user.from_dict(external_provider_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


