# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from traq.models.patch_user_tag_request import PatchUserTagRequest

class TestPatchUserTagRequest(unittest.TestCase):
    """PatchUserTagRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchUserTagRequest:
        """Test PatchUserTagRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchUserTagRequest`
        """
        model = PatchUserTagRequest()
        if include_optional:
            return PatchUserTagRequest(
                is_locked = True
            )
        else:
            return PatchUserTagRequest(
                is_locked = True,
        )
        """

    def testPatchUserTagRequest(self):
        """Test PatchUserTagRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()