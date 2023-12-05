# PostLinkExternalAccount

POST /users/me/ex-accounts/link 用リクエストボディ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** | 外部サービス名 | 

## Example

```python
from traq.models.post_link_external_account import PostLinkExternalAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PostLinkExternalAccount from a JSON string
post_link_external_account_instance = PostLinkExternalAccount.from_json(json)
# print the JSON string representation of the object
print PostLinkExternalAccount.to_json()

# convert the object into a dict
post_link_external_account_dict = post_link_external_account_instance.to_dict()
# create an instance of PostLinkExternalAccount from a dict
post_link_external_account_form_dict = post_link_external_account.from_dict(post_link_external_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


