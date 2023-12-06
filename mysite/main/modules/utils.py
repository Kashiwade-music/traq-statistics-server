import time
from main.modules.traq import traqApi
import os
from main.models import User, Message, Stamp
import main.modules.traq as traq
from rich.progress import track
import datetime


def convert_to_datetime(date_string):
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    datetime_object = datetime.datetime.strptime(date_string, date_format)
    return datetime_object

def __check_already_loaded_user_database():
    print("Checking if user database is already loaded...")
    print(f"Number of users in database: {len(User.objects.all())}")
    if len(User.objects.all()) < 1:
        print("User database is empty. Loading...")
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


def get_userid_from_username(username):
    __check_already_loaded_user_database()
    # print all users
    print(username)
    user = User.objects.get(name=username)
    return user.id


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
