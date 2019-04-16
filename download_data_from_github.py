#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
from github3 import login

log_file_name = ".txt"


# 连接 github
def connect_to_github():
    gh = login(username="your github id", password="your github password")  # 自行修改
    repo = gh.repository("your github id", "your github repo")  # 自行修改
    branch = repo.branch("master")

    return gh, repo, branch


# 拿到 github 上保存的文件
def get_file_contents(filepath):
    gh, repo, branch = connect_to_github()
    tree = branch.commit.commit.tree.to_tree().recurse()

    filename = tree.tree[-1]  # 返回最新一次 commit 的数据  # 根据上传的日志格式自行调整
    if filepath in filename.path:
        print("[*] Found file {}".format(filename.path))
        blob = repo.blob(filename._json_data['sha'])
        return blob.content  # 直接读取文件内容

    return None


# 读取文件到本地
def get_log_contents():
    log_contents = get_file_contents(log_file_name)
    log_contents = base64.b64decode(log_contents)
    log_contents = base64.b64decode(log_contents).decode()

    return log_contents


def main():
    print(get_log_contents())


if __name__ == '__main__':
    main()
