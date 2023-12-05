from main.modules.traq import traqApi
import os
from main.models import User, Message, Stamp
import main.modules.traq as traq


def __check_already_loaded_user_database():
    if len(User.objects.all()) < 10:
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
    limit: int = None,
    offset: int = None,
    sort: str = None,
) -> traq.MessageSearch:
    traq = traqApi(os.environ["TRAQ_ACCESS_TOKEN"])
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
    # database update. if message is already in database, update it. if not, create it.
    for message in messages["hits"]:
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
        m.save()
        if len(m.stamps.all()) != 0:
            m.stamps.all().delete()
        for stamp in message["stamps"]:
            s = Stamp.objects.create(
                userId=stamp["userId"],
                stampId=stamp["stampId"],
                count=stamp["count"],
                createdAt=stamp["createdAt"],
                updatedAt=stamp["updatedAt"],
                message=m,
            )
            s.save()
    return messages


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
