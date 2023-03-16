from datetime import datetime

import pandas as pd


def main(medal_dict: dict):
    all_medal_list = []
    for page, medal_list in medal_dict.items():
        for i in range(len(medal_list)):
            single_medal_dict = {"page": page, "rank": i + 1}
            single_medal_dict.update(medal_list[i]["anchor_info"])
            single_medal_dict.update(medal_list[i]["medal"])
            single_medal_dict.update(medal_list[i]["room_info"])

            all_medal_list.append(single_medal_dict)

    df = pd.DataFrame(all_medal_list)
    df = df.set_index(["page", "rank"])

    now = datetime.now()
    now_str = now.strftime("%Y.%m.%d_%H-%M-%S")

    df.to_excel(f"MedalList_{now_str}.xlsx", engine="xlsxwriter")
