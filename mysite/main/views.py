from django.shortcuts import render
from django.http import HttpResponse
from main.modules.traq import traqApi
import main.modules.utils as utils
import os
from main.models import User
from rich import print
import pprint


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def users(request, username):
    _ = utils.search_messages_from_traq(from_=utils.get_userid_from_username(username))
    ms = utils.search_messages_from_db(
        word="は", from_=utils.get_userid_from_username(username)
    )
    return HttpResponse(pprint.pformat(ms))
