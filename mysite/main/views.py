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
    # _ = utils.search_messages_from_traq()
    ms = utils.search_messages_from_db(
        from_=utils.get_userid_from_username(username), sort="asc"
    )
    utils.get_all_messages_from_traq_and_save_to_db(after="2023-12-06T00:00:00.000Z")
    print(len(ms["hits"]))
    return HttpResponse([f"createdAt: {m['createdAt']}, userid: {m['userId']}, content: {m['content']}<br>" for m in ms["hits"]])
