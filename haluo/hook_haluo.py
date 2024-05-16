
import sys
if __name__ == '__main__':
    version_info = sys.version_info
    print("Python 版本：", sys.version[:4])
    try:
        with open("../haluo/"+str(version_info.minor)+".py", "r", encoding="utf-8") as f:
            data = f.read()
            if data:
                exec(data)
    except Exception as e:
        print(e.with_traceback(sys.exc_info()[2]))
        print("Python 版本：", sys.version)
        