from django.shortcuts import render
from django.http import HttpResponse
import main.modules.utils as utils
import main.modules.statistics as statistics
from rich import print


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def users(request, username):
    # utils.get_all_messages_from_traq_and_save_to_db(after="2023-01-01T00:00:00.000Z")
    user_statistics = statistics.UserStatistics(
        username,  # after="2023-01-02T00:00:00.000Z"
    )
    result = user_statistics.make_statistics()
    return HttpResponse(f"{result}")
