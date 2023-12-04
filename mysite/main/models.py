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
