# PutMyPasswordRequest

パスワード変更リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | 現在のパスワード | 
**new_password** | **str** | 新しいパスワード | 

## Example

```python
from traq.models.put_my_password_request import PutMyPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutMyPasswordRequest from a JSON string
put_my_password_request_instance = PutMyPasswordRequest.from_json(json)
# print the JSON string representation of the object
print PutMyPasswordRequest.to_json()

# convert the object into a dict
put_my_password_request_dict = put_my_password_request_instance.to_dict()
# create an instance of PutMyPasswordRequest from a dict
put_my_password_request_form_dict = put_my_password_request.from_dict(put_my_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


