# 项目：hook_yuer.py
# 时间：2024-05-16 14:38:06
# 运行环境：python3.11.x
import sys
PYTHON_VERSION = ".".join(str(i) for i in sys.version_info[:2])
if PYTHON_VERSION != "3.11":
  print(f"【你的青龙python版本为{PYTHON_VERSION},请使用python3.11.x运行此脚本】")
  exit()
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(zlib.decompress(b'x\x9c\xad\x9acs%l\xd7\xa6wv\xb2c\xdb\xb6;\xb6m\x1b\x1d\xdb\xb6\xd9a\xc7N\xc7\xb6m\xdbv\xc7\x1d\xa7\xe3d\xee\xe7~\xe7\xa9\x9a\x0fS\xf3iV]k\x1du\xd4\xaa:\xeb\xfa\x01\xcb\x04\xf0\x7f\x14\xd4\xff\xe6}\xe8?#\r`\n0\x05\xb3\x05\xe8\xfc\x0f\xc1t\xc0\xfe%P\x07\xf8/\xc1u\xc0\xff%\x84\x0e\xc4\xbf\x04\xe9\x80\x80\x003\xc8\x7f\x1a`\xfd\xdf\x1c\xc0?\x06f\r\xfd_3\x05\x96\x80\x01\x00\x95`\xff\xf5\xff\x97\x81\xfd\x93\xa9\n\xa0\x01?\xfb\x8f(\xb8\\\xd2\x02\x00\x1f\x9c\xdeZ:\x00\x00\xc4\xf1J\x93\x04\x10@\x02\x86\xf9\xcf\xc6\x95\xe9w\xe1\xde\xf7\x13\xdar}\xc0\xb7@\x16b+\xf1\xae\xfb*|\n(\xfd\x9f\xb42{\xb3\x0b)\x0e*\x08\xfc\x8bR\x0f\x8f\xac\x9bI\xc4\xe0!\xe5?\xdd\xed\x18\xaf\xb0\x8c+\x7fz\xe5\xdd\xef\x15\xd0\xca\xdd\x12&\xf2/\x1bYjs\xf1\x9a\xcb\x8b\x08\'6^H\x88\x19\xa4j\x9b8\xf2\xf2s\xcb\xbe)!\xce\xa1 \xf55zq\xd8?\xa8\x84\xad\xa2\xad *\x10d\xcd\x96\x99\xf7\xbfN\x0bx\x05l\x8f@\xa7[\x965\xc5n\xe4\x99\xca\xeb\xd7\xda\xc5C\xf24E\xb9\x196<\xd9\x9bi\xb2\n\xfaa\xc1\xc3~W(\xa2\xd6\xf1B\\\xd0Es\x9b\x7frh\xbcz|\x8fD_0\x07O&g\xb6\xcfD:IX\x1c\xf0\x0f\xe4\xa8HH\xa8\xd8x\xf67\xeb\xc1\x15\x1d\xda\xd7\xf3\x0f\x97+\xa6y\x7f\xc7\x82w\x95\xae\x8f\x1e\xc06\xf0\x03\x01\xbb\xfa\xd0\xea:Eev$\xde\xe6\x15\xd9t_\xf9\xec\x92\xb8O\x1bG\xf5\xea\x18\xf0}]\x84v\xd5\x054B\x9chKA\xf8\xfa\x08\xdb9N?\xb5V\x85\x9f\xbe03[\xd0\xf3f\xd7\xc3\xf0\xa5-\x7f^E\xf3\x1a\xa1\x9d\x1cx\xd5\xc9{\x02Oxw\xd7o\x80\xe2lt\xeb\xc0\xd45\x0b$\x9df#\xbe\xf9+\x9e\x03\x18\x1b,>\xee.ua{\xe6\xa8\x0471\xa9\xc4\x8bD!\xb6\xeb1\x92\xe2\x14\xc59\xfdY<\x98{s \xa2[@\x0e\xef-\xadai\x08\x12\xa84t\x0bbI\x07N\xe4\xcf\x1e\x95\xa2\x86\xad?\x82L\xc8\'\xa7\xf4\xf8\x88\xb5\xafB\xdf\xab\xd7k\xbdLrsqO\x94\xba==\xae\xa2\xbdc\xdd\'m\xff\xf1\xb4\xd4]\xca\xcc\x15}O\x88\xeaC\xc9\xec\x9ar\x92 \x86\x0b7\x1b*\xab`\x05y\xc1O\xc5D\x9f\x86\x10\xc39\x9cpf\xbfR\xb7{\xe5\xe2\xd8u\x03\xd9\xf7s=\x89\xf7i\xa4\x9c\xc7\xac\xd3\xd7 \xf12\xf7\x9a\xf2}\xce\xbd\xae\x04{W\xf1\xbf\xad\xde\xf5x\x08\xfc\x86I\xf5\xa1\x8c\xaa\xfdZ\x1a\xf4\xf5\x04\xdbJ^7\xbe\xb8\xee\x98\xcfr\x05Ms\xfc\xd2\x03\xa6\x0fEjA_\x80\xcc\x97\xc5\'V\x98\x91\xa8\xb1\x88\xc5qT\x8d$\x1e\xd6\x17\x0f\xf5\x8e\xc5\xee&9E\xaf!*\xeaG;o\x8d\xb1=C\xd7\x01\xb2\x9d\xaeU\xd1\xab~R\xde\xfb\x9a\xa1 \xae\x9fd\xac\xcbN\xbeh\xd9\xf4\xf0\x8f\xbe\xe4\xf0\x93a\x99\xb4\n\xfc5:\x15\xfd\xb4A,\xbb3\xdc\xb7\xe3\xba\x7f\xbcU\xef\xc7\xbe\x11\xe4\xfci\x02\xc3G\xc4UEEI&\x85\x06>\x9d\x05Oo\xc0\xbf\xee~~\x8f>\x8f\n\xc5\x9b5\t\xb5F\x82\x06\x96\xdcj\xb71\xf4\x81^q\x8d\xdf\xcbm2A\x86\xdb\x9c\x071\xe6;c\x97`\xa0\xea.\x08p\xe4\x9f`n\xd7\xfa\x92\x9b\xd4\x032\x87\x1a\xd2\xb1\x10\x1e6\xb2)\x12P\xcd\xad\xf7\x86\x05l\x86\xaf\xf4\x9c\xcd\x8b\xdf8\x04>\xba\xe4\x86\xbdY?\xd3I\xcb\x165\xb7;R\x97\x98g\xd6y\x9c\xfe\x12\xa2\xcd4p3\x9b\xf6{\x13[\x7f>\x99\xdd\xedU\xc5\x02\xb5\xc3=-\\v?\xee\x92\xc2GYC\xb9\x1d\x97\xd1s\xdf\xd5\x13 \x07uZ$N\xe2\x1e!Z~\xad\x8f\xc0\x10/\xb2!\xf3Pb\xee4>\xa8E\x9fQ"\x8d%\x83\xb0\xff\xc8\xc4d\xff\xa8b\xa8\x11K\x07\xc3\xa7\x1f\xf3HD\r<\x93#\xd6\xfb\xbc\x97\x08\xa6\xe9f\x12\'\x98\x08\xb9\xb8U\xdfD\xef\xbbM(\x1dw\xc2\xc0\xab\xff\x1d\xc61\x87tUs\xb4\\q\x8f\xb9\n\xb3\xbamS\xd1g\x88\xea\xa8\x1d\xd4H\x13\xf8\xc2\x13<\x99\x04\xed\xdf\xf0W\x07\x839\x82\x9f^k\x9b\x8d\x0b\x128\xd14\xa5\xc2\x87{i\x01W\xaf{\xf5\x89tV\x91D\xdcq!\xd48\xfb\x81\xd5ZT\xf2\x84\xf8v\xea\x92\xf8\x1c\x84[2\xf4\x08\x89\x8c\xd5\x055\xf3\x9b\xd0\x11\x89\x05 \n\xda\xa5\x95\xbfq\xaf\xe1w\xfb\xb9\xa0c\xa9\x81\xa8,\xf4\xe8\x8b~\xbb\x11\xda\x7f/\x8b@\xb8"\x93\xbd\xe7\xaa\xb1u\xe8tS\xf0\x14\xaf\x87{\xd2=\x9b;\xe0L\x85\xd8\xb98"\xdf%m\xc4\x0f\xc5M\xcd?\xc8\x15\xd5\xb9\xe8\xc1\xacNI\x173~\xfc\xd8,\x97UZ\xe0\xe5\xec\xc3h\x14\xd0\x9f\xbfx\xee\x1f\x91\xd3X\xd2H\xe9\xfe$\xe6\xb6\x8e\xf1\xb2\xa8\xfc\xe4ET|\x97\xfbI\x166\x00\xd0V\xab\xd0\tR\xb0\x1a\xee\xda\x9bH.\xc8\x12\xf2T[Q\x7f\xb1\x84\xa9\'\x89\xe4\x86\xeeuFZ\xf0\x89K\x9b^\xd20f\xd4\x1czA\xfbB\xe8"e\x1a\xbd\xd9N\x9c\xe2\x18/Qyoa\x8e&\x89\xfc;1\xd4$\xd9\xd3\x03\n\xa5Up\xc6\x02\xba\xb68\xa1_\xa3M\xd1\xbe\xe7fj\xba9a\xc1\xc9U\x823\xe9\xd5C\xfb\xf3\xc3\xbc\x12\x13h\xfa,\xb4)\xa1\xdd\x9e/\xbf\xf9\x95\xf0\xd1M\x1f G=4\x9b6\x9a\x8c\x9b\xe3\xc2\xd7s+\xb4\xec>\x8d\x93\xf8N\x97D\x9e\x8bD\xbd\xa2l\x85"\x80\x1at\x96\xb1\xed\xefk>\x0b\x92\x86D\x9a^\x98\xe9P\xf8\x0e\x00\xb742\x8b7\x99\x0fZ\xd5\x9bBO\xb2\xd5\x87>W\x925\x9f\x15c\xea\x89\xaa \xe9\xbe\x9cwd\xad_x\x03\xc8\x0c\xd3/\xccc\x8d\xde\x8ds\xf1\xaf[9\xb2\xbe\x17Y\xe9\xe7+\xc4\xc7\xdf\x04\xfa\x8c(?4\xbd\x19\x1a\xdc\xed.T\xb7(\xc6\x94\xbep+\x8a\xd6D\xea\xff4\xf2R\x84K\xf5$t\x1f\x1f\x97\xf1\xa8!Mk\x18\xb3:\x15rd\xc1\xed\xb4\xbe>8\x1f0\xf4\xfaW\xc2\xa6Y?\x07\x9ea@\xa5\x16\xe1\xcf\xf4\xaf\xd2j\xdf\x90l\xac\xa1)\xdcu\xadB6J\xf1>\x02\x89\x0f\xa5\xc4\x841\xa9\t\x02\x8c\x95:\xcb<\xe4\x12qqN\xce\x975\xd6\x9a\xe8\x14.\x0b3\x87\xb4i\xf5`hk\xf8ck\xa7? .\x7f\xd3\xa2\x88=\x89\x08P+T#~\xa4\xca\xaeW*\xee\x94\xc0\xa7\x97M\x8b}\x8b=\xa7I(@\xe17\xee\x81U\x11(F\xd9\x93Z\'TP\x92\xbe\xaf/\x15\'36i%\xba\xa8\xd0\x8bX\xb4S\xb1.\xad\x02\xf4\xf6\xc1\x86X\xc08\x82\xe8F\xa4\xa0\xc31}w"\xae\xea\x10\xea$\xb2\xa7gP\x19\xdf\x0c3\n\x94w\x923W\xafn\x0c\x8bV\xca\x14\xdfC+\xdd\x82k\x0chv&\xa2zG+|\xc4yx\xfdt\x1a<D\xa8\x10p\xcd\xd3\n\xf4\x96\xab\x0f\xa1\x8f\x19\xf7oL\xf7U\x9dPUo\xedl\x98\xc0\xe1b\xe9\xe7\xd8[\x99\xdf\x96\x1e\xf2\xd5v\x17\xa7\x02\xf7|/0\xc9\xc6\xff\x9e(\xd2 \r,V\xb3\'\xf6B\x842V|\x93\xc3\x17\xd2$\x9c\x8bj\xc2\xec\x9e\xb7\xe3>\xb4\xdc\xed\xb2\x8f\xa0v\x92\xf2\xcal\xac\xee\xc2-\x9b\xf7[:\xe93\xd2=1%\x969R\x8brC\xdd\xa5\xa5\xad/\x14\x9eO^\x17~\x04@\x11\xad\x80\x8c\xab\xdcK/\xadz\xdc\xf3\xb1\xa6~\xc0\xd6v\xca\x15R\xc2\xcd\x91_\x0f\'\x84\x92|\x88\x9a\xfe\xc91<\x14=Hqw@\xbd\x13~x\xfb\x96\x98s\xf3c\xb0\xb3=\x99\xda\xean\x9c\x8b\x9a-\xcc\xf1o\r$\x02\xb7>\xb8\x8fU\xeb\x05M\xb8-\xbd\xf0\x93\xe9\x8cy\x10\xc1\xd4\x1b\xa0\x05\xd5\xf5Cb\xee\\\x173\x9f\xae\xa2\xa6\xcc:R\x90|\xa5\x18T\x11\xabE\xa4\xd4\xd1\xba\x92>\x89ay\x12 \t\xef\x02)(\x84\xfaP\xd9\x1b\x96\x9d\xf8]\x18Li\xb7w\xb9\xe4\xb8\x0f\xc2?\n\xcd\xfa\x00\x8f\x87\xdf\xe7|\xde\x0e\xf5\xb6\xdd\x88\xff\x96\xfa\xed\x8dz\xae\xec\xc6\xf1\xf9ae\x8e\xd9J4\xdeD\xf2\xa9<M\xc2\xbbM\x88\xea\xb8/\xddXm\x98^\xfa\xd0\xe5\xee\xf9\x1c\xba\x89\x1f\xa5Xm\xf7\xb3B\xc3\xa0\x1c_3\x92%2\x1a\xe6(dg1\x81\x9b\x0cq\x1f\xd7O\xaf\xa2\xee\x1ar\xcf\xc9R\xb4\x02UY\xfe\x166\xc6\xd5\xcdE\xd9$\xb2\x01\x16_y\xcca\x88\x04\x96p\xd8\xd4\x8b+\x07#\xc6R\x8c\xa2\xbe\x8e\xac\x16X\xc6X\xc3\xb3E\xcb \xbf\xaaz\xf3\xfd\xb1W\x02\x87\xaa\xe7\x0c\xe1W\xbft[\xe9\xb72\x1em\xb3\x06\x05d`#\xff\x96\x0b\xd8\xaeW\xc1q\xffr.\xa1}\xc3n4$\xdd\x07A\x1cE\xdc\xd5\x0e[\xc2\x00cS\x814z\x80\x0cYT\xdb\xe2\xb0r\r\xdc\x1ce\x05t\xdarx\x8a1E\xbe\x16R\xb6\xe5r\xa08\x9d_\xfc\x13\xd2\x15\xc4V\x96P\x9f\xdd\xf3.\x959g\xe0<\xad5\xf9\x93.\xa2\x8b6\x8b\xed\x94\x92\xaa\x92\x14\xc1\x19\xccF\x0e\rvoB\x86c/\xec\x02\x9fH\xda\x92"\xc7{\xe1}WH/m\xf8\xe8\xa4V\\\xe74\xaf\xc2\x85&\x84\xc8\x98\xff\xef\x07Vd\xd66\x9e\xe1#\x8e/\xd7_&\xa2:\xbb*W\x9d\x18$\x97\xb29k\x0b\xb8\xc0\x9b\xe7L\xf6\xbc\xef\xd1.\x96\xbe\x8f\xa6\x86\xe3\x05\xaaR\xe4P\xcbql\xb6(\xd4\x94\xca\xebB\xc2\xe0\xeeB8\x04e\xacQ\xb05\x9fw\x1c\x04\x9b\xf50\x977\xe8\xb2\x839\xb6\xe4\xa0\x08\x1ba\x8a@\xdc\xc2\xf2\x1f\xc3E\xe62\x8cU\xba\xf7\x11\x99\xbf\xca\xf7\x97\x11F\x1f!C\x8b\xd5L\x18\xe2\xd4p\xe7\xbc\xfa\xc5X3\x92\xfc\xd5h?\xa7\xbf\xaa\xe0&\x8a\x03\x88B\x8c\r\x82\xd9t\x0b\x9cW\xe3\x03\xfar\x1eh\xfb\xfa\x8fD\x95\x7f\xa5OZE\x9f\x0e5\xef\xc9c\xb6v\x81d\x9b\x11q\x85\xad\xcb\xad\xe32\xc5\xa6\xed\xd8/=\xa3<\xde\xc1\xfc:"\xbc\xe3\xf8\xf4\'\xec\x837D\xc5\xda\xe3 \xd3"\x82\x12\xf7\xe5~}i\nx\x91qc\xb6*\xa8OiA:d\x05\x82\x81_\xce@\\R\x03>\x907\x9f\xe8#]\xae\xd7\xd9\x82\x02k*2\xeb\x00r\x80\xc6\xf2\xb8~\xf5\xd1\xdfV\xe3\xbd]\xc1\xb6%5\xf7\xaa\x13P\xb4!|\xbe\x1eq\xbc;=\x8a\xa5\x8d4pm\xdd\xee\x12\\2Sro`Zr\t\x9e-F\xabJ\xa2\xbf\xe9`c\x99\xbaxjZ\x11S^,\xea\xd3\x89A\xdc\xcar\tZ@\xfeX\x82\x83\x85H_\x99e\x8e\xe1f\xa4\xa9U\x00\xc6\x0eM\xaf\xa6\xc9c\xfc;\xfc\x87{\x98$\xc3\xec\x163\x1f\xd9w\x89\xfe\xa3\xbf\xb04\xbd\x8cX\x8d#\x07\xf1\xd1\x18\xd1T\xea5\xba\n\xf6]\xc5\xe1.:T\x13r\xdcP\x18&tzA\xf4\x1bG\x8c\xafo\xe9\x00\xcb\xba`\xb5k\xb7\x17\xba\'\xa1\xc9\xa1\xd8\xf2\x10\x07\xd4H:7\x8bNZ_\x08\xf1\xbb\xcbh\x1f\x9e:\xf1\xf3\x82\xea\x19\xac\x1c6\xe1Q\x83\xec(\xa3\x8b8\xc9\\\xb3=\xb8\xe3\xf1\xfaE<\x02\xa4\x9a\xa2\xc49\xa51\x1c%in\x13\x86\x90\xfeuD\x0b\xdf\x9a\xed\x9fe\xea\xab\xa7g+q\xa4\x8e-r1\xcf\xa5M\x8ea\xc3\xb0\xdf\xd1\x12\x813\xbb\xe7\xa0\x07}\x8f\x1a\xc9\xa0\x89\xbb\x16\x99/#\xbab\x87\x94\xe5\xd7(\xc6jVX\xc8\xbaU\x9cO\xc6{kF\x08\xe6\xe6\xefI\xf2o\x0f\x9c\x95wDs\xb38\xcb\x9f\xf6d<\x9b5\xbe\xca\xf97\xf3\x9f\x8c\xa8\xb2JF\xcdar!p\x88\xac\x1cY\x08\xa9\xd8\x82\x87\xb1\x14\\&\x9d\xd8>\x7f\xb1\x8d\x16\xc2g\x07\x19\xfe\x06\xff\xa9NK\x86\x99\xdc\x1e\x1db\xab{\x0e\xa1\xc6\xead\xba\x9d\x1f\x1e\xc3\xfaU$|x\xae\xb2\xb2\x1f\x8f\x02E0\xe1O\x8e\x0f\xcb\x94\x1b2\xc7\xbf1W\xa5b\xbc\xd7\xe1\x84\xb6\x11\xfe\x82\x9ae*\xe3}\xdf;y,W9\x00\xd7\x9e\x1aO\xd1d\xf17hxi\x1f\xfc~\xd6t\xc5\x16\xe6\xf9\x93\x16\xc6DV\xc59\xe1\xc7\xca\xef\xc2c\xde5\xdf\xd5\xcf\x00\x94\xa9\xe9iF\x0fd|~J\xfeq\xaej\x05\xaes\x0c\xbb\x14s\xc2\x8e\x9dVp\x82\xa6\xc7\xa7\xddx\xe19\x99TZ\xad*\x1d\xef\xf2\xefa\xdd67\x97\xda\x83\x98\xc3b\x12\x13,\xd9\xbf\xbe\xe2-\xf6\x02v\xddw\x13}82\x07\x1c\x8a\xb5R\xfd\xa2S\xef\xc1\x12\xddM\xf3\x90z\xa1~\x9a9\xb3g\x91\x157\xf1\x04%\x1f{Fi\x18\xb9\xcf\xf25}\x9b\x8f\xd6\xf35wQ\x87g\x0e\x18esK\xae\xac\xd6z\xda\x12\x86\xd1\xd7\x829\xdbM\xfe\xa6e\xc3L\xc4\xc4E\x1d\r%,?\xa6T\x16\x0b\xdf\x9a\xf5\xcc\xebB\xa9\xa2\x9bfe\x93\x91$\x02wF\xb6\x0b^\x9b[\xf5\xab\xd9\xb2\xa3E\t\xb3\xb6\xf7\x84\x16x\xb8]\x1c\xc1\x1f\xd7}\x83?\xca\xbd\xc8S\xb2\xb4\x90\x8c\xd6\xb9\x96M\xe2r\xc7|[\xe4\x95y\xd1\x1cZR&\x8d\x05z\x8d51\xad\xe1\x84\x92\xbe\xd8\x1a\x8b\xb4U\xcf*\x0c\x84\xa9\xfc\x9c9\x831\xc9\xda\x98C\xca\x05\xa9\xed<\xab\xe5\x9e\xfb\xe7\xbb\xcf\xe9\x9c0*\x7fXi\xe5\x9a\x81\xe5fI\x11\xcc>[1F\x0c\xeeoe\xe1\x17a\xe2\xbd\\c\xf4\xa4\x9e\xf6c\xb7\xdeg\xcb\x15!\xec\xd8\xce\x98\x18|n\xb3F\x99\x197\xc9W\xcd\xd6##\x84\xf4\x0e\x8a\xebB\xfb\xaf\xda[{\x8c7\x8b<\xc1,\xaf\xd1\xa3\xf6\x17\xb2qs\xf6od\n;\x00^\xb4,\x18C\xfbG=~y\xc6\x95\x85\x92\xbev\x91Oj\x85\xd6D\x1e\xdf\xb8Bb\x13\x7f#\x00\x96\x1eY^G\x96\xae\x9f\x88{\xa1\x13\xeb\xe1\x04\x8c\xff\xc9\x11Y^\xec\xe5\xd3r#\xa4B\xc4\x8d\xb6\x01\xb5\x92\xc2\xf0\x9e!\x01\x894\x8e\x9c"\x87\x1e\xca\xaf<\xf112\xc6\x91/\xf8\xb7\x1b\xed:\xca.\xed\x173\xe4xV\n\xe3\xb1e\x83\xc5$\x04n\xbe\x85\x85L\x862w\xb5\xc3\xad\x9b\xd67\xe7\x91\xacsP\xf5`\n\xe8\xa4\x7f\xb4\xce\x94\\\x1db}\xc3R>\xac\x81h+\xa0@\xf1.\xd4A\xe2c\xe8\xc4\x85\x8enB;"\xc4\xd1\xd4\xa1\xc8\xd3\xd0\x8c`\xac\xec\x1eR"\xe3\xe9\xc4dyYw\xc2\x8e\x1cH\xec\xa6\xdd\xd0?\xf0Nm\xf8\x05}\x9aDLU\xf9\xe2F\xdd.\x17\xe7\xf1%{.\xfb\\s\x8cf~\xc5\xa6\xbf\xa3% Q\xa6\xcd-\xb7\xb6\x97\xe0TN\x85JY\x86\xe3\x93\x12\xbeb\x01\xd6\x8a\xe4\xf3\'\xf1a\xc9\x1b\x15\xeb\x8c?c7\xee\x88\x9a&\x15p~\xc2/\x12\xa4\x02"F\xcc\tB\xc0\xc85\xc1\xc0M\xf4\xf9\x91\x9f\xf6{2)k\xa7\xe9)\xcd`t\x93\xe9\x87\x07\xed\xafz\x9e\xf0\xc5</T\x99\x17\x92\x05vv\xc5y?\x03p8`\xde\x02G#\x93\xc8\xee]5.\xcf\x98\xcc\xb9\xb9z,\x19\x82\x17\x03Ez\xfb\x8d\xb3C\x9bk\x9e\x9a\xf7\xa7\x11,:\xc3Y\xa9\xe87\x88\xba\xfc\xfe~xG\xf4\xc238\x97\xd0Er\x96"[l^\xf1[\x99\rX\xb9-\x021q\xc9}\x0f<W\xe2k\xac\x8b\xfe\xbc\x16\x96OCj\xbb8\xce2?\x172\x12>-\x92\x10\x97%\x11\xe5\xeby\xd4\xc7;fu-N\xa1i{;&[\xf1Y\x16\xe5\xd3O\xd4\xdc\x9d\x1bS\x86=A\xd0|Y\xda\xcfH\x17?\x06\xcc\x03\xd1\xa3\xfa\xf79\x11\xfe\x89\xbd\xa2 w\xcf\rx\xc5\xc7r\xfb\xd8|\xd0\xa1\x14\xf5B1_\x89\x92\x90=\x9cG\t\xe3\x02\xc8Pd\t\xfd\xa1\x1f6#\xee\x14\xfdW\xf6\x9d\x86?;\xceE?\xceI\ryzO\xbc\xf8\xa2\xca\x88\xf3\xfa["\xb6\xe7\x17\xac\xd4\xb8\xf8t\x0e\x116\x93\xcc\x82&\xabyQ\x17c\xcc\xbd\xf4Y?g\x19\x10\x1f\xb1\xfa\r\x89p\xcd\x88*9 @\x07!\x9e\x8dD\xc28\xf5\xda\x11\xca\xc0\n]\xff\xa3z\xae\xc1\x1e\x06\xb1\x8f:\x17\xc9\'\xe4\xb5\xe8\x10r3\x05\xfcs\xc6f^\xaa\x07\x01\xf7\xfb\x1e\xc5\xfa\xa6_\x18[>c{0\xac\x92jq\x1b\x16\'9\xfc%S\xa93\xae\xad\x8b\xb8&\xc2\xf1\x08\xe2rz\x96\xf7\xd8\xbc\x10\xcd\xc0\xe3\x84O\xae]w\xf1\x9e-\xf5\xf0\x92\x1a\xdds\xb6\x8a89\x1d\x98\xd9/\x9e\xddA\xb3O\x87A\xd8\xf0\xa4\xa2\xfe\x8e\'\xc9.\x0fP\xa5U<W\xfd\xd3_\xfe\xd9\x92^\xc7\x1ff\x99\x9b\xe2%@\xde4\xcc\xa6\x1d\xe8oMX*\x82\xacG\xbb\xdd)\xa5\x8fU\xbfC\xeb\xb5\x89\x97;\xa9%7Z\'\x98E\x07\xfbb\xf6\x170\xcf\xdd\xf7\x04r\xdf\xed\xd3,\xa2\x95\xbfo^34\x99{\x96\xda\xc0m\xdb\xe9?\xb3\x9al\xf7 q\x10"q\x8cl-\xff\x18\xa1|\xac9\xdc)\xfe\xf4v\x0f5SY\x88\xfa\xe5\xcc\xc3\x9f\x9cCU=\x97\x93\xa7\xd9\xc0\xf0\'A\xe3\x81\xa0\x8d\xc9\xb7\x1f\xdf\x00\xbd\xd3\xa0@1\xe0\xb8O\x90\xd3\xcf\xfe\xed\xd0\ti\\7\xfd\x07\x03q~\x98\xf6q\xbe\xbd\xcaViA\xdfK5\xee\x04\x86hA\x89\x10\xcd\x05\xf7}\xc6\xabF\xb7\xd7\xc6(\xa1\xa4t\xb0\x16\x82\xd2\xee[\xa4\xf3\x8aG\x86`\xc8\x10h~<$d\xad\x0eP\x10\xdc\xd7\x16\xa7\xfdN\x84\xbb\x87\xbb4U;\x0c\xedrP\xf9\xf4\xcd\xfe\x8d[\xe5\xa7\x1a\x91\x86.\x82\xed\n\xa2\xa7\x12\x88\xacwJ\x89\x0b\xcfmz\xfd\x1e\x8bdi\xbe37\x96\x19#\x04\xcb<b0*0\x1b\xe9\xb4Z~\x18\x81\x05\x03@\xac\x92l\xdbn\xd93!F\xc4)\\\x91\xbd\x8a)\xe3@.\xffu\x8c\x01\xa35lu\x12<Ex\xea}\x1f\x84\x15OG\xad\xf5&K\x838\x82xb\x0eS\xc8\xf1J\x98\x1c\x19\xa0\xc4V\xdd\xc7\x92\xd6\x83\xcb&\x1d\xbd\xeb\xa8\x90\x85\x86\x91}\xd0\xa8\tC\t\xd2i\r\xc3Q\x90\xe1\xa2\xfd\xf5p\xbd\xa3\x9d\xc3\r\xb1\xc2\x87n\x1b\xf0\xb7kV\x92yj\xf0\xde\xd8\xf0\x943\xbe>\xc3&m?\xa0\xb7\x9f\xe8m\xda\xa8\xc6y\xec!+\x1f\x1b~{\xd482\xfd\xe5+SL\xfbM\xcf3zG\x87\xd3!F\xe9$\x0e\x12\x01F\xe6H\x82\xeb\xed\x8d\xf6!\xcc\x04\xe1\x96\x85\xc9H\x18wi\xee\x8bT\x1b\xe1[\xc7@Z\xcb\xf2X\xd9\xd8\x0b\xd9\xd4\x16\x01\xaa\x0f\xd8\x8e3\xd9Q\xb4"\x10\xd49\xd2\xe7\xf1!\'\xfb\x98\xeae4L|\xdd\xfcP\x98\xdc\x17\\\x07d4\x92?\xc8\x93D\xe5\x96\x0b\xaadBS\xce\x80\x8a\xb9\xa4\x84\x84t4\x82_\xa1\x8af1Q\xbe \xf5\xfb\xa1\x1c\xdb~\xbf\xdd\x0e}e\x9f|\x8e\xe9$\re\xc8\xe0\x0eO\xc4\xf7\x1a\xf7&\xdbx\xd4\xaa5\xfe\xceQ\x82\xa8\xd2X\xb9\x1d\xc2I\x91\x8e\xde\xb6\xf0\xd0+\x16\x0eH\x96W\xfd3\x90\x8c6\xa6\xd1T\xa7/\xd6\xefu\x97I\xc7\x12i^D\xe4\xc9\xc9\x16P\xf74\x1c\xad\x00\xcb>\x95\x80\xd8\x0f&\x9dGo}:\xff&x\x98{z[{\x80\xf5\n\xd6as\t>\xc9mC\x87i\xa9w\xebx.\x81@\xd5\x8c;\x86\x14\x9f\xae`\x85O@\xd6\x132B\xd2Z\xee\x00P\x8a\x96\xcc\nlK\\\xe61\xfdEd\xbe\xa9\x92\x90\xf7\x859\xa6\x17\x81\x17\x07\x1b5u\xbdt\x1d\xec\x95\xc2P\x07\xdb\xaf\xc2=\xa4\xe7\x1f\xba\x9e\xef\xe3V\xcbTVkk\xf4\xb8\x00M\xa8\x9c\x00:]&\x15\xce\x1d\r\x9c\x98\x0b\x96x`0z\x88\x82\x9c\xa3\xbe\xc4)\xb5\xa3\xd7e\xc50\x12\xbe\x0f\xa3\xfdm\\\xf7k\xe8\x82\xc9\xdd\xccO6J\xd5+\xd3\xad\xeb\xfc\xc7V\xc3\\\xbar\x99\xbb.[\x82^\x9c]\xd6\x01\x89\'\xab\x8e/\xda\xe9\xbbZ\xba\x01\x86\x96\xc5\xa6x\\e\tC\x06\xa8/m\xd9\x85\x10\xb6\xcf\xe7\x85B\x05\xdc\xd7t\xec\xa4\xe5U;d\x9d\x17\xde6\x9b\xe9\xcbj\xc3[_=\xb9:\xd3\xf2\xf9s\xcc\xe7Tv\xaa\x1e\xb6\xb9\xbat\xc1\xe1n\x8e\xbd\x13\xeb\xf8|<\x19\xa6\x93\xb0\x18/eQ\xae\x12\xdex\x90\xc5\xbd\xc6\x81\x98Jz\x9b\xad\xc74\xea\x11\x9a1\x94\x91G\xf0\x12\x8a\xae\xa0\xf9g\xac\xa0\xb1V\xb0i\xb27m<\x13!\xb8\xef\xaa\xdf\xa5\xce\xf0\x05\x17\x8f\xda\xa0=\xce\xba\x80\xe35]\x88Q\xe7\x8c\xc8\x8e\xdd&\xae\xa5\xff\xb3\x8a\x9a\x890|\xf5\xf7\nZ\x12\xa3\xf6\xc0\x853I\x1a_\x8d\xb2\x9cb\xee^\xae(;\xe2B\xe5\x0e\xa9\xa0\xc7\x11\xe8\xf9\x9a\xfa\xa1]\x96\xab\x9d\xed\x94\xde\xd2{\x18\xfa\xeb\xeaw\x14\x9eGJ.;3\x05q\xf3a,\xff\xb7N\xb2\xac\x1f#\x1b\xf1\x02\xc0"\xf3\x8b\xe6\xc3A"\x8f<\xbaz\x1cE\x8f\xb0P2\xe7\x17O@Quw\xe1\xb4\xa9[\xa4\xc0\xab\x1a\x8dg\x00R\x854\x1f\xb9\x8f\xf5+K\x92F\xe6#\xe4\xc1\xf5M\xdc \xe9\xe2\xc0\x022\xcb\x9b\x0b#\xfaG=\x08\xdfl#\x9ep\x84\x07\xb5_\xec\xa8\x98\xc3\xb8\xcb\xcd\xf2\x88\x87j\x89K~\xcb\xa3\x82\xb7\xfb\xe5"\xbe\x0b\xd0\x1a\xb7\xd9\xb65\xd0Fi\xca25\x1aC\xc3.\x02\xef\'N\xb2\x90\xd1`z\x97\xe3\xca\xc6\x9cb\xed\xefNI\xe0T\xd7`\x96\x17\x9c\x8at\x11/\xad\x9c@-qx\xa2\xb8\x81<\x8d\xeb\x7f\xbd\x14\x9e6I<s\x99\xe4\x00]\xab\xe2}qb\x0bt\x1dt\x13Pv\x92\xd4P\xcf\xf7\xab\x95\x02NQ\xf8Er\x9bs\xc4\n\xafd\xf1C\x16\xf1\xe2\x8a\xbb\x0bu\xe3\'MJ\xd7 a\xb3\xc9\xae\xaa\x17\xfbQ^\x86\xf2\x8f\x96Ll\xe2"\xf4\xde\xcfw\xc42\x8d\x05\xf1\x12\xe4\xd7\xf5\xa2\x01k\x88\x9fK\na\xff\xd6m\x1b\x83\xe05\xc8\x0c\xae!\xdd\xe2n9\xfa=\x90\xdd\x948\xce\'^\xa8\xdf>c\xab\xe4\xcb\x9bFg24\xa4\xd8?\xc2w\xfcyP`M\x05Fg~\xbf~\x87/\xef\xac\xb5\xdb\xe2\x08\xa5R\x19\xde\xb6\xdaw\xe0G\xe6\x993\xb3y\xabe\xa3/\xb19\xa5\xd2\xb1\x80\x14\x1ce\xfc\xf5\xf2@\x19u\xcf\x06o\x1d\xa2\xe8\xa8\xc1-\x9f\x7f\xd6X\xc4Gq\x7f\xab\xf9\x89\x90\xed\xae\xe6\x13 \xfd\xd0\no\x9a\xfc.[\xeb\xed\x9f\xb4\xc8\x91>\xfbu"\x1c\x031o\x99r\r\x81`|s:|\x8f\xd9\xc6\xbf*\xf8Eo:\xee\xd8V\x01\xa86<\x9d"u\x96\x1bt\xf4\xd3\x94\xd2\x8c\x80\x82+\xc4\t\xd4\xb0\xb2\x0c\xd3\x86\xb3QM\x8d\xa0\xc8C\xd8\xfb#\x0e!\xbd\x0cib\x0c\xear\x9d\xa3\xbe\xf7\x16\xf2\xca.\xb8\xedC\xae\x12W\x19R4\xaby\x99l\x9c\xb1\xfa\\\x07\xd7\xfd\xb9\x11Th\x05\xc6C\xb8V\x15\xb7\x85t\xe1\x149\\{>\xda\x16\x1fU\\b\x98 \xad\x8cY6zq\xc2\xb5\xfa\xa3\x8a\x8f\xcb!\x9dlY\xee\xf2\xf3P\xc4\x94M_J\xdc\x18S\x8b\xdc!\xad]K\xf2\x19\xba\\\xeb\xef\x04\x12\x0b=\xbf;\xa7\x8f\xa1[:5OS\x8b]m\x98\xf1\xc2:\xac\x0f>"\x95\xfd\x15\xaf\x90\xa3pw\x96\x8c\xb5z;\xf3\xfbt\xbf\x10U\xca\xf4\x8a\xe4"\x0fmnI?<\xc5P\xae\x025\xf7:\x8a\n\x93\xd6\x13!\xd2a\x960Y\xe50\xcbX\xb5K\x1e\x84am\xa93\x16\x96\x9f\x94f\x96\xa8\x90\x0e\xca[v4\xfc\xf71o\x06v\x97u5-\x91\xd9J\x1c\xeb=\xe2\xf4\x89\xde\xa2c\xf34\x81M\xd9\xe7\xa1g\x0f/D\x128\xbfI\x80[Zf\xe2V\x1d\x84mI;\x0cX\x0b\xfah|\xf3)\xce\x1f5p z\x8eFN(\x96d\x88\xa4\xe3\xa8\xbb\xc1np~\xeb\xce\x92\x90q\xb3\x90\x86=\x96\x8fd\x10P\xff\xdd~\xf4\xc1QJ\xf6\xc2\x08\xbf*\xd1\xe4\x03X;\x8a\xe5\xde\xae\xb6\x15\x90\xa8\x1a\x8e6U\xd22\xb1\xfc\xc2&,;la9\xc6\xf3s\xe4\xcb\xd1f\xee\xb7\xe1kh@%\x15\x1e\xe5\xb3\x87@\xe3\xdcb:oL\xc6\x1agE_j\x06\xa4%\x0c\x8b\xfbq\xbd\xe6\xd2d\xc2\x0f\xf9|6\xa7\xd8-\xa5`\x83\xd1"!:>\xe8C\xd5\'\xb4\x88 \x1d\xafl\xc2S\x04S\xe0\xc3\x1cbo\xee\xfd\x91\x81\xec\x12\xc8fx\xd8\x1e\xc3\xd3\xa0<\xba\xa9O\xf5\xec\xa2\xaf3d\xfb\xb1\xd6r\x8d\x81|\xd5\x86\x0fk\xad\xf2Ua`\xe8`B,\xf1\xa8\xaef\xd4\x02.\xcdJ\xf62\x8e\xc2X]\xa4SnWK\xbe\xc5\xa9\xc6\xf9^7t\x19]\xd7t\xa9\x83\x9cZWn\xfbs-\xff/\xc5\x90\xc6\xc2\xdd\x81\x81g@>U\xb9\xb4\xdb*\x19\xd7/"\xb7 \xf9)\xa8v\xa3\x82\xae\xa2\xc8)\xb8q7*.d\x91\xc3ME)\xfe\x9b\xdf2r+\x83\x01\x1e\xa7\x9b^J%9\x10\xae\xee\xcf\x0es\xd7\xab\xa2\x8c\xa2]\x0b\xd4pq\x03_A\'[!8f\xb2\xbcr\x1c1:!\xe9\x1b\xd2$\xe6DP\xf4\r\xaez/\x96\x06\x14\xed%\xaa\x9e\xb8\xc4J!?\x9fpx\xbe\x94\xa8\xb2\x8c\xa1\xdb\x1c\xe6\xf2/\xc9\xcdM\xe9\x08\xa7\xb5\xddnZJ\xfe\x90\']?k{\xff\xe9T\x17\xa3\xa6\xe9\xea\xa5\xe2\xea\xf8]\r\xf3c\xf8\xbb\xaeH,2\x1f\xa9\x13\xa2\xf7\x98\x90\xd3\xc6Ee&`\x920\xbe\xf8\xd8\x06\xcf\x16\xcfy\x14\xe45\x84\x81\xbeC\xd4\xa4]\x8a\x90\xce\xdfbwU\xd8"}NI\xe1e+\xc5\x92X\x0f\x8eC\x99p\x19\xed\x8fK\x89\xca\xcb\xee\xe6H\x91r\xb8\x0c5\rj\x80\xb43tu\xdd\xbcd\tP\xc0\x1a"\x88\x8d#\xb2snj\x84\xad\x04\xd3\xef\xab4p\x99R\x13q\x90\xf9\x88\xa1\x9dF!x\xff\n\xbc\xf4A\x88k\xa5Y\x18\xdf\xd3u\x97\xb7\x0c\xc1\x15\xcdh\xe5\xf0\x9c\xe0I=H\xdc\x7f`~\xb8\xdb#=\xc3\x0b\x07\x16\xfd9+7\xcb\xbc\x04\x8e\xad\x98\x99:\xb5r6\xd3rh\xf7\xf9\x86\x01m\xf9\x13j\x90\x04\xbc\xbf\xdf\xfa+\xa3\xda\xde|\x07\xf3I\x8aM\xcd9\x82\x15<\x9a\xf0=&7@1z\xc3M\x8bu\xc2\x16%\x1a\xe3T\xa3<J\x9f\x067\x04b\xfc(=Jm\xbfn\xdcY&\xb0\xe1\x91\x85\x99\xfak\xae\xb9\xc1\xd9-\x94-\xc91J#G\xb4\xc4\x8cB0%7\xfe\xe5\xbf\x0e\x96:\x8e\xfcx\x0b\xe0\xd4\xb4(W\x89)\x08\xa8>\x91\x10\xe2\x90\xb7\xb5\xf1\xbfF\xba\xcfVM\xf1y\x97^b\x89\xf0\xde\xe8\x92v\x84-\x14\xa4\xceWQ\x1e\xb03\x02\xf2bg\xb9\xd3\\\xb1ax\x1a)\xbd-5\x0f"\x86\x0f\xcb\x99Q6H\xc6|W\xe3\x93\xc37eP\xf9.\xc7\xae:#\xdf\t6\x91]\xe6\xe7\xca\xc9\xaeQ\xa7i]7$\x94\xf3\xc6\xc6!\xf1\xcd\xbcj\x89\xb0\x86\xdd\xd5\x1aY\xce\x88"\x92#v&\x8f\x9b\xc4\xdcZ\xf7\x98\x934\x90\x91\x0e\xa2\x10\xfbV=>\x9a?O\xe5\xe5\x04?\xa8\xd5\x93-M\x1eJ\xd5\x11\x98\x96\xa1\xdd\xd9\x80Ry0\xa5\xe0\t\xc3\xb4&uW\xfd\xb6\xf0=K\xcc\xfc}\n\x9b\xf8\xb3\xc3p^\xc57\t)\xb2i\xeb\x82\x96\xec2\xa1\x80\xd4o\x89\xef\xd4\xbd.u\xb3\xd5m\xe3l\x8d=\xca\xa5\x9e\xaf~&;\x89\xd2f:\xe9 \xe6z\x9a\xc1\x88\x9b\xe1]\xcc\xd5\x19+N\xca3z\xd0\x13\xcb\x94\xa1\xbb\xc8\x93D\x9d\xc4y\x0c\xce\x8d\xaf^o\x97\x99\xe1\x1d2g\xd9&\x12\x0c\xc7\xdb\x0f\xe1c\xbf?\x95\xca\x8bg2\x89\xfc\xbc\xea\xe7\x9c\xb0\xb0j\xae\xe5\xec\xe1a\xb5T\x05\x8c\xd7W\xdcX\x86\x1ei\xb4\xea\xe1\xd2\x07\xb9\xcf\x08+-\x1d\xf2\\\x81\x02\xe5ygC(\x86\x0b\xea\xd7Wu\xd3\x9em\x9b\xd4\x11\xee\xa1\xd0\x96n\xb9K\x1f.8\xc9\x90\xd7\xee\xf0\xdem\xeeK~\x98\x17\xe4\xaf\xde8i\xf7( Ex\x02\xf7_]\x89g\xd2\xa3\x0f\xf0\xcc\x8a\xe6\x80k\xd5,\xc5#s\xa4\x9c\xfd;\x05M\xe3\xc8#Wr\x93\xa6\xfa\xf2 A\xe5\x1a\xf9\xb5\xdf\x03Z\xfa\xeb>\xce+\x87s\x9b\x90\x9b\xc3F\xa3\xa8\xfcT\xfek\xfa\xb0\xec\xbd\xdaV\xd3h\x89\x02\xb4\xa6\xe5\xe5\xfa)\xaaXx\xbd\xbb\x93\x93\xab\x8d-\x04\xb5%5\xe5\xf4\x88\x9f\xd0\xc7[\x07\xfb#\xdd?\x08\x1e\x9b\xbf\xc8Q*\x19\x17\xf6\xc7\x03\xb1)O\xfd:\x95_y\xf1\xde\xe4\x83F)\xd5L~\xe9\xac\xfe\x12\x8ft\xbc\xf5}G\xfa\xca\xaf/\xe6\xc1\r$3\x15MA0\xde"A\x16\xcc&\xa7\x98\x98BA\x96)\xcd2E\x08\xa0\x886\x16\xb6\xf0\xc6\xf3\xe9\xde1.\xf1\xcai\xf5\x16\xb5c7\x11\xc0\xc6\xec\xebv\xaf\x7f\xfd\x01\x0e\xb2\xd6\x15\x14\xd4\xb9\xd8\xf5i\xff}<L\xae\x12L\x94\xcc-\xd5\xdd\xa1r*\x85J|3\xb2\xb7t\x07U\xb9K\xa4\xd3\xe8\xb1B\xa7`1\x12DE\xd1~\xf9CT#1\xf2\x9a\xce\x99\x08\xb5\xea`\x88\xba$\xa4\x8d\n\x05\xaby\x11\xc0\xe8,\xe8rp%\x83-\x01\x1a\t\x1f`\xa8*2\xcd(C\x91\x9d\xd4\xa9\x18\x82\x02\xcb.\xed\xe5\x9a\xefqzS\xf9\xfeW\xec\xf6\xd2\x93\xbe\xf7\x0b\x9b\'\x94\x8a\x814\xd1\xc0\xf7\xa7v\xa3\x11>\xc0\xb5yt2\xcd\xb1p\x8d\xd6\xb5O\xac\xff\xb1~\xfc#\x9c\xce\x05\x023\x05\x17\n\xe8\x0c\xfb\x1aWa\x8bG\x00\x06aM\xec@\n\xca\\o\xe2\xe3\x9b\x85\xcc\x9fw\x13(\xe8Q\x8b#=g\xebg{\xf1/2\t\xbd.\xc5\x19\xa7\xf1\x96\xe3\xe6!]\xae\xf0\xe5uD1?M\xa1\xb6\x91k\x81\'"\x7f\xde\xb9\xb2\xca>\xdes\xa9\xf7\x1b\xd7R|P\xb5k\xc9R2V7\xd1\x8cl\xcd7Oc\x9dP\xf2S\xd3I+F\xaef|\x13\xfa\x04\xba9-tc\x91\xc5\x15\x95~\xbce\xd9TY\xfb.\x18@Tj\xee)\xd9\xaaR\xb3.c\x02(Tp\x7f$v\xda?\xe7\x8dS\xe4\xf5\x13\xa1\xa2-L\xf4\xa1\x9ak\xc4TC\xd9\xdf\xc3\xd3\xb9\x82\xd3E\x8a\xa5\x0cho\x80\xd2\xf1\x9b\xde\xc8\xa8}\xa5\xa9\xbb\x91r^\x8b\xaa\xfb+\x03Nn$\x05:\xda\x8fS\xc9 2S\xcc\x9bV\xce\x11\x13\xb9\xc5N=\xf6(j\xc5\x04=N~\xa9\x06v?M\xe7\t\x07GG;\x15\xf3Br5F]G\xb7\xbc\xdfc\x12\xda\xe4\x83;:tTLF\xdd\xb3`R\'v\xc0\xfa\xf0V\xf6\xe1\xb4\x8b\xd4\xce\xa7V#\x10\x13\x07\x05\xb1\x99RS\x8br8\xf1D\x83\x8c\x89#\xf4\\\x1e\xfd2\xdbFk\x86}>KW+XY\x8f\xa8)x\x97@\x12\x04U?\x9d\xd0\xc1\xce\xcfgt\xb7`\xe8\xce\xa1\xe96 \xe6H\xd1`\xd6 \rL\x11e\x9c\x1ez\xaa/p)\xcf.\xe4\x14\x1d\x01\xe7\x03\xb1\r\x00\xd9|0\xb0\x1b\x9c\xc9(\xda\x03\x1cU\xdb3\xa0\xd93\xab\xcb\x90`X\xbaZ\xdb\xcc\xb7\xcdlw\x81\x8d\xe9\n\xf4\x93\x03\xaa\x9d\x83_\x8a\x07\xc8\x14\x87~\xfeH8\xf71\xf0D\xca\xbc\x91\xd8\xfa4\xc9\xcd\xf4OO\x93\xbc)\xda\xc6SG\xf8\xe3\xbewU\xb8\xcc\x0f\xdb\x80\xb1\xa5\xab\x8a\xd0\xa8\xd9\xd3\x17~W\x8e\x10\xfd\x99\x98\xfa\xc37L\xca?\xd2]q\xf2/\xcclH{|\xb1\xa1\x9a\x9e7"\x0e\x9f\x1e\x14\xce\xdf\xf5!Bo\x04\xfbd\xbdV[\x8f\xf0I\x19\xd5\xadw\xe5w\x9c\xa1\x86\x9cn2d\xee\xd5\x05a\xd0P\xb4\x9c\x1d\x1b\x1b\x05\xf0\xbak\xf3\x10\x10#V\x02\x81\x9a\x87\xd9\xd2\x91\x9f7{\xd4\x1a\xe1\x8d\x1e\xe0\xaf#w\'4\xdc\xf4h\x93\xb2!R0\xeb\xcd\xd5\xc5_\r\x87\x84\x9c\x04\x90\xd8\xceY\xd1r9\'1\x14r` \xca\x83f|\xf9\x1e\xc7\xdc\xb0\x0f9i,t\x1b\x9d\xe0^\x7f\xc0\xbc#\xd8\x8a\xc3o\x19\xce6\xa7f\x10\xca_\xb0\xd0G\x15#\xfa=\x13\xc8\xa3\xc6Z\xc1\xe8|\x8b\x18\xfe\xc0\xbf&\xcf\xd98=\xdc\xb8\xef\xc5\xe4\xbc_\x08.\xf0\x0f\xd3\xfb\xfa\xc36\xa6\x1b\xa5\x1e\xe1\xa9\xa8E\xf1k\xed\x9c0\x915\xe0\xd6\xe9\xf6-?\xcc\xd7P\xfb\x87\xe8\xa8\xaa\x05\xe6 :\xc8\xd5]rtP$\xbf\xe4\x04\x97pV \xdb}-\x99\xff\x1e}\x9f\xa9z\xdeF\xd0x\xd4!A\xd5\x16g>\xc4\xa1\x0cm\x148\xc6\xedxRtkR9\x1c\rdtki\xda\x90\xf5)z\xf5nl\x88\x81lU\x0ea\x1cz\xe0U\xa4\xbb\xfb\\\xab\x80\xaaX\x08p[\xb6xl*z\xb4\x95wv\xb5\xffFD{\x14w\xff\xa2po9\xc2A\xf1\xe0\xd2\x89\x06u\xb6\x90[t<\xb1\x8ar\x043"\x8a\xd9]\x8f1\xb5\xb8\xc7\xdf\xa0n&\xc3\xdf\x82\xee-o\xba\xb7$\x07\x9a\xb3\xe0\xd43\xc2\xbb\xca\xec\xd7\xc4\xd8\x04\xcc\xd8\x04\x92\xae2\xc1/\xb6;B\x92\x9d\x12\x80tb\x90\xbf\x9d\xbd^\xbd\xe7;\xde\xf9\xc7\x87\xdf\xa6\xecC\xbc\x1e\x01\xc0R8\xbb\xef\xdb\xbb6KV|\x91Ig\xa8i\xe3\x18T\x08\xd6\xd8\xd0HA\xfd\xfc2\xec\x9d\xa9\x9e\x11>\x14b\xfcD.\xc9\x0bb\x88Z\xb2\x96\xc9\xec2\xd4\xe1\x98,\x94\x8be\xd1"\xefB\xec\x91+\xe4M\x19\xc0\x1e\xddi\xf0A\x0f\xe2\xc4H\xd9.\x0e\x9e\xa0oD\xe8\x18}<\xc6\x8a\xf1\xe2\xa1\xbe\x1d\xce\xad\x17\xcci{\xd5bn[\xea\x85\x15n\xcf|s\x1d\x91\xd6\xccy>\xbf\xcb$\x00|\x93%\xe0h\x01N\xfa7\x91V\xf38\x8c\xcf\xeeu|\x83\xd8\x18\ns)N5\xd4\xb5(\xb5\x13\xb5\xa4s\x9a\xa6I\xf9\x97\xd6\x1d\xcd\x9d\xd2\xd3u\xc7F\xe5\x99\xae\x1a\x15\xdex\xbb\x7f\x8dwm\xe8F\x85\xc5\xf2\x9c\xd1\x0c\x9d\x1d\x8ad\xae\xeb\xa2{28\x825gD|\xb9\x1al\xfb\xbc\xd3\x8d\x12\x98\x075\x95C\xe0&Z\xe4\xb37\xda,( [\xeb\xda\xa6,]M~\x8b\xc6\xb9\xaf\xea\xe3\x0e\x8a\xe3\x1d\xafJ\x93\xc1c\xa9$\xa0\xcb\xaa\x8a\xbf!\x1c[\x1d#~<\xc06B\x7fa\xde\xf1\x95\x1fK\xbby\xa8\xaa\xa8z"\xae\xe0hZ}\x01T\x19,Y\xec\xeb\x1c\xd7x\xc0_\xe4\xa1\xb8\xc8wt\x03\xa4im\xeeYf\xd3/\x10\xe1\xf2_\x07\xb2\x02l\xbe\x11\x9cH\\0\x13\xa7\x9b\xb7\x1e\x97\xeb\xe5b\x18\xd8R\xe6\xb5\x98\x16\x00CH\xd2e\x0b\x99\xe4\xfb\\\x173BR\xc3\xba)>\xa5|\x1cgl\xe6\xd8\xab\xcb\xd4\x10r\xf0\x7f&\xa2\xe9\x86I\xa9\\\xc0J{\xc6\xd5\xa5\x93\x00\xa3\xc224\x83ybJ\xcczp>\xaf\xe8\xe7D\xfc\xc0k\x10~\xe0,\x90@/Y\x9d\x8e#@\x97\xef\x9d<\xe6\xdd\xe3hD.\x0cT\xf4\xb1\x80\xc09\xae\x18\\:+h\x8d\x0f]pJ\xd0weK\x13\x96\x17\xd2N-\x00\xc3dh\xb4Q\xc6\xe1w\xbb\x11\xe1\x99Yv\xaew\xef\xcd\x1db{\x10\xd9)\xb4\'\x1f\xee(\x02x\x91I\xa3"7\x8f\x89\xcbgd\xc0\xdf\xa8[a*\xaa\xc8]\x98\xf9\x87U{=0\xa4\xbe\xe7\xd6m$wKf\x86\xbc\xba"\x1c\xbe\xd5h\x88R+\x82z\xab\x04\xab$I\x82m!\xdf\x97\xd7\xf1{\x14\xad\xfa\xc6J\x8bm\xf0\xda\xda"`\x03\x10q:\x1d\x92\x9f\x03AT\xad\xe9\x1c\x0e\xc2\xe6\x14Q6#z4\r\x922\xf6\xcfg\x90\xdd\x9e?\x7f\xf88[\x89r\x8d\x1d"B\xdb\x18\x85KO\xf6r\x00\xd4\xcb<\xf1v^\x1ed\x81\xb3\x88\xd0\xcc)\xe4\x7fYom\xc1\x97\xa03|2\x9do\xd4\xd43\xd3\x1c\x16\xe5\xda\x1dx\xae6R\x8f\xb6\xde^\x8a\x91p\xe4}\x9fW\x84\x172D\xb5s\x80\xa7\xcb\x99>\xfd4\xab\x14Bi\xa9\x91y\xb9\x05\xacA!\xe9\x91\xfdy\xf4\x02\xf4Nl\xa8/\xf2\x8e\xf5l;\x9a\xce\x87|o\x87\x11f\xb6\x9f0t/ \x19\xe2\xa83%\xf5\xb4\xe6\x15\xfe\xf2\xe3V\xde\x91\xfc\x95j\x94\xf5\xcc\xd1\x85\xe3\x0c\x82\n[Y9a\x11\x94\xbc\x03\xb8\xb2$\r\x92\xc4Is\x0b\xecz\xc6=#\xf0t\xf7\xf7\xdf\x7f\x82.\xedPyH\x06m\xbf\x1eS\xa6\xb3\x1bjc\x0b\xf5\x15\x18\n\x1a\rj\x87\x1f\xb5\xfa\x96\xf13\x96\x17\xc4.\xa67\xd8\xcd\xef,\x88 \x19\x18\x8au\x8d\x1a\xcd\xa2\xb4g\xc2\xc5\x8d[6\x89\xe0 \xe1\xbc\x12\x82\xd1V4x\x05\xd1\x9e\x93\x0b\xbf\xb2\x1c\x1e\x82\x15}\xf1\xa1\x03\xae7_2\xb4\xd8h\xdc\xc0M\x91\xd2\xcaI\x98\xb7\x17R%*\'\x92\xfe:\xe4?\xd0Jo\xd3\xcd\xf0\x0c\x1cY\xc2%`\xe5\xc7\xc4#\x84\xe5\xf1\x89\xf4\xab\xad\xb1h\'\xbb\x1c\xe0\x0cc\xa7\xd3<\x1c\x96 \xd79\xe4\xe5A\x91\xd4\x0f\xe7\xcb\x82y\n\xd3\xe6y\\-\xd7V\\\xc4\x18\xad|\xe1\xdf\xdcH~\xe3\x89m\xb8-{\xca\xb7:\x02\x9b\xa2\x01W\xf5\r\xe5h\\\xae\\G\xc6\xc1\x15\x0b\x8b[&\xbb\xa1\x03;q&\xafw\xea\xe7\x9ak2fN\tpO)\x1b\'\'\x95\xaa\xb4b\x9cG\x89\xba\x03\x16\xe7C\xdfD\xd0\xa0\xa02\xdb\r.\xde\xee1\x88S,\x95\xb9\x93C\xe3#\xaf#\x18\x96\xd6\xdcJ\x87\xab\xee\xda\xf7O\xf3\x17;_\xb7)?\x95a.\xbc\xa3\xb2\xa6\xcb&U5\xc2m\x9f\x85\xa0\x98\xb86\x9d\x93\xf6\xa5\x1f\xfd\x82\xe9o\xb0\xf2\xfe\xb6Bf(\xef\xc5\xe0\x8d\xb5y\xd3\xf4\x87\x9f\x86\xf6\xc9\xc8\x95gY\xd8U\xae\xda\x9d\xaf\x19\x01\xa9Dc\xab\x1e\xfd=\x8d\x17\xdc\x90\x1f\xbd=\xaf\xe3\xae\xc8\xbd\x8ap\xe3g\xc3\xd2\xf6\x88i\x9c\xaag\x8d\xc5\xc0\xd3y]\'\xeb\xc2It!<\xbc\'\xb3\x9d\xcf\xfa9\xf4\x95>D\xaf^\xdb5\xfad\x8e\x83\xc38K\xdd.\xeeK\x12/\x12\x856\xb4\x9dT\x13\xe0AA)\xcd\xa7\xf3\xaa\xedr#g\\|`1\xd2<\x8dpt\xf7\xd3\xf58\xfd\xf3wR\xb3*\x02M#\xcdb\x8a\x96\xbb\x8b&\x85\x90\x9f\xa5\xd4\xcb\x19kRp!\x03\xf1\xd5O\x14u\xaf\x1a\xa9\xc9\xab?3\xef\x13N\xeb\x08;d\x01\xd8\x9e\x85\xb8\x9b\xc27\xad\xd4L\x9c\xb6\x15\x12\xaf;\xda\x11\xf6\x1d\xf4\xe0\xeb\xc8\x06\x95\xaa\xad\x88W\x1e*\xecx\xf5\xeb%(\x90\xc0\xd1\xa4\x04\x91\xacn\xaf9\xcc\xdeC2\xff\xb3\xc5H\x8a\xd3\xc5\x9c)\xe6\xe7\r\x0bb5\'OS\xb8\xa0\xd8/\xf1]\xe62e\x08\t\xa5+\xe3M\xef\xab\x16df\xed\xac6\xa9\xaab\x85\xc4\x91\x82\x94\xdd\x17+oAz\xed\xa0\xea*?\xa1\x90\xbc\x83\xf3\xfdD^\x07\xc8\xcfO\xd9\xe2\xcaK\x1c}\x8a\x86\xee\xb8e\xf0\x17\xe3\r_\xea\xd6\xa1X\x1e\x18\x86\x00\xbd}\xbfnc\xbf\x95\xd3\x07t\xde\xa1t\xcd\xc0\x1c?\xc4\xc3\xdc\nY\x0f\x19\xf4?\xb1\xb8\x9c\x9d\xdd\x056GD##Be\xfc\x96\xdc\xb7~\xea\xad\xc2C\xddA\xce\xa9\x8d\xe8\xbc\xb5\xa7\xd1\xdc\xe1\xf1\xaf\x97\xe6\x93\x0f\xbb\xe0VU5S\x88<\x95\n\xca\xb8\x94\xef\xdd\xd1T\xa5\xb9I=\xcb\n\xf3+\xe6\xb1\x8aL\xfb*\x84\x8f\x0c^\x14\x98\xa7\xc9\x18\x0e`D\x15;\xe3at\x1d\xc9Ja\xfb5\x11\x87ON\x7f%\xebl"\xd2j}\xeb\xf9\xbbG\xb7\xf3\x89\xe8\xd0\xb2\xc8\x1e\x89\xf0$\x17\xfa\xd3\xaf\xf8\xe7\x85}\t\xb8!\xba\xdc\xf7\x1d\x951\xc2\xc9\xfd\xe0D\xb3\xf7l\x08Yc\rP<\x9f\x1b\xb9\x15\x1a\xfc>\xf8\x07\xf9\xc4y\x83\x8f\x9d\x04)\xf8%\xdf\xfd\xdd$u`\xc5\xde\xee\xf3\x04"\xcf\xd4\x88\x9f\xcf\x8c\xcf)\xaa\x8eq\x08\x06\x82\x88\x1f6\xcf\x8b\xe8\xd9\xf5\x8a\x1b\xa6\xcc\xect\xf9` \x06S\xe6E\xbd\xac/\n\xa9\x95\xdaj\x9bfj\x0c\xab(G\xba\xf9\xf75c]\x13\x8c"\xa3\xb7\x15R!#\xb4\x92\xc1$\x85\x89\xf4O\x84}\xe3\xba\xf7\x19\n\xd6U,\x11\xb7\xfdj\xfca\x99uG\xe8\xd1\xcc\xd9\x81.\xc2\xeaO\'ZC\x12\xc3O\xfe\xc2CF\xcdZ&?\x1f\x0bB\xc8\xcenR)\x04"b47\xb2\x0f(C>\xc3\xbb@\xf7\xd1\xca\xa3\xf1\x10\x9b\xab^\x90d\xb9\x8e\xdf\xc7\xdf\x9ba\xcd\x8d\x82\xc4!\x8er>\xf1CC\xe4=\xedOm\x1a\xf9\\A\x82\x00\xf6\x87j\xe1\x8bv\t@\xe9\xb3\xa9\xcaZ\xd9\x11\xc7E@\xf7X\xbc\x9e\xfd\xad\xd9\xa8\xe0w\xdd\xb0_\xaf\x1b\xcb\xd7\x15l\xa97o\xb3\xe1W\x80\x93=\xbb\xf6\xca\xdb\x02\xd7\xbb\xac\xe5G\xf6\xed\xa6g\x86\xa3\x8d\x14]\xfe;Q.\x01\xf5\x91\xe5\xb5h\xb0\xb1@\x8e\xb5{2\xf4\x92\x0cX\xbb\x17K\x9a\xb4\x8e\xf2\x8d\xf6L\xeel\x05Hg\r\x89\x9a\x1b\xc0O\xc5\xb5Z\xc6\xcd\x9aHi\xeezlN\xffc\n@>\xd5\xcd\xd7\xf7\x9f1\x96\xb7N\xf7\xf1\xd4\xd4+ H.\xe1^\xf6%\xd7\x93\xdd\xef\x9d\x87\xf4\xe5\xee\xce\xdf\xbf\xd5\xde\xa3s}N:\x0f\xa8\xbb5\x11"\xd0b\xd7P~\xd8!J>8e\xbewSTI\xd6q2\x0e\xd5\xce\xae\x9f\t\xc0\xb5B`\xbe\x08SvDs\xd7-HS$\x1d\xf1+\xba\xf5N\xefp\x81\t\\m\xb6\xf2\x9duN9%;\x8eDq\xff\x14\x9b\xd6\x8b\xe8\xd0\x03\xc7(\xd7\\l$\xe1MH\x00ZO\xe8\xe4=\xf2\x01Ht\x19c\xd2\x9c\x84$\xf4=bq2\xdd$%\xad\xab\xd8I\xd4\xd6W\xee\xb7\xa1:\xdc?\xc7=\x0cJ\xa1vn\xefA\xf5(!\x8d\x02\xe1\x16*\xca\xe6\x87 \t\xacb\x0eI\xcb\x0b\x85d\x88#&T\xd8\xfb\rw\xc9\xaa\x94\x8f\xbf\xef\x8dSa\xcd\xb0\xfa\xe2^\xa6\xee\xf9\x03n\xd1R\x13\xc1\xbbX\x0b2i\x10a7d\xc7(\x82:\x1f\xebv\xf6\xaf$\x7f\xa8w\xefaw\xf2f\xc8\xdf\x9f\xc4\xa3\xd5\x06\xb5-\xd1\xb16}`X\x8a\xd5\x93\xfb\xd9\xbd6/$x\xd5\x8a\xda\xa9\xee|<W\xbaN\x89J\\6\x19\xa3\x03\xe1\xec\xbcF\r\x9bg!\xa9\xca/\xc2i\xa7\xed1\xfb_\xbf\x98\\\xafz\xf2\\T\xfd\x95P\x95\x9e\x9f4\x8ft\x83\xe5\xcf\xaa\x1d\x15\x89\x7f\xfbW\xa3\xd6\xd1\x89\x82\\\xd9\x19\xfb\x98\xe7\xc86\x1a\xcc\x85} t\xc3:\x91\xb8c\x7f\xc4\x8f\x98.+\xa7\xee\x9f/\xf2n\xcc\xc2\x14(9\x98\x87\x99\x89\x96q~X\xa7zKs\x91!Y\xaf\xe2b\xd5\xf1\xdaE\x8c~\xc4\xed\xdd\x83UN\xd3\x90"o\x10\x16\xd0\xb7y\x97-$\xc1\xad\xafV\x12\xb8\\we>\xb5\xd8\x9cB\xdc\x9e\xfd\xc6\xba\xb6\x97\xc7\xe1p\x93O-;@\xfb\xd5|\xba8S\x83\x80.\xf0\'a\xbb\x814G\xd6q\x19:G\'\xc3I\xcb0\xc3\x1f\x02\x8a;\xd9\\\x99\x9c,\x17\xfcB\xb0L\xdbU6\xd1\x90\x02\xe1\x161\xddt\x8f"~\xe1`\xeb\xd9\x84\xceX\xa12s+\t\x05\x1e\x86\xd4\x8a#Y\x9dLw\xab\x1d\x96\x1dfA\xdc;\x8e\xef\r\x11\x95\x16\xb9d*\x8d@\x93\xc1\xd0]\xd5.p\x94\xb1\xc2S\x86\x89\xdb\xa0\xbfP\x837~(\xc1\xce\x84\xdc>\xb1G[\xb4\xce\x80J\x88v\xed\xd8\x9b4\xf2\xf4\x0f\x1a\r\x0fI"\x0ed\t\xd2\x1c\x11\x03pv.\x18_\xe5\xa9>V\x8d\x93\x02\xfd)y~\n\xbf\x1f:\x13\'\xc8\x1e-\xb9-\xdb$\xac\xa6\xb8\xf0qD\x85-\x9ep; }\xe6vD\xe2BDt\x0f*\x1a(s\xbasf\xc0`.\x9f\x18Xt\xaf\x04\xaak\x93\xe5\x895\xff\xc9Ej\xb6\x08+\xd6\x02\xf1y\xceE5o\xb8\x8f\xc6l\xe1\xb3\x87b\xdb\x9fT\x87\xfa\x8d\xe7\xb8(\xb63\xa3\xd5x\xb7^\xd7\x87\x08#\x96\xa4#\x84\xael\xad\x96\x06h\xe2\x98l\xba52\x95\xa47TU\xa2\xd1\x90f\xd5\xf8B\rqCBz[2\xc8\xb3^Q\x87\xb7NR%\x15\x0b\x07\xae\xea\\\xe1a/\x99kB#8}W\xa4\x90"\x8f\x11(j\x97\xd0\xedt\xd5\xf9\xe6\xef\xd6\xbf\x14E\xe6:\xce\xc97\xff\xad\xb74\x9c\xe2\xddR\xd2\xb6\x8a\xf0\\\xbe\x90\n\xb5\xd3\xe8\xbe\te\xce\x0cBG\x15>\xf3l3\xdbL0\xb5\xc7\x87\xe5\xca\x973w\x11^\x05R\x97\t\x07\x1b\xa5\x87Z\x99\xc1au\x13/\xf5\r\x0e\xec\xd6AI\x8eg\xa5\x1a\x9a%\xa8\x9f\x8b\xcb\x9cHP\xdbza`\xbe\xf8w\xc0\xdfN\xbb\xe1\xa6^\xbd!\xa9\xfb\xf7\x03<"A\xb9/6\x17\xca\x06Ua\xdb\xd3\xb5&s\r\xe3A\xa3\x93\x81FU\xbd\x88\xc9\x08\xb8\x83\x8d\xb3\xfd\r$\x89LWN;l\x08\xfc\xedY\xb8\xb5\x14\xe7+\xd8i\x11\xa6\xe89\x01\xb4E\xb4&V\x95\xe5\x14\xf5L\xe8iv\xefw\xedP\xc6x\xc5B\xf1\x9b\xbfG\xd8u\xe2\xd8x\xd9Y/6\xd0\x13\xedk8\xff\xb9h\xed\xbdk\xd5\xde\x86cZ\x00\x80\r\xab\x9f\xf6\x83\x01\x02{\x05N\xeb\x87,\xde\x80\xffYBh\xeb\xd0\xc0l@\xd9\x199\xbbX\x1a\xd9n@\xd8z\xdb\x19m@Xx[9n\x80\x1b{\xb3l@\x1b[\xd9\x1b\xb9\x98XYm@x\xdbZ\x19o@\x98y\x9a\x99l\x80l\x1d\x8cL]6`M\xcdL\x1c\xec\x1c\x9d\xcd\\\\\xca\x01\xf7\xff\x89{\x85U\xf2b\x90ps11r5{\x85\xe6\xb3s0u\xb35\x13pF\xfc\xf7\xca\x16\x00p)\xfag\xdc\x80\x83\x81\x81\xad\x01h\xe7\xfe\x7f\xbc2\xb62\xb6:\x84:\xa8&\x846\x876\xd3.\x87\x1b\x00@\x11L\xd7\x16\xea\x16\x00\x10\xd4\xb3\x85z\xf8\x1f\xfcc\xdf\xf4\xff\xb5\xff\xe0\x1f\xa37\xf8\xd7\xfe\x83\x9b\xff\x1b\x9c\xe1\xff\xf9\xe8\xff\x02Y\xf8\xa8\x1e')))
except KeyboardInterrupt:
	exit()