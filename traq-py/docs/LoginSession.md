# LoginSession

ログインセッション情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | セッションUUID | 
**issued_at** | **datetime** | 発行日時 | 

## Example

```python
from traq.models.login_session import LoginSession

# TODO update the JSON string below
json = "{}"
# create an instance of LoginSession from a JSON string
login_session_instance = LoginSession.from_json(json)
# print the JSON string representation of the object
print LoginSession.to_json()

# convert the object into a dict
login_session_dict = login_session_instance.to_dict()
# create an instance of LoginSession from a dict
login_session_form_dict = login_session.from_dict(login_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


