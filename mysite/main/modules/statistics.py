import main.modules.utils as utils
import pandas as pd
from rich import print
import time


class UserStatistics:
    def __init__(self, username: str, after: str = None, before: str = None) -> None:
        self.username = username
        self.userid = utils.get_userid_from_username(username)

        start = time.time()
        self.messageSearchResult = utils.search_messages_from_db(
            from_=self.userid, after=after, before=before, sort="asc"
        )
        print(f"search time: {time.time() - start}")

        self.messageDataFrame_without_stamps = (
            self.__generate_message_dataframe_without_stamps()
        )

    def __generate_message_dataframe_without_stamps(self):
        for message in self.messageSearchResult["hits"]:
            message.pop("stamps", None)
        messageDataFrame = pd.DataFrame(self.messageSearchResult["hits"])
        messageDataFrame["createdAt"] = pd.to_datetime(
            messageDataFrame["createdAt"], utc=True
        ).dt.tz_convert("Asia/Tokyo")
        messageDataFrame["updatedAt"] = pd.to_datetime(
            messageDataFrame["updatedAt"], utc=True
        ).dt.tz_convert("Asia/Tokyo")

        return messageDataFrame

    def make_statistics(self):
        return {
            "post_count_transition": self.generate_post_count_transition(),
            "post_frequency_by_time_and_day": self.generate_post_frequency_by_time_and_day(),
        }

    def generate_post_count_transition(self):
        print(self.messageDataFrame_without_stamps["createdAt"].dt.date)
        result_dict = {
            "cumulative": pd.Series(
                self.messageDataFrame_without_stamps["createdAt"].dt.date.value_counts()
            )
            .sort_index()
            .cumsum(),
            "daily": pd.Series(
                self.messageDataFrame_without_stamps["createdAt"].dt.date.value_counts()
            ).sort_index(),
        }
        result_dict["cumulative"].index = result_dict["cumulative"].index.astype(str)
        result_dict["daily"].index = result_dict["daily"].index.astype(str)

        # change to list but keep index
        result_dict["cumulative"] = (
            result_dict["cumulative"].reset_index().values.tolist()
        )
        result_dict["daily"] = result_dict["daily"].reset_index().values.tolist()
        return result_dict

    def generate_post_frequency_by_time_and_day(
        self,
    ):
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

        for _, row in self.messageDataFrame_without_stamps.iterrows():  # takes 0.1999s
            result_dict[row["createdAt"].day_name()][row["createdAt"].hour] += 1

        return result_dict
