# VersionFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_login** | **List[str]** | 有効な外部ログインプロバイダ | 
**sign_up_allowed** | **bool** | ユーザーが自身で新規登録(POST /api/v3/users)可能か | 

## Example

```python
from traq.models.version_flags import VersionFlags

# TODO update the JSON string below
json = "{}"
# create an instance of VersionFlags from a JSON string
version_flags_instance = VersionFlags.from_json(json)
# print the JSON string representation of the object
print VersionFlags.to_json()

# convert the object into a dict
version_flags_dict = version_flags_instance.to_dict()
# create an instance of VersionFlags from a dict
version_flags_form_dict = version_flags.from_dict(version_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


