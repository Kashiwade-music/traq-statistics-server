# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from traq.api.oauth2_api import Oauth2Api


class TestOauth2Api(unittest.TestCase):
    """Oauth2Api unit test stubs"""

    def setUp(self) -> None:
        self.api = Oauth2Api()

    def tearDown(self) -> None:
        pass

    def test_create_client(self) -> None:
        """Test case for create_client

        OAuth2クライアントを作成
        """
        pass

    def test_delete_client(self) -> None:
        """Test case for delete_client

        OAuth2クライアントを削除
        """
        pass

    def test_edit_client(self) -> None:
        """Test case for edit_client

        OAuth2クライアント情報を変更
        """
        pass

    def test_get_client(self) -> None:
        """Test case for get_client

        OAuth2クライアント情報を取得
        """
        pass

    def test_get_clients(self) -> None:
        """Test case for get_clients

        OAuth2クライアントのリストを取得
        """
        pass

    def test_get_my_tokens(self) -> None:
        """Test case for get_my_tokens

        有効トークンのリストを取得
        """
        pass

    def test_get_o_auth2_authorize(self) -> None:
        """Test case for get_o_auth2_authorize

        OAuth2 認可エンドポイント
        """
        pass

    def test_post_o_auth2_authorize(self) -> None:
        """Test case for post_o_auth2_authorize

        OAuth2 認可エンドポイント
        """
        pass

    def test_post_o_auth2_authorize_decide(self) -> None:
        """Test case for post_o_auth2_authorize_decide

        OAuth2 認可承諾API
        """
        pass

    def test_post_o_auth2_token(self) -> None:
        """Test case for post_o_auth2_token

        OAuth2 トークンエンドポイント
        """
        pass

    def test_revoke_my_token(self) -> None:
        """Test case for revoke_my_token

        トークンの認可を取り消す
        """
        pass

    def test_revoke_o_auth2_token(self) -> None:
        """Test case for revoke_o_auth2_token

        OAuth2 トークン無効化エンドポイント
        """
        pass


if __name__ == '__main__':
    unittest.main()
