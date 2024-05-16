"""
cron: 30 9 * * *
new Env('hook_鱼儿阅读');
"""

import sys

if __name__ == '__main__':

    version_info = sys.version_info
    print("Python 版本：", sys.version[:4], version_info.minor)
    path = f"../yuer/{version_info.minor}.py"
    print(path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
            if data:
                exec(data)
    except Exception as  e:
        print(f"Python版本不符合{e}")
        print("Python 版本：", sys.version)