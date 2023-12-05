import requests
from typing import TypedDict


class User(TypedDict):
    # {
    #     "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #     "name": "Skh4WEdNC9o-m",
    #     "displayName": "string",
    #     "iconFileId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #     "bot": true,
    #     "state": 0,
    #     "updatedAt": "2023-12-05T09:28:56.258Z"
    # }
    id: str
    name: str
    displayName: str
    iconFileId: str
    bot: bool
    state: int
    updatedAt: str


class Stamp(TypedDict):
    # {
    #   "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #   "stampId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #   "count": 0,
    #   "createdAt": "2023-12-05T10:33:46.947Z",
    #   "updatedAt": "2023-12-05T10:33:46.947Z"
    # }
    userId: str
    stampId: str
    count: int
    createdAt: str
    updatedAt: str


class Message(TypedDict):
    # {
    #     "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #     "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #     "channelId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #     "content": "string",
    #     "createdAt": "2023-12-05T10:33:46.947Z",
    #     "updatedAt": "2023-12-05T10:33:46.947Z",
    #     "pinned": true,
    #     "stamps": [
    #       {
    #         "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #         "stampId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #         "count": 0,
    #         "createdAt": "2023-12-05T10:33:46.947Z",
    #         "updatedAt": "2023-12-05T10:33:46.947Z"
    #       }
    #     ],
    #     "threadId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    # }
    id: str
    userId: str
    channelId: str
    content: str
    createdAt: str
    updatedAt: str
    pinned: bool
    stamps: list[Stamp]
    threadId: str


class MessageSearch(TypedDict):
    totalHits: int
    hits: list[Message]


class traqApi:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            # bearer token
            "Authorization": f"Bearer {self.token}",
        }

    def get_users(self, include_suspended=False, name=None) -> list[User]:
        """
        Retrieve a list of users from the TRAQ API.

        Args:
            include_suspended (bool, optional): Whether to include suspended users. Defaults to False.
            name (str, optional): Filter users by name. Defaults to None.

        Returns:
            list[User]: A list of User objects representing the users.
        """
        res = requests.get(
            "https://q.trap.jp/api/v3/users",
            headers=self.headers,
            params={"includeSuspended": include_suspended, "name": name},
        )
        return res.json()

    def search_messages(
        self,
        word: str = None,
        after: str = None,
        before: str = None,
        in_: str = None,
        to: str = None,
        from_: str = None,
        citation: str = None,
        bot: bool = None,
        hasURL: bool = None,
        hasAttachment: bool = None,
        hasImage: bool = None,
        hasVideo: bool = None,
        hasAudio: bool = None,
        limit: int = None,
        offset: int = None,
        sort: str = None,
    ) -> MessageSearch:
        res = requests.get(
            "https://q.trap.jp/api/v3/messages",
            headers=self.headers,
            params={
                "word": word,
                "after": after,
                "before": before,
                "in": in_,
                "to": to,
                "from": from_,
                "citation": citation,
                "bot": "true" if bot else "false",
                "hasURL": "true" if hasURL else "false",
                "hasAttachment": "true" if hasAttachment else "false",
                "hasImage": "true" if hasImage else "false",
                "hasVideo": "true" if hasVideo else "false",
                "hasAudio": "true" if hasAudio else "false",
                "limit": limit,
                "offset": offset,
                "sort": sort,
            },
        )
        print(res.json())
        return res.json()


if __name__ == "__main__":
    import os

    token = os.environ["TRAQ_ACCESS_TOKEN"]
    traq = traqApi(token)
    print(traq.get_users())
