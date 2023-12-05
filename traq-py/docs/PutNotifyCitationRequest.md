# PutNotifyCitationRequest

メッセージ引用通知設定リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notify_citation** | **bool** | メッセージ引用通知の設定情報 | 

## Example

```python
from traq.models.put_notify_citation_request import PutNotifyCitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutNotifyCitationRequest from a JSON string
put_notify_citation_request_instance = PutNotifyCitationRequest.from_json(json)
# print the JSON string representation of the object
print PutNotifyCitationRequest.to_json()

# convert the object into a dict
put_notify_citation_request_dict = put_notify_citation_request_instance.to_dict()
# create an instance of PutNotifyCitationRequest from a dict
put_notify_citation_request_form_dict = put_notify_citation_request.from_dict(put_notify_citation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


