# PatchStampRequest

スタンプ情報変更リクエスト

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | スタンプ名 | [optional] 
**creator_id** | **str** | 作成者UUID | [optional] 

## Example

```python
from traq.models.patch_stamp_request import PatchStampRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchStampRequest from a JSON string
patch_stamp_request_instance = PatchStampRequest.from_json(json)
# print the JSON string representation of the object
print PatchStampRequest.to_json()

# convert the object into a dict
patch_stamp_request_dict = patch_stamp_request_instance.to_dict()
# create an instance of PatchStampRequest from a dict
patch_stamp_request_form_dict = patch_stamp_request.from_dict(patch_stamp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


