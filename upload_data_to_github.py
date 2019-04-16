#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import time
from github3 import login

from .crons import keep_apps_alive


#  返回最新的 log 运行日志
def run_cron():
    keep_apps_alive()

    with open("./../cron_log.txt", "r") as f:
        res = (f.readlines()[-8:])
        res = "".join(res).encode()

    return res


# 连接 github
def connect_to_github():
    gh = login(username="your github id", password="your github password")  # 填入你的用户名和密码
    repo = gh.repository("your github id", "your github repo")  # 填入你的用户名和仓库名
    branch = repo.branch("master")

    return gh, repo, branch


# 保存数据到 github
def upload_result(data):
    data = run_cron()
    gh, repo, branch = connect_to_github()
    remote_path = "{}.txt".format(str(int(time.time()))[-9:])  # 保存日志文件最新一次数据  # 这里根据你的日志格式修改
    repo.create_file(remote_path, "Commit message", base64.b64encode(data))

    return


def main():
    data = run_cron()
    upload_result(data)


if __name__ == '__main__':
    main()
