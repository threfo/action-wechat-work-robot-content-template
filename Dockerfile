FROM python:3.7-slim

RUN pip3 config --global set global.index-url "https://mirrors.aliyun.com/pypi/simple/" \
    && pip3 config --global set install.trusted-host "mirrors.aliyun.com" \
    && pip3 install actions-toolkit

COPY gen_qywechat_bot_message.py /gen_qywechat_bot_message.py

ENTRYPOINT ["/gen_qywechat_bot_message.py"]

