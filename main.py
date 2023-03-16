from loguru import logger

from src import login, getMedal

if __name__ == "__main__":
    logger.debug("本程序遍历粉丝勋章列表并写入Excel")
    # 获取用户登录状态
    client = login.main()

    # 使用功能
    getMedal.main(client=client)
