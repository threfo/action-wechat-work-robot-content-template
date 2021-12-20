#!/usr/bin/env python3
import json
from actions_toolkit import core


'''
* [企业微信群机器人配置说明](https://work.weixin.qq.com/api/doc/90000/90136/91770)
* [python action-tools](https://github.com/yanglbme/actions-toolkit)
* [threfo/action-wechat-work-robot](https://github.com/threfo/action-wechat-work-robot)
'''

github = json.loads(core.get_input('context', required=True))
commits = github.get("event", {}).get("commits", [])
action_status_url = f'{github.get("server_url")}/{github.get("repository")}/actions/runs/{github.get("run_id")}'

# 1.generate meta content
# title
md_content_title = f'### 项目：`{github.get("repository")}`\n### 分支：`{github.get("ref_name")}`'
text_content_title = f'项目：{github.get("repository")}\n分支：{github.get("ref_name")}'

# commits info
nl = '\n'
md_content_commits = '\n'.join([f'> <font color=info>[{item.get("id")[:6]}]({item.get("url")})</font>, **{item.get("committer", {}).get("name")}**：<font color=warning>{item.get("message").split(nl)[0]}</font>' for item in commits[:5]])

# build status
md_content_build_status = f'### [查看构建状态]({action_status_url})'
text_content_build_status = f'查看构建状态：{action_status_url}'

# 2.generate all content
# qywechat bot content
md_content_start = f'{md_content_title}\n**开始构建**\n\n{md_content_build_status}'
md_content_success = f'{md_content_title}\n{md_content_commits}\n\n**构建成功**'
# `mentioned_list` must use `msgtype: text`
text_content_fail = f'{text_content_title}\n构建失败/取消\n\n{text_content_build_status}'

# 3.set output
core.set_output("md_content_start", md_content_start)
core.set_output("md_content_success", md_content_success)
core.set_output("text_content_fail", text_content_fail)
