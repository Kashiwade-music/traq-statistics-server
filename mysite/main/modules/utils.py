import time
from main.modules.traq import traqApi
import os
from main.models import User, Message, Stamp
import main.modules.traq as traq
from rich.progress import track
import datetime


def convert_to_datetime(date_string: str) -> datetime.datetime:
    """
    Convert a date string to a datetime object.

    Args:
        date_string (str): The date string to be converted. Format: "%Y-%m-%dT%H:%M:%S.%fZ" e.g. "2023-12-06T00:00:00.000Z"

    Returns:
        datetime.datetime: The converted datetime object.
    """
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    datetime_object = datetime.datetime.strptime(date_string, date_format)
    return datetime_object


def convert_datatime_utc_to_jst(
    datetime_object: datetime.datetime,
) -> datetime.datetime:
    """
    Convert a datetime object from UTC to JST (Japan Standard Time).

    Args:
        datetime_object (datetime.datetime): The datetime object to be converted.

    Returns:
        datetime.datetime: The converted datetime object in JST.
    """
    datetime_object = datetime_object + datetime.timedelta(hours=9)
    return datetime_object


def convert_datatime_jst_to_utc(
    datetime_object: datetime.datetime,
) -> datetime.datetime:
    """
    Converts a datetime object from JST (Japan Standard Time) to UTC (Coordinated Universal Time).

    Args:
        datetime_object (datetime.datetime): The datetime object to be converted.

    Returns:
        datetime.datetime: The converted datetime object in UTC.
    """
    datetime_object = datetime_object - datetime.timedelta(hours=9)
    return datetime_object


def __check_already_loaded_user_database():
    """
    Check if the user database is already loaded.
    If the database is empty, load the users from the traQ API and save them to the database.
    """
    if len(User.objects.all()) < 1:
        User.objects.all().delete()
        traq = traqApi(os.environ["TRAQ_ACCESS_TOKEN"])
        users = traq.get_users()
        for user in users:
            u = User.objects.create(
                id=user["id"],
                name=user["name"],
                displayName=user["displayName"],
                iconFileId=user["iconFileId"],
                bot=user["bot"],
                state=user["state"],
                updatedAt=user["updatedAt"],
            )
            u.save()


def get_userid_from_username(username: str) -> str:
    """
    Get the user ID from the given username.

    Args:
        username (str): The username of the user. e.g. "kashiwade"

    Returns:
        str: The user ID corresponding to the given username.
    """
    __check_already_loaded_user_database()
    return User.objects.get(name=username).id


def search_messages_from_traq(
    word: str = None,
    after: str = None,
    before: str = None,
    in_: str = None,
    to: str = None,
    from_: str = None,
    citation: str = None,
    bot: bool = False,
    hasURL: bool = None,
    hasAttachment: bool = None,
    hasImage: bool = None,
    hasVideo: bool = None,
    hasAudio: bool = None,
    limit: int = 100,
    offset: int = None,
    sort: str = None,
) -> traq.MessageSearch:
    """
    Search messages from traq based on various parameters.

    Args:
        word (str, optional): The word to search for in the messages. Defaults to None.
        after (str, optional): The date and time after which the messages were created. Defaults to None. UTC. Format: "%Y-%m-%dT%H:%M:%S.%fZ" e.g. "2023-12-06T00:00:00.000Z"
        before (str, optional): The date and time before which the messages were created. Defaults to None. UTC. Format: "%Y-%m-%dT%H:%M:%S.%fZ" e.g. "2023-12-06T00:00:00.000Z"
        in_ (str, optional): The channel ID to search within. Defaults to None.
        to (str, optional): The user ID to search for messages mention to. Defaults to None.
        from_ (str, optional): The user ID to search for messages sent from. Defaults to None.
        citation (str, optional): The message ID to search for messages that cite it. Defaults to None.
        bot (bool, optional): Whether to search for messages sent by bots. Defaults to False.
        hasURL (bool, optional): Whether to search for messages that have URLs. Defaults to None.
        hasAttachment (bool, optional): Whether to search for messages that have attachments. Defaults to None.
        hasImage (bool, optional): Whether to search for messages that have images. Defaults to None.
        hasVideo (bool, optional): Whether to search for messages that have videos. Defaults to None.
        hasAudio (bool, optional): Whether to search for messages that have audio files. Defaults to None.
        limit (int, optional): The maximum number of messages to retrieve. Defaults to 100. Max: 100
        offset (int, optional): The offset to start retrieving messages from. Defaults to None.
        sort (str, optional): The sorting order of the messages. Defaults to None. createdAt, -createdAt, updatedAt, -updatedAt

    Returns:
        traq.MessageSearch: A dictionary containing the total number of hits and the list of messages.
    """
    traq = traqApi(os.environ["TRAQ_ACCESS_TOKEN"])
    all_messages = []
    total_hits = 0

    while True:
        messages = traq.search_messages(
            word=word,
            after=after,
            before=before,
            in_=in_,
            to=to,
            from_=from_,
            citation=citation,
            bot=bot,
            hasURL=hasURL,
            hasAttachment=hasAttachment,
            hasImage=hasImage,
            hasVideo=hasVideo,
            hasAudio=hasAudio,
            limit=limit,
            offset=offset,
            sort=sort,
        )

        all_messages.extend(messages["hits"])

        if messages["totalHits"] == len(all_messages):
            total_hits = messages["totalHits"]
            break

        offset = len(all_messages)
        print(f"totalHits: {messages['totalHits']}, offset: {offset}")
        time.sleep(0.5)

    for message in track(all_messages, description="Saving messages to database..."):
        m, _ = Message.objects.update_or_create(
            id=message["id"],
            defaults={
                "userId": message["userId"],
                "channelId": message["channelId"],
                "content": message["content"],
                "createdAt": message["createdAt"],
                "updatedAt": message["updatedAt"],
                "pinned": message["pinned"],
            },
        )

        # Delete existing stamps in one query instead of individually
        m.stamps.all().delete()

        # Create stamps in bulk
        stamps = [
            Stamp(
                userId=stamp["userId"],
                stampId=stamp["stampId"],
                count=stamp["count"],
                createdAt=stamp["createdAt"],
                updatedAt=stamp["updatedAt"],
                message=m,
            )
            for stamp in message["stamps"]
        ]

        Stamp.objects.bulk_create(stamps)

    return {"totalHits": total_hits, "hits": all_messages}


def get_all_messages_from_traq_and_save_to_db(after: str = None):
    """
    Retrieve all messages from traQ and save them to the database.

    Args:
        after (str, optional): The timestamp to start retrieving messages from. Defaults to None. Format: "%Y-%m-%dT%H:%M:%S.%fZ" e.g. "2023-12-06T00:00:00.000Z"

    Returns:
        None
    """
    temp_after = after
    temp_before = None
    while True:
        m = search_messages_from_traq(after=temp_after, before=temp_before)
        if len(m["hits"]) == 0:
            break
        oldest_message = m["hits"][-1]
        oldest_message_datetime = convert_to_datetime(oldest_message["createdAt"])
        print(f"oldest_message_datetime: {oldest_message_datetime}")
        if oldest_message_datetime < convert_to_datetime(after):
            break
        temp_before = oldest_message["createdAt"]


def search_messages_from_db(
    word: str = None,
    after: str = None,
    before: str = None,
    in_: str = None,
    to: str = None,
    from_: str = None,
    citation: str = None,
    limit: int = None,
    offset: int = None,
    sort: str = None,
) -> traq.MessageSearch:
    """
    Search messages from the database based on the given criteria.

    Args:
        word (str, optional): The word to search for in the message content. Defaults to None.
        after (str, optional): The minimum creation date of the messages to search for. Defaults to None. UTC. Format: "%Y-%m-%dT%H:%M:%S.%fZ" e.g. "2023-12-06T00:00:00.000Z"
        before (str, optional): The maximum creation date of the messages to search for. Defaults to None. UTC. Format: "%Y-%m-%dT%H:%M:%S.%fZ" e.g. "2023-12-06T00:00:00.000Z"
        in_ (str, optional): The channel ID to search within. Defaults to None.
        to (str, optional): The user ID to search for messages mention to. Defaults to None.
        from_ (str, optional): The user ID to search for messages sent from. Defaults to None.
        citation (str, optional): The message ID to search for messages that cite it. Defaults to None.
        limit (int, optional): The maximum number of messages to return. Defaults to None.
        offset (int, optional): The number of messages to skip before returning results. Defaults to None.
        sort (str, optional): The sorting order of the messages by createdAt. Can be "asc" for ascending or "desc" for descending. Defaults to None.

    Returns:
        traq.MessageSearch: An object containing the search results.

    """
    messages = Message.objects.all()
    print(len(messages))
    if word != None:
        messages = messages.filter(content__contains=word)
    if after != None:
        messages = messages.filter(createdAt__gte=after)
    if before != None:
        messages = messages.filter(createdAt__lte=before)
    if in_ != None:
        messages = messages.filter(channelId=in_)
    if to != None:
        messages = messages.filter(content__contains=to)
    if from_ != None:
        messages = messages.filter(userId=from_)
    if citation != None:
        messages = messages.filter(content__contains=citation)
    if limit != None:
        messages = messages[:limit]
    if offset != None:
        messages = messages[offset:]
    if sort != None:
        if sort == "asc":
            messages = messages.order_by("createdAt")
        elif sort == "desc":
            messages = messages.order_by("-createdAt")

    return_dict = {
        "totalHits": len(messages),
        "hits": [
            {
                "id": message.id,
                "userId": message.userId,
                "channelId": message.channelId,
                "content": message.content,
                "createdAt": message.createdAt,
                "updatedAt": message.updatedAt,
                "pinned": message.pinned,
                "stamps": [
                    {
                        "userId": stamp.userId,
                        "stampId": stamp.stampId,
                        "count": stamp.count,
                        "createdAt": stamp.createdAt,
                        "updatedAt": stamp.updatedAt,
                    }
                    for stamp in message.stamps.all()
                ],
            }
            for message in messages
        ],
    }
    return return_dict
