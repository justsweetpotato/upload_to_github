#!/usr/bin/env python
# -*- coding: utf-8 -*-
# heroku 应用激活(每小时, 对应设置在 settings 中.)

import requests
import time


def keep_apps_alive():  # 发送请求, 以持续激活 herokuapp
    url_list = [
        # 公共应用
        "url",  # 这里输入你自己的 herokuapp url
        "url",
        "url",
    ]

    # 开始时间戳
    with open("./../cron_log.txt", 'a') as f:
        f.write("-------- 开始任务, 开始时间: {} --------".format(time.ctime()))
        f.write('\n')

    for url in url_list:
        try:
            with requests.get(url) as r:  # 使用 with 语句确保连接被关闭
                status = r.status_code
        except Exception as e:
            with open("./../cron_log.txt", 'a') as f:
                f.write("app[{}]: {}".format(url_list.index(url) + 1, e))
                f.write('\n')
        else:
            with open("./../cron_log.txt", 'a') as f:
                f.write("app[{}]: {}".format(url_list.index(url) + 1, status))
                f.write('\n')

    # 结束时间戳
    with open("./../cron_log.txt", 'a') as f:
        f.write("-------- 任务结束, 结束时间: {} --------".format(time.ctime()))
        f.write('\n')

    return


if __name__ == '__main__':
    keep_apps_alive()
