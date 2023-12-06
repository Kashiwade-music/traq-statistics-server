import main.modules.utils as utils
import pandas as pd
from rich import print


class UserStatistics:
    def __init__(self, username: str) -> None:
        self.username = username
        self.userid = utils.get_userid_from_username(username)

    def generate_post_frequency_by_time_and_day(
        self, after: str = None, before: str = None
    ):
        messageSearchResult = utils.search_messages_from_db(
            from_=self.userid, after=after, before=before
        )
        for message in messageSearchResult["hits"]:
            message.pop("stamps", None)
        messageDataFrame = pd.DataFrame(messageSearchResult["hits"])
        messageDataFrame["createdAt"] = pd.to_datetime(
            messageDataFrame["createdAt"], utc=True
        ).dt.tz_convert("Asia/Tokyo")
        messageDataFrame["updatedAt"] = pd.to_datetime(
            messageDataFrame["updatedAt"], utc=True
        ).dt.tz_convert("Asia/Tokyo")

        # Initialize result dictionary with zeros
        result_dict = {
            day: [0] * 24
            for day in [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ]
        }

        for index, row in messageDataFrame.iterrows():
            result_dict[row["createdAt"].day_name()][row["createdAt"].hour] += 1

        return result_dict
