from django.db import models


# Create your models here.
class User(models.Model):
    # {
    #   "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #   "name": "Zg9VGiYPmMGH0c8cQd1trkxr8j",
    #   "displayName": "string",
    #   "iconFileId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    #   "bot": true,
    #   "state": 0,
    #   "updatedAt": "2023-12-04T12:56:37.586Z"
    # }
    id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=36)
    displayName = models.CharField(max_length=36)
    iconFileId = models.CharField(max_length=36)
    bot = models.BooleanField()
    state = models.IntegerField()
    updatedAt = models.DateTimeField()

    def __str__(self):
        return f"{self.name} ({self.displayName})"


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


class Message(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    userId = models.CharField(max_length=36)
    channelId = models.CharField(max_length=36)
    content = models.CharField(max_length=10000)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    pinned = models.BooleanField()

    def __str__(self):
        return f"{self.id} ({self.content})"


class Stamp(models.Model):
    userId = models.CharField(max_length=36)
    stampId = models.CharField(max_length=36)
    count = models.IntegerField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="stamps"
    )

    def __str__(self):
        return f"{self.userId} ({self.stampId})"
