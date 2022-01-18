import ssl
import urllib.request as UR
from env import Env
from switch import Switch


class BaseApi:
    get_env = Env()
    url = get_env.get_env()
    account = get_env.get_account()
    password = get_env.get_pwd()

    def __init__(self, proxy_=None):
        switch = Switch()
        is_switch_on = switch.is_proxy_on()
        if is_switch_on is True:
            # 走代理时，全局取消证书验证，避免报错
            ssl._create_default_https_context = ssl._create_unverified_context
            proxy_ = "127.0.0.1:8080"
        else:
            pass
        if proxy_:
            proxy = {
                "http": 'http://' + proxy_,
                "https": 'http://' + proxy_
            }
        else:
            proxy = None
        proxy_support = UR.ProxyHandler(proxy)
        # build a new opener that adds authentication and caching FTP handlers
        opener = UR.build_opener(proxy_support, UR.CacheFTPHandler)
        # install it
        UR.install_opener(opener)
