from collections import defaultdict
import main.modules.utils as utils
import main.modules.traq as traq
import pandas as pd
from rich import print
import time
import copy


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
            self.__generate_message_dataframe_without_stamps(
                copy.deepcopy(self.messageSearchResult)
            )
        )

    def __generate_message_dataframe_without_stamps(
        self, messageSearchResult: traq.MessageSearch
    ):
        for message in messageSearchResult["hits"]:
            message.pop("stamps", None)
        messageDataFrame = pd.DataFrame(messageSearchResult["hits"])
        messageDataFrame["createdAt"] = pd.to_datetime(
            messageDataFrame["createdAt"], utc=True
        ).dt.tz_convert("Asia/Tokyo")
        messageDataFrame["updatedAt"] = pd.to_datetime(
            messageDataFrame["updatedAt"], utc=True
        ).dt.tz_convert("Asia/Tokyo")

        return messageDataFrame

    def make_statistics(self):
        return {
            "message_ranking_by_stamp_count": self.generate_message_ranking_by_stamp_count(),
            "post_count_transition": self.generate_post_count_transition(),
            "post_frequency_by_time_and_day": self.generate_post_frequency_by_time_and_day(),
        }

    def generate_message_ranking_by_stamp_count(self):
        result_dict = {
            "ranking_by_user_num_who_put_any_stamps": [],  # list[message, user_num]
            "ranking_by_user_num_who_put_the_stamp": [],  # list[dict]
        }

        # "ranking_by_user_num_who_put_the_stamp": [
        #     {
        #       "stampId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        #       "ranking": [
        #         {
        #           "message": {...},
        #           "stamp_count": 0
        #         }
        #       ],
        #     },
        #   ]

        for row in self.messageSearchResult["hits"]:
            stamps_count = len(row["stamps"])
            if stamps_count > 0:
                result_dict["ranking_by_user_num_who_put_any_stamps"].append(
                    [row, stamps_count]
                )

                for stamp in row["stamps"]:
                    stampId_index = next(
                        (
                            i
                            for i, item in enumerate(
                                result_dict["ranking_by_user_num_who_put_the_stamp"]
                            )
                            if item["stampId"] == stamp["stampId"]
                        ),
                        None,
                    )
                    if stampId_index is None:
                        result_dict["ranking_by_user_num_who_put_the_stamp"].append(
                            {
                                "stampId": stamp["stampId"],
                                "ranking": [
                                    {
                                        "message": row,
                                        "stamp_count": 0,
                                    }
                                ],
                            }
                        )
                        stampId_index = (
                            len(result_dict["ranking_by_user_num_who_put_the_stamp"])
                            - 1
                        )

                    ranking_index = next(
                        (
                            i
                            for i, item in enumerate(
                                result_dict["ranking_by_user_num_who_put_the_stamp"][
                                    stampId_index
                                ]["ranking"]
                            )
                            if item["message"]["id"] == row["id"]
                        ),
                        None,
                    )
                    if ranking_index is None:
                        result_dict["ranking_by_user_num_who_put_the_stamp"][
                            stampId_index
                        ]["ranking"].append(
                            {
                                "message": row,
                                "stamp_count": 0,
                            }
                        )
                        ranking_index = (
                            len(
                                result_dict["ranking_by_user_num_who_put_the_stamp"][
                                    stampId_index
                                ]["ranking"]
                            )
                            - 1
                        )
                    result_dict["ranking_by_user_num_who_put_the_stamp"][stampId_index][
                        "ranking"
                    ][ranking_index]["stamp_count"] += 1

        # delete less than 10 stamps
        result_dict["ranking_by_user_num_who_put_any_stamps"] = [
            item
            for item in result_dict["ranking_by_user_num_who_put_any_stamps"]
            if item[1] >= 10
        ]

        delete_indexes = []
        for i, item in enumerate(result_dict["ranking_by_user_num_who_put_the_stamp"]):
            mex_stamp_count = max(
                [ranking_item["stamp_count"] for ranking_item in item["ranking"]]
            )
            if mex_stamp_count < 10:
                delete_indexes.append(i)
        for i in sorted(delete_indexes, reverse=True):
            del result_dict["ranking_by_user_num_who_put_the_stamp"][i]

        # Sort results
        result_dict["ranking_by_user_num_who_put_any_stamps"].sort(
            key=lambda x: x[1], reverse=True
        )

        for item in result_dict["ranking_by_user_num_who_put_the_stamp"]:
            item["ranking"].sort(key=lambda x: x["stamp_count"], reverse=True)

        return result_dict

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
