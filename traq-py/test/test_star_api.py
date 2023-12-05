# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from traq.api.star_api import StarApi


class TestStarApi(unittest.TestCase):
    """StarApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StarApi()

    def tearDown(self) -> None:
        pass

    def test_add_my_star(self) -> None:
        """Test case for add_my_star

        チャンネルをスターに追加
        """
        pass

    def test_get_my_stars(self) -> None:
        """Test case for get_my_stars

        スターチャンネルリストを取得
        """
        pass

    def test_remove_my_star(self) -> None:
        """Test case for remove_my_star

        チャンネルをスターから削除します
        """
        pass


if __name__ == '__main__':
    unittest.main()