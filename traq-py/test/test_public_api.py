# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from traq.api.public_api import PublicApi


class TestPublicApi(unittest.TestCase):
    """PublicApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PublicApi()

    def tearDown(self) -> None:
        pass

    def test_get_public_user_icon(self) -> None:
        """Test case for get_public_user_icon

        ユーザーのアイコン画像を取得
        """
        pass

    def test_get_server_version(self) -> None:
        """Test case for get_server_version

        バージョンを取得
        """
        pass


if __name__ == '__main__':
    unittest.main()