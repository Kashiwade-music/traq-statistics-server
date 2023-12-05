# PutChannelSubscribersRequest

通知をオンにするユーザーのUUID配列

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on** | **List[str]** | 通知をオンにするユーザーのUUID配列 | 

## Example

```python
from traq.models.put_channel_subscribers_request import PutChannelSubscribersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutChannelSubscribersRequest from a JSON string
put_channel_subscribers_request_instance = PutChannelSubscribersRequest.from_json(json)
# print the JSON string representation of the object
print PutChannelSubscribersRequest.to_json()

# convert the object into a dict
put_channel_subscribers_request_dict = put_channel_subscribers_request_instance.to_dict()
# create an instance of PutChannelSubscribersRequest from a dict
put_channel_subscribers_request_form_dict = put_channel_subscribers_request.from_dict(put_channel_subscribers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


