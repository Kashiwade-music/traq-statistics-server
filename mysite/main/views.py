from django.shortcuts import render
from django.http import HttpResponse
import traq
from traq.api import message_api, user_api
import os
from main.models import User

configuration = traq.Configuration(host="https://q.trap.jp/api/v3")
configuration.access_token = os.environ["TRAQ_ACCESS_TOKEN"]


def check_already_loaded_user_database():
    # check django models has already loaded user database
    if len(User.objects.all()) == 0:
        # load user database
        with traq.ApiClient(configuration=configuration) as api_client:
            api_instance = user_api.UserApi(api_client)
            try:
                api_response = api_instance.get_users()
                for user in api_response:
                    print(api_response)
                    User.objects.create(
                        id=user.id,
                        name=user.name,
                        displayName=user.display_name,
                        iconFileId=user.icon_file_id,
                        bot=user.bot,
                        state=user.state,
                        updatedAt=user.updated_at,
                    )
            except traq.ApiException as e:
                print("Exception when calling UserApi->get_users: %s\n" % e)


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def users(request, username):
    check_already_loaded_user_database()
    with traq.ApiClient(configuration=configuration) as api_client:
        api_instance = message_api.MessageApi(api_client)

        try:
            api_response = api_instance.search_messages(
                _from=username, limit=10, sort="createdAt"
            )
            print(api_response)
            return HttpResponse(api_response)
        except traq.ApiException as e:
            print("Exception when calling ActivityApi->get_activity_timeline: %s\n" % e)
