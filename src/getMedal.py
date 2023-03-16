import httpx
from loguru import logger

from . import agent, dataHandling

headers = {
    "origin": "https://link.bilibili.com",
    "referer": "https://link.bilibili.com/p/center/index",
    "user-agent": agent.get_user_agents(),
}


def get_fans_medal_list(client: httpx.Client, page: int):
    logger.debug(f"正在遍历第 {page} 页")
    url = "https://api.live.bilibili.com/xlive/app-ucenter/v1/fansMedal/panel"
    params = {
        "page": page,
        "page_size": 10,
    }
    resp = client.get(url=url, params=params, headers=headers)
    all_info = resp.json()
    assert all_info["code"] == 0
    has_more = all_info["data"]["page_info"]["has_more"]
    medal_list: list = all_info["data"]["list"]
    special_list: list = all_info["data"]["special_list"]
    special_list.extend(medal_list)
    return special_list, has_more


@logger.catch
def main(client):
    page = 1
    all_medal_dict = dict()
    while True:
        medal_list, has_more = get_fans_medal_list(client, page)
        if not has_more:
            logger.info("遍历完成")
            break
        all_medal_dict[page] = medal_list
        page += 1
    dataHandling.main(all_medal_dict)
