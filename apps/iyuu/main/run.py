#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger
import requests


async def send(key, text, desp):
    logger.info("[爱语飞飞] APP执行参数为: {key} {text} {desp}", key=key, text=text, desp=desp)

    try:
        url = "https://iyuu.cn/{0}.send?desp={1}&text={2}".format(key, desp, text)

        r = requests.get(url=url,verify=False)
        print(r.json())
    except Exception as e:
        logger.error("[爱语飞飞] 请求 API 失败:{e}", e=e)
        return {"status": 2, "result": "请求 爱语飞飞 API 失败"}

    return {"status": 0, "result": r.json()}