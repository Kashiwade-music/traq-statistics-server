# PatchMeRequest

自分のユーザー情報変更リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | 新しい表示名 | [optional] 
**twitter_id** | **str** | TwitterID | [optional] 
**bio** | **str** | 自己紹介(biography) | [optional] 
**home_channel** | **str** | ホームチャンネルのUUID &#x60;00000000-0000-0000-0000-000000000000&#x60;を指定すると、ホームチャンネルが&#x60;null&#x60;に設定されます | [optional] 

## Example

```python
from traq.models.patch_me_request import PatchMeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchMeRequest from a JSON string
patch_me_request_instance = PatchMeRequest.from_json(json)
# print the JSON string representation of the object
print PatchMeRequest.to_json()

# convert the object into a dict
patch_me_request_dict = patch_me_request_instance.to_dict()
# create an instance of PatchMeRequest from a dict
patch_me_request_form_dict = patch_me_request.from_dict(patch_me_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


