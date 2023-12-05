# PutUserPasswordRequest

ユーザーパスワード変更リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** | 新しいパスワード | 

## Example

```python
from traq.models.put_user_password_request import PutUserPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutUserPasswordRequest from a JSON string
put_user_password_request_instance = PutUserPasswordRequest.from_json(json)
# print the JSON string representation of the object
print PutUserPasswordRequest.to_json()

# convert the object into a dict
put_user_password_request_dict = put_user_password_request_instance.to_dict()
# create an instance of PutUserPasswordRequest from a dict
put_user_password_request_form_dict = put_user_password_request.from_dict(put_user_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


