# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from traq.api.pin_api import PinApi


class TestPinApi(unittest.TestCase):
    """PinApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PinApi()

    def tearDown(self) -> None:
        pass

    def test_create_pin(self) -> None:
        """Test case for create_pin

        ピン留めする
        """
        pass

    def test_get_channel_pins(self) -> None:
        """Test case for get_channel_pins

        チャンネルピンのリストを取得
        """
        pass

    def test_get_pin(self) -> None:
        """Test case for get_pin

        ピン留めを取得
        """
        pass

    def test_remove_pin(self) -> None:
        """Test case for remove_pin

        ピン留めを外す
        """
        pass


if __name__ == '__main__':
    unittest.main()