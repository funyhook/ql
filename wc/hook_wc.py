"""
cron: 0 9 * * *
new Env('app_望潮');
* 反馈群：https://t.me/vhook_wool
"""
import sys
from  utils import notify,common
print(notify.push_config)
print(common.PYTHON_VERSION)
if __name__ == '__main__':

    version_info = sys.version_info
    print("Python 版本：", sys.version[:4], version_info.minor)
    path = f"../wc/{version_info.minor}.py"
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
            if data:
                exec(data)
    except Exception as e:
        print(e.with_traceback())
        print("Python 版本：", sys.version)
