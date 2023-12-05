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

from traq.models.ogp import Ogp

class TestOgp(unittest.TestCase):
    """Ogp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Ogp:
        """Test Ogp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Ogp`
        """
        model = Ogp()
        if include_optional:
            return Ogp(
                type = '',
                title = '',
                url = '',
                images = [
                    traq.models.ogp_media.OgpMedia(
                        url = '', 
                        secure_url = '', 
                        type = '', 
                        width = 56, 
                        height = 56, )
                    ],
                description = '',
                videos = [
                    traq.models.ogp_media.OgpMedia(
                        url = '', 
                        secure_url = '', 
                        type = '', 
                        width = 56, 
                        height = 56, )
                    ]
            )
        else:
            return Ogp(
                type = '',
                title = '',
                url = '',
                images = [
                    traq.models.ogp_media.OgpMedia(
                        url = '', 
                        secure_url = '', 
                        type = '', 
                        width = 56, 
                        height = 56, )
                    ],
                description = '',
                videos = [
                    traq.models.ogp_media.OgpMedia(
                        url = '', 
                        secure_url = '', 
                        type = '', 
                        width = 56, 
                        height = 56, )
                    ],
        )
        """

    def testOgp(self):
        """Test Ogp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()