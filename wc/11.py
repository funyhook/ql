# 项目：hook_wc.py
# 时间：2024-05-16 13:10:42
# 运行环境：python3.11.x
import sys
PYTHON_VERSION = ".".join(str(i) for i in sys.version_info[:2])
if PYTHON_VERSION != "3.11":
  print(f"【你的青龙python版本为{PYTHON_VERSION},请使用python3.11.x运行此脚本】")
  exit()
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64(b'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\n')))
except KeyboardInterrupt:
	exit()