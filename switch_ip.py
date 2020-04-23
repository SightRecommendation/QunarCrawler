import time

import requests

while(1):
    # 要访问的目标页面
    targetUrl = "http://proxy.abuyun.com/switch-ip"
    #targetUrl = "http://proxy.abuyun.com/current-ip"

        # 代理服务器
    proxyHost = "http-cla.abuyun.com"
    proxyPort = "9030"

        # 代理隧道验证信息
    proxyUser = "H2F6B3B5NWZ0SW1C"
    proxyPass = "0369FFFFFCDA2F43"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
        "port" : proxyPort,
        "user" : proxyUser,
        "pass" : proxyPass,
    }

    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }

    resp = requests.get(targetUrl, proxies=proxies)
    time.sleep(1)
