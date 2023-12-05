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

from traq.models.message_search_result import MessageSearchResult

class TestMessageSearchResult(unittest.TestCase):
    """MessageSearchResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessageSearchResult:
        """Test MessageSearchResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessageSearchResult`
        """
        model = MessageSearchResult()
        if include_optional:
            return MessageSearchResult(
                total_hits = 56,
                hits = [
                    traq.models.message.Message(
                        id = '', 
                        user_id = '', 
                        channel_id = '', 
                        content = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pinned = True, 
                        stamps = [
                            traq.models.message_stamp.MessageStamp(
                                user_id = '', 
                                stamp_id = '', 
                                count = 56, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        thread_id = '', )
                    ]
            )
        else:
            return MessageSearchResult(
                total_hits = 56,
                hits = [
                    traq.models.message.Message(
                        id = '', 
                        user_id = '', 
                        channel_id = '', 
                        content = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pinned = True, 
                        stamps = [
                            traq.models.message_stamp.MessageStamp(
                                user_id = '', 
                                stamp_id = '', 
                                count = 56, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        thread_id = '', )
                    ],
        )
        """

    def testMessageSearchResult(self):
        """Test MessageSearchResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
