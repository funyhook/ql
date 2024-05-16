# ============
# 项目：11.py
# 时间：2024-05-16 10:27:52
# 运行环境：python3.11.x
import sys
PYTHON_VERSION = ".".join(str(i) for i in sys.version_info[:2])
if PYTHON_VERSION != "3.11":
  print(f"【你的青龙python版本为{PYTHON_VERSION},请使用python3.11.x运行此脚本】")
  exit()
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(zlib.decompress(b'x\x9c\xad\xbaSp%\\\xf3\xa8\xbfc\xee\xd86\'\xb6fvl\x9b\x13\xdb\xd6dvl\xdb\xb6m\xdb6&\xc9\xc4\xd6\xc4\x99\x9c\xf7{\x7f\xff\xaf\xea\x7fq\xce\xb9:]k\xf5S\xcfM\xd7Z\xd5U}\xd5&\x80\xff_\xc0\xfd\x7f\xbc\x0f\xfa\'\xa5\x02L\x01\xa6\x10\xb6\x00\x9d\xff!\x84\x0e\xc4\xbf\x84\xd4\x81\xfc\x97P:P\xff\x12Z\x07\xfa_\xc2\xe8\xc0@\x02\xcc`\xff\xb9\x00\xeb\xff\xd6\x01\xfccP\xd6\xf0\xff5S\xc8\x12\x08\x00\xa0\x12\xe2\xbf\xfe\x7f3\x88\x7fj\xaa\x02\xe8\xa1N\xff#\n.\xd7L\x00\x80\x88\x8e%\x1f\x9b\xb06\x8d\xaav\xe37\x1e7\x00\xfe\xd9\xcf\xcf\xffc\xbc\xfa.\xfc|\xb8\x9e3\xa4#\x1e~\x14\xda{\x10\xba\xf9\x01E\xec\xa1\xdd\xb3."n\xa3Q\xab>3\x88V\xb2fy\x11%\xb0s\xa3\xd1\xe9S\xd2=\xd2\xb5.\x93\x7fT\xe5\xee\x13k\xbf\xc91\xd72\xa6+\x0b\x0c\xc1\xe9\x9e)\xb5+1\x89\xf5\xce\xf9\x0338*\x0f\xb53\xbd\xe6QGX\x7f*-\xec\x99\xeb!\xd6\xb9\xeaN@A\x03F\x08/\x91\x08\x01!\x80\xe5\xd2\xac\xf2 \x8d\xf0\xe6h\xe4h\xa29\xf1\xd2\x02\xec\x08\x80lPt\xe6`\x1a\t4E\xf1o\xc2\xac\x89\x13\x0ej\x1f\xf4\x87B\xc9Bx\xca\xa5\xe5g\x9cB\xa2\x12\x92e@\x04\x08\x00\x14\xa5<\x00 \xcfni\xed\x8d\x104\x94\xf4\x91\xcf\x9a\x93\xb8\x84\xf5TT\xda`\xed\x05$(Y\xba\xcb\x91L&\xa4\xbfT>\x88\x95.=\xcb\x89\x7f-\x94\xe7\xbc\x15>\xb3j\x16R\\\x06\n\t\x97\xc4\xd2\xc7qz\xe7\xe4\x01P\x95\x00\x96\xf2\x90\x96\xe9\x98\x08%\x12\t\xde\xa6K\xd3\x9cK\xb7\xaas\x03\x8a\xd2\xe9B\x12\xe9\x9c\xc6\xac\xf2r\x99\xcaaV\x199J\xde\xe9I\x04Vyvhs\x7f\xf09\xad\xce8\xc7\x16\x85\xe3,\x01\x04\x96\x00\x00\'\x00\x10\x97\x80\x96\x91\x93\xcf]\xfe"\xf3\xb3D\x02\xc3VN\x9eFmV\x9eK\xbe\xa1\xf4L\x88\xd3r\x99D\xe9Cu\xc1G\x86C\xd5ZP\xe9\x0f\xbb7x\xfc\x8cDil\xce\xd4\x12j\t0\xf7\x9f\n\x7f\xfe\xf9\n\x08\xae\x0c"\x8f\xaf\x08"\x0e\xf8\x9f\xa6\x01\xff\xad:\xf7?\xed\xe4\x9c\x03\x02\xc6\xf3\xfe\xdb\\\x04\xac \xb9`\xc5\x07+\x92t\xf6\xf2\xbf\xe9\x9cC\x12i2\x829\xd1\xf4/tB\x8a\x0f\xe5\x97\xf4\xcd\x9c\x7f8?\xe8\xe6_K\x13\xbc\xd9\x14U%\xa3UA\x1fXv\xf2\x9c\xa6\x9c\x04\xde\x81\xa2\xf2lB\xc2g\xa6\xb0\xd1\x04\x04@!J\x90%\'\x10\x00W\xf0m&\xde\xc2\xf1\xba\xfc\x93\xfb\xee6e\x04\x92\xd0\x0e\xdf\x1c\xbb\\=D \xb9\xea\xd2\xba\\&\x89\xabMf\x81\x87:\x85\xcc\xd2\xb09\xa2aT\x17Qk\xcd\xff\xac\x9e\x1d\x1d\xa3\xbci\xd3\xb1SF\xcc?TU\xe7n\xeax\x02-n\xc8&\xe6\x8ab^n\xeaG>o\x0e\x83\x1a\xe7\xd4\xdc\x81\xa9\xbf\x1c#\x1a\x01y\x11\x1eA\xfe$\xaf\xd7\xb2\t\x8e\xa2\x9c)F\x8e\xba\xa6\x8d\xda\xa0*6B\xf0\x16Eb_+\xa4\xce\x15)\x12)&\xdb\x0b\xe4#\x93\xe5,\x1b\x9d\xaa\t\xa2a\x1e\xe7\x86\x134\x01\xde\x18\x1a\xf3\xb1J7e\xad\xf2\x9c\xe1\xda\x92\xf5\x9f\xba\xa2\xe6\xdf9\x86\xf8F\x91\xb6Q\x04\x17\xf1\x10\xacVc\xc5\xb4\xbf:\xa0G\xee\xdc\xda\xe3\x82\x97DE9\x89\xfd)\xe4\x9d\xd0(!\xa1\xb1\xa7X\x87\x8e\xda\x82\x0c\x1b\x82\xf4\xdafZ\xe8\x9aV\x11*E\x82\x0fS\xa4\x00?U\xddq2T\xf8\xc7*\x05P\x06\xc9@\xe8\x90\xb4\xdch@\xa5\xc70&\xf1o\xda]S\xbf\x8d\x9f\xf5\x9d\xfb\xfcO\xbe\xf8}#\x18\xb0}\xee\xa5N\xdd\x95\x9b\x1b\xff&y\xb8]\xf1wy"\xe9\x8c[\xe4%\xae\xf4\xfc\x0e5\xd0\x01\x8eC8rF\xcd\x14?\xed\xf7\x15\xc7\xb0\x11azm\xdcV\xd2I\x0c\x06\xa5\x15\xca\x90DASapD\x12\xb9\xef\xdb\x0e7C"\x0e\xa6\\}\x97Zl\xfd\xc8\xc2\xfe\xd1\xb9$\x14\xc0\xee9\xbb\xbb\x9b\x04mD\xaf\x0eO\x18/{(\x8f\xa0\xa4\x80\x07P\xefo\xa5\xc5\xd88uo!\xfcV(8\xae\xa4v\xd7\xe8[!\x87P=*5\xc9+}$\x96e\xd4\xbfGk\x01\xa6\xc5\xceq\x8d\x99\xfb=\xdf\xdb\x93\xef$bL\xa7\xb5\xf5\xd8\xb2<\xad\xdc\xe1\xd0(\x15\xf4\x08J\xa8\x85\xcb\x9d;Y\xe20\xba\xef\xeb\x05\xfeng\xea\x9a\xf9\xdb\xf4\xb2\xb5:\x85\xc2\xd6S\x9f66O\xea\x8ao\x0f?\x14\x11\xe7\xf8e\xae\x1d\x80\xb0\x80\x10\x9c#\x8cF\x07\x0e\x19?!"\x9c\x7f\x13\x14\x14i\x02\xe0\x0bTpC\xb7x\x8e\x01$\xaf\xb2kH\xce\xaf7v\x164g[\xa3&\xc6\xf6\xde+u\xf1>0\xe20:%#E=\xf8\x0c\xdej.\xde\xb0\xf0QK\xfd\xc4\xe7\xd5b"\xa5\xa2\x94\xcf\xd9\xdeOx\xcf$c\xc8\xc7\xec>\xf9\xaeu_\xbf\xf9~.@@}\xff\xd1\xf5\x1c\xc3l\xfe\xb4\xd2z\xc3_\xb7"XzV\xd0\xd3\xb3\xe7\x06\xf3\xf8w\xe6\x8f~\xd3"aoc\xf6@\x9d\x7f\xbb\xf1\xcc\x8b\xed\xc4(/\xa3\x9e}/V\x1b\xef\x01E\x8c\x88\xe2b\xd1\xd1c\xe5K\xd7\x8e\xfc\xfe!z.\xd7\xda\x83\x8fs\x99\x1f\xb9\x1bZ\xb9\x1dj\x8b\x95\xb6\xfd\xc2;\x1f\xfd\xaa\xfe\x88\xfd\xa0\xb9\xdczK\xf8\xa9\xe4^\xe7Q,\xe0!z\x12\x03u\n\xedo\xce$\xfbE\x95\xd7\xe5g\xf1\x93\x0eYP\xb0]Q\xf0\'\xda\x10E\xa5\x89T\xa0p\xd0J$\x08\xfc\xa5\xbf\x85{d1\x9e\xba\xdf\x12\xe7~~\xa1\'\xd1\xa4\xc9\x9e\x86\x16\xb3\xa3~\x1e\xbb8\x07\xc2\x88\x02\x1e\xdd\x94\xda\xb4\xe6KP\xb0\xb9?\xc9\xad\xa9\xda\xfcM\x0f6i\xc5\x0b\xf5\x00+\xc0\x04\x8d\x1e*P\x04\x1aZ0\xb2\xdc\x02\x08)\x1e\xb4x\xc9\xa8\xe8\xb9Z\xc2\xfe\xe4C\xff\xa1\xa1\x95\xcc\xfc\x84"\xc9\xf8\xc1"h\x10\xf3\x88\xaf\x02\xe3,\xf7\xf5\xbcu\xf2t\xab5\xbd\xa4\x7f;\xe5\x1cu\xf1\x1e\x8f\x93.]\n\xa4 "S\x84m`*\xde\x94(\x95\xc4\xe3\tX\x87\xf4\xcc_"\x08\xc6\xc1\xdcU\xa1\x145\xb1\xfd\xee@9\xe9\xadl \x18M\xb2\ro\x9eV\xda\xe3}\x8a\xdfk\xfc\xc0\x99`H\xf2\xc4L\xce\x1d6\xa8\x15\xcc\xbdu\xe9\xf7cB\xa5Y\xc5\x8eB\x04\xe27W`i\x82X\xc8&\xd4\xdd\x86\x969\xc41\x1e\'\x98y\x86\xf5\x0b9\xfe\x0f\xba\xf6hw\x0e1\xf4<;\x06+\xb2hH,K@\xaf\x93\x05\n\xec#\xb0L\x95\xd9,\x0bd*\xcb\xf4\x19F\x92w\xd8<\xd1\'\xdc\xbfg\x89\xc4f~\xceP\x82\x8fi2\xfd*\xc6\x02\x05`SX\xe7\x8c%/c=q\xbe\xda\x81\x81\xa4G\xe5\x9d+f\xa5\x03\x0byRK\x9dv\x84\xf7\x93%@Mw\x13\x85n\rL\xddP\x89H\xe7\x87\x93\xe7\xefB\xa1\x11i\xb0\x14$H|v\x93\x01\xa3\x03\xac\x02L$\xc1p\xd6p\xd8.\xe3\x0e=F\xfe^P\x17\xe5I\xf5\xaf^\xee\x91o\xefU5\xd72\x06\xb8P\xf463xd\xf0~(\xb7?\x9e#\xa3\xd0\x91m4\xc7\xa9G\x10^\xf2\xa3\x859\xb9[\xd7\xdb\xd2K+R\x8aF\x8e\xc5"\xa0(\x7f\xd0\xc9Cu\xdcC\xb8z\x9a\xdb7;\xbd\xcc\xbe\xf3\xb3\x1eC\x12\xd5\x19\x9a\xb2&\x0c\xb0\xeb\xbd|4K\xa2\'\xe7\xcf\x7f|\x0c<\'\x80k\xa0Erg\xcd\xd4\xb1Z]\x8c\xd7WYt\xf3\xf7\x9c?Z\xfb\xbf!\xb1H\x92\xa8qw\xd3\x14\x98[\x08`\x9eA\xd1<Ou\xbb\x851{j\x85\xe0\x11\xe4\xf1!#3\xf36Q\x14^\x84\x06\x13\x14\xbb*\xcf\xb8\xe5\xb5\n\x92\xf1\x08;\xef\x83\xd72\xac\x80lzZ\xa0\xefzm\xae_-D\x9b\x1e\xb2\xfdF\'\xf3\x99\xf3t|\x1c\x98\x86C\x19C\x01\'\xb2_s\xbd\x8cE\xd8\xa2#\x8c\x00\xec\xb0\xc9\'o|\xcfC!?b\x98W\xee<Dsvge\xb2~j\'U\x17\xdc\xe2\xae\xbb"\x17\xe5\x117\x08bj\x03\xb16P\r\xef\x8eP\x0f\x06\xd6\x90\xd2\x91\x98\xe8F\x1f\xaa\x0c\x1e\xb5\xbcn\xc1\xf1\x02\x80\xde@\x08h2\xc3\x9dK\x06\x88\x9f)\r\r\x9fx\xfaE\x1d\x02\x9f\xa4\xf4\xcc\xec-\xdd\xbe\r\x05\xbc\x7f\x91v~\xeaxK\x9b\x9a\x9a||\xcf\xddw\xb8\x93\x98\x1a\xdb\xd0^K\x0e\x98\xff\xf1\xb9x\xe7\x15\xf3\xe4\x04\x07~\xe7\xc0F&\xce\xa0b[d\xf4meI\x9f+\xb8\xa5I\xe5x\xe9)\xb9\xf8\x8b[Y\xf5\x89+\xbaf\xbe[\x9au\xbfL\x7f\xa3\x17Elb\xde\xe2\x95\xc9\x8e&anz1U5\xa3\x89D\xd7\rP\x05\xaf\x04\xda\x80w&\xd1(\xceN\xees\x8e\xd6\xb2\xabmZf\xf6\xe5\xd7\x84[\xa2W\xaf\xd6\x1d\x97A3\xe2ti\xd1-PN`\xee\xc9\x83\x04^v4&\xd1\\\xd6\x13\xb3h\xeb)Y\xa6M \xf7">D\xea6\x9aa\x1a\xb2\xa5\xad\xcc\xc1\xa6\xe1\\\xb2h}\xb5\xc3N\x00\xb6\xad3\xf3\xc4PZ\xbf(Q~aL\xc6\xd4\xa62[\xd3\xda\x86-\xa5S]\xa4b\xae\xcaEFN\xb8\xfdr\x9e\x0e<\x0b\x13Nr\xdc\\\x0f\xb6\xe0>\x11\x88\xaf\xec"\x19E\xfaz\xe4\r&\xac%b\xdev\x04\xf1\xa5\xc1\xce\xbd\xd2\x97\xe72\xb5\xea\xf1\x9c\x85\x85\xfd\xd7\x9c\xee\xc5\xec\xb3%n]\xa1]\xf9\x84\xcf\xccLF\xdf\x13\x925c\x9d\xbf\xb3\x99\\\xe7E\xbdE\xcc1\xfaCR\x03\x07\xf6\xd32\xcdH\x9e\x9a\x86%\xa7\xa98\x10\xca\x83\x1d#\xd1\xb9\xec\xbe\x9dO1\xef\x91\xe0h\xaf-r\xc89F\xe5\xf0\xcba\x1d\xe3\x0c\xe2\xad\'\xcf~\xb4kT\x81\x8a\x9bNtP\xb2\x19\x1e\x1b\x9a\xb4d7>4\xd8uJSH\xa2<V\xae+\xe2VLU\xb9\x87\x08\x07GY\x81e\xd4)\xbb\n\x9fU\xb2\xc9\x9c\xdd"v\xca\xb34\x10&\nnp\x9f\xf3i\xc7\xa3\x07\xbd\x0f\xeae\xf6\x00\x7f2\xd7\xd9up\x17\xc4\xaf>\xcaYR\xdc\xbf\'d\xe1^\x85\x9414\x85-\x90\xf7|S\x817\xad\xa5a\xc2+!d|\x85\xe6\x80\xd2`\x14\x12\xc5e_\xaf\xc5\xa8\x064\xef]9%`FdN\xcd\xdf~pE\xdc0\xab\xa6J\x90\x86T\x10b(\xcbG(/\xac\x13\xf6\xd4z\xdcX\xa93\xe6bb\x13\x0f\xb7L\xd22\x83\x1c\x0cO\xe1_E\xa7\xf5#\x1e5\xee\xe2K\xc0\xd5\xf9>\xa1\x93$2.\x89\x17\x1co\x89o\x0cc\xa9\xdd\xf8:\xe8\xd7\xee\xaa\x18{\xb3\xd0\x80\xb3\x9f=\xcd\xb9\r\x02\x1f\xa3\xc7\xe6w\x04l\x86\xb5\xfa\xacr\xe5\x99ZH\xd7\xf7\x06h7+\xa3\xb6\x1d\xb8\xb4\xc8q\x03A\xfe\x82\x9b\xa1\xec\xd2\xcdu:=\xbd.\xaa\xf5\xbb;Ad;A\x10;]\x16\xae5Q\xfb\xdd\xd3-\x9f;\x9a\x98?z(\x92=\xfbOO\x1f"m?\x9d\xb2HM\xce\x94\xe8L\x93\xf2\xa8&/\xb2\xde\xe3\xf59jk1\xbcT,\xdb\x0c\xcb\xfc_(\x0f\xd6\x98Lq\x19$\xfc\x1eB\x00\xf8\xb3.j\x14\ngH\x91\xb8Fy\xf9\xb0\xa13\x91\x07C\xcfd\x83!\xa9\xd7O\xe23\x80\xda\x80\xdeA\x18\x15\xd6pcc\x0b~\xf2\xac\xd0\x9b\x1a\xb0\x1a\x06\xbcp\x1e\xacZ\x9e\xbd\x87\xb00,\x8c\xd5m\x12Eh\x05\x10\x1c\xd26x\r~\xeb+<\xc8\xa6\x88\x10\x14\xb8\'3\x17\xfd\x9b\x04\xee3\xe0\xcd\xfdD\x9d[\x10c\r\xed@\x90*\x8b\x1f\x93\xe0A\xc0$\xa7\xea8\xa3\xab\xa7Z\xae(;\x08\x88\x91\xeeT\x17\x86\x97\x0fV\xaf\xa6\xae\xae\x1e\x9a\xa8W3\xd1\x9d\x8d{\xfd\xf0\xeb\xad\x85j\xfbD\x96\x80\xd2\xea$\x84\t1\xd622\x96M\xeb}\r\x89\x1e\xe8n\xa1\xb9q\x93\xe8AJE\xc9\xdd\xb3\x19\x9b\x1an\xa9\xc2a8\xa2_\x14A\xbb\x87T-%\xc8f\xbfZS2\x07\x07|\xc0\r\xddu\x11\xd6\x1bVe\x10\x8c\xa0\xf5)\x17\x96\xc1G\xc98\xa5\xc7\x90q\x10\xc3\xcc\xcf\x93AW\xd3\x16]l9\xbc\xc8;G)\xce\x16"\x8b\x069\xe8\x121\xab\x9eN\xe0\x9c\x8c\xc2"\t\xf5\x05\x05\xf0\xab\x08\xba&\xcb\xcb\xc8X\xb67\r\\|i&\x9bHc\xa7\xc1\x16I\x02\xd0OV\xf1#\xb1\x9a!Z\xce\xa8\xeb\xaa\xa32\x81\xda\xd4%\xf2\x9b\xe4\x94\x9b 2\xf7\xfdC9\xa2\xdf\xde\xf4\xebwo\xff|\x17\x1f,X\x9e\xb6\x18\xd4\xa4\xa9Z&\xe9\xf5`\xd8\xf8C\xdf\xee6\xd7Pw`\x12?\x0e\x7f\x05\x0c\x89\x8b\xb6\xa9\xe9X\xbb\xbe:{\xbb\xeeB\x1f\xb3\xc27\xe8d\xe9y\xa1e~\xe74\x07\xbcP\x18(2\'\xc7e4[ed\xa6\x05\x92V\x8c\xa4\x84\xa2v\xb5@\x1b\xc34\x19z\x13\xb6[ \xf0Y\x88\xa2\x1b\xb5\xf5im\xed\x1fL\xd4\x9b{\xb9\x0c\\t\xf3\x898\xe9\x93c\x9c\xaf\xff^>\xfe\x8e3<\xe7\xc1\xac\xd3\xac\x8c\x8eN^@\x07\xa3\xebJ>E\xb2\xfb\xb0\xed\xe5\xc8\x00\x83\xb1\x18\xe1\x84\xd9$\xe4\x10\xe2\xa4\x85b\xde\x01N\xe7\x92\xc1\xa4\x91Us1\xec\x8b[\xa0\x1b\xab\x81\xa9\xc33P\xea\x8b\xc0\x1e{\xfei>L\x1e\xe2^\x19\x88\x8c1L\x8e\xcc/q\x1a\xb5[\x00\x0f\x1aj\x95_o>\xaf\xe9\x0e\x93\xa6"\xc2\'\xa2\xb2\x8dY\xa97\x9eo\x11.c\r\x847B\xd1;\x8e\xd3`(\xfd\xe6\x11S\'>|c\xa8(\x8a\xdd\x8f\xa1\xb958\x99A\x04\x97\xcbn\x9aG\xc4C$,\xf8r\x04U\x9d\x80Fc\x8d1N\x87\x93\xdc\x8amRn\x1e\xb88&\x06\xd9W\x9b\xf5S"~\xb9!\r\xab\x9c\xdf\xf5DZZ\x9a\xbeO\x993d\xbe\xb9\x12\xda\x84\xb3N\xfa\xc1P\xa90\xb7.*\xf2{\xe0\x99|\xb4\xc4\x9b\x1f\xc1\x86\xe5^\xc9Flx\x8e\x13\'\x9e\x8c]\xcb\x83e\xb2t\xb0\xbfij\x07\x15\x1c\\6\xf7\xae*\xe4\xa1G\x03\xdb"\xc0\xc8\x0f]\xd4W\xbe8\x8f\xbd_7\x866\x14\xea4l\'[p\x1e\x1d\x18HM7\x8d.P~W1\xefI\x1aA\x8a\x85\x00\xef"\x1c\xc1\x87\x7f8\xb1\xf2\x9c\xb7\xa7\xddX\x06\xad\xa4%\x85\x9f|\xb6\xf6\xe8\xea\xb2\xf1\x82\xc6M\xc3<\x93\'$\x81F%\x85&\x07\xf5\x049\xf0\x8c\xeb\x10\x1f\x06\xd9\xech8SW\x95<\x90\x14\x96=\xa5\x8b\x14\x87~\xba\xe2{\xeev\xc1"\xc71`\x89\x93\x8d\x91)\x98\x89\xe8\xcf\x14\xc7\xb8\xa0\xd6\xe0\xc3\x97\x12\x11\xbfX\xb6P\xae\xdc\xa6\x02\xb5\xc3:g\x89\xe3Ue(\xc4\xb6\x0b\xfc\xbdCx}d\xd4\xcf0\x8c\xbd\xc4\x00\x97\x83\xa1\x81\x86"\x9c6\xaa\xa3\x84\xc8J\xc1\xba\x05\xfcq\x00\x90\xa6W\xfe\xf1+\xf2\xf9/\xfc\x015\xd1\xbc\xca\xd5\x8d?^6\x16w`F\x08\x8c\xb2:yg\x11\xb8\x02\x88\xd0(\xe1\xbd\xb8\xe1\xcb\x94\x00\x02H\xb1UP\x88\x96a\xa4\xa7\xc3\x13\xf2\xc6\xfc(8`^\x87\x7f\xce7\x02\xd2i\xab\x1d\xeb\x86\x12\xcaB,\x17\x14\xb8*\xf1I\xc2\xec\n\xe7OZ\xe1\x03(\x92n>\x7f\xa0k\xdd(S{\xf6L\x08\xcdKL\x9d/\xea\xd7\x19\xaf\xe2AC\xe9\xe1{\xde\xbb\xd3 \x9f$\xa8\xa3\x94\xe1\xf8\x9e\xc0\xf38\x81\xa4a\x19\xe0\xd7\x86\x86F\xd8\xc2\xcb\xb8=\x13\x1f\x86<&\x85\xfd\xf4Es\x15\xc0\xa4\xa2\x10G\xbe/\xb9\xe7\xe1o\xb8\xf0\xfb\xeb\x81\xf6T\xd5\x04c\x18k\xa4\x04\x14\x9f\xa4\xa2\xb4[\x17\x8c\xf76\xf5\xb6D\xa1H\xce\xba\x0c\xd6\x809_K3\xbek\x16\x89\x9f\x84#\xf9\xee\x87A\xed1Q\x86F\xd8\xbc\xdfr\x06\x0fS\x90\xa5\xea\xb7\xda\x14J\xcf\xcc|\x8a\t\x96*\x10\xf54\xb5\xb4\xe4\xb0nr\xca\x87<\xecRmv\x04\xa4\xb6\xcf\xd4jj\xc2.\x90\x0f\xbe\x11\xf1oY\xfe@\xa8\x1f\xba\xcb*A.\xdd\x9ey\x8cR\xd1\xd5\xe5\x0eI\xd8\x8a\x0f\x14\xe5\xee\x823\xa9#\xaf\xd0\x0e8\xa4\xd8S:\xb6[\xb8\x11\xbc\xb1\xc3Z\xe9]\x1bs.\x88|z\x7f\xa1\xfe\xce\xd1J\xf1\xf5!\xb6\xb3\xfb\x16\xc1\xa3k\xd1}eH\x85\xc4\xc9M\x90\x87]\xb6\x98\xdb\xc6\x8f\xb6\x10\x93Y\xea#<V\x8e\xd9S?/\x87\x93\xd89\xe102\xf4\xf9g\x1b\xc1\xbb\xdfV\xc4\xe0\x83I\x92J\x92\x9b\xeeY\x85\x95\x9dT\xbe\xe38\x87\x8d\xe5\x036\\L%-\xcf\xa1\xf8S\x85\x8c-y\x95I\x04mY_\x82(\xd9%\x8a\xf9N\xb4\n\x86d\xff\x9e\x87]uU\x84\x00\x8b\xc1WZ\xf9\x9e<\x97\xa8\xf5\x94\xd1\xc4\xcc\xd0r\x8d\xf6\xc9\xac\xa0\xe8\xc1\xa3\x97N\xfet\xbe^\xf1\x8b\xb2\xbeV\x81\r\xa8\xe9\x9e\xe61C\x16\xd2\x13+l\x9f\xbf\x1e\xea\xe0\xe6\xc4\x80_\xdc*KW\x0f\xee\xad\xe3\xd8\xdc\xbc\x11Q\xd4(NA\xa6%x]_\xb9\x00\xa3\xadD\x9c\xf9\xf8\xab\xcfs|\x94\x12\xb5{\xa1\x944\xa4\xc6_\xe5$TY\xdf\xf5\xa4\xc2\xe5\xea\xff\x1a\xd2\xec:,\xb6p.=ab\x19\xdd\xbe\xa8\x04rg\xc1\xbeA<W\x98\x84\x0ez\x97\xaaE\xf5_\xa0\x9f\xce$1\xff\xb2\xff\xe9p\x8a\xe8\x14\xce\xcb2\xaa\xf2\x93j8\x86\xb9\xf3g\xd3-\\\x18\x06}]p\x08j\xbe\x05J\xa3\xec\x92\x8c\x16y)\xb2\xf8\xf0-\xbd~\xdbv\x07\x96\xece\xab\xfe(\xea\xd70MA\x85o*\xae\x11\xdb\x1a\x0e\x0b\x85Z\xbd\x03\x9b\xcc]\xc1kd\xaf\x9d\x97\xd4\x90\xae^\xfb\xfc\x02Qn\xe8\xfb\xf9\xc8\xf1e\x83\xbb\xf5\x18,\xec_\xdb\x0fJ\xb2\xe9\xcf\xe9\x0f\\?o[\xf2\xe2\xc9)Lz\xdf\x88\xb7\x8d\x1b\xbe=k5\x85\xd0\xb2\xe1\xd1\x13SQ\x12\xd2\x88\xdd\xb4\x84\xa2\xeb\x14g\xbd\x8d\xc7\xb0\xb2FI\x06\xc6\xac:\x8b\xfc\x8c-C\xdc0\x9f\xfb\x11\xbcHl\x942-\x02\xbb\x8a\xa3@Zu\xba\x95 \x8b\xbd\x90\xc6n\x82\xb2\xe8\x0fc\xda7\xb3y#H\xdf\xc8F\xdcCN\x86a#C\xa3\xd4AG\xaf9F}L\xf2\x0b1\xd7j\xbf\x18\xf7G.`o\x19\xb1\xe4\x8bW\x07\x88\xf7\xcfx]\x16\x91\n\xdd\xfca\xfa=\xf7ck}(]\\WCP\xf8vN\x1f\x9dGz\xcc\x08\xca3\xc5\x07\'\xdb\x00\x90\x9f\xfc\xbc\xa5\nh\xd9\x02\xbbH\tK\xef\xa3\xec\xd9_f\xbb6\x99H\x15\x8c\x1b\x9f\x9fr3\x84S^[\xf9\xa0\xa3rg\xd1\x1b>\x11P\xc1+jF\x82&x\x94\xdb,S\xf5\xea\xc1\x01\xa9\xa3\xed&\x19\xd1r\xd3\xb3r\xe6-\x98;\xff\xa1xr\xdd\xe5\xd1\xe4\x89\xcb\xe9\xd7\xda\n\x1e\xaa\xf4\xd0\xe6\x8f\xd4\x05\xb3Z\xd8\xf0\xc5\xed\x02Q\x15*\x80\x04S\x01i\xdf\xc2\xfb\x17cL\xec\x02aF\xae\xfa\x17\x84\x93\x8d\xe8Fg\xef!\x99\x19K>\xc2 \x17\xfe&\xb0X\xfd\x99\xe9]\x16k4bX\x11\xd0HQyl\xa7\xd4\x90\xfd\xae\xa5t\xf9B\x94W\xa6\xaa\xae\x9e\xbc\xa2\xc9\xb2}\xbc\x99\xd2\xd7F\x1bHK@u\x1a\x17v\x88F\xe3YX\xd7\x06\xc1\xc9d\xae\xa99uR0g\x17\xf5%\xfa\x04\xddF\xa3\xd9H\xf6\xd7F\xb9\x92\xe7,\xf0gra6c\xe0t!\x86\xf64\xf4<\x062&\xeb\x84Kp\x18\x90\xbc2\xfbY\x9e\xd8deu\x86T\x9c\xc0\x88\xff\xb6h\x16\x86y,\x8bX\xb9f\x9f\xc2\x9drb\\\xde/\xf9\xb7=Es\t\xcbM\xd3\xebG\x0fq\xb7;\xb7\xb6\xe1\x1a\xce*`\xc7\xd3\x95\xb7\xcc%\xef\xa9\x8b?\\\x11\xae;\x07\xa2\xfa\xab\x10\xba\x14\xa2x\x9aLI\x9e\xb6\xf2\x1f\xe36\xacgN\xd0\x07\x81,\x9d\xaa~2\xf3\xb4\xd6rH\xbe*\x00.\xc4}\x13\x99nl \x1e\x93\xa8 \xe2@\x08\x98V\xe7\x8aJ\xaf\xf0\xd7\xf3t\xd7\x1aZ\xcf\xf3C\xb0\x07\xda %\xe7\xce\x9e\xfd\xa2\xe4\xa5\\\x8a\x03\xb8\x13\xe0\xe2,\x8d\x1d\xee\xfe\x8c\x9e\xaf\xc1qs\xf7\xa3\xae\xa0J\x1b\xfd\xbbv?z\xd3y\x04<\xf7\xfc\xeef\xc69#^\xb5\xbe\xed\xc9U.{\xc9\xe01\xf7\x1753\x1c$\xf3/[m\xac\xa1\x02\x08\xf0\xad\x9e\xa8\x02\xcc\x87\xeeB\x0c_\xf4\xcc\xb2\x02\xa2\x03\xbf\xc0;p\xef\xf6\xda\x19\x07&\xa9\xed\x0e\x9b\xbf\x18-+g\xe6\x98c\xd5\xf6\x9e\xb4/-\x9et:\xccjq\xc3J\xc0A\xce\xe1\x02\xa9`\xd6\x0c\xe85\x8fctt[Z\xd1\xfe\xee$\xa2\x7fX\xa3\tvG\x08\xc9|\xa7\x11).\xbbD8\x8b*\x80dF5\x8b\xdb\xa34\xf7\xa10\xc9E\x92\xd1\xd1\x15\xd1Q\xe2g\xcb\xd0\r\xcbcb/\xd4+\xa7&\xf3\xeb\xb8\x16\xbcPt\xf5N$^\xdf\xc9\xd0\x9a\xc2\xcd\xbb\x8c?\x9bE\xa5\x8d\xf1-t\x8a\xaf\xabW`\x9b(\xa7\x8c\xee(\x911\xa9\xa8-\x1e\x8e\xdcB]\xbd\xb2xW\x8f\x8b\x9b\x15\xed8a\xbbU\xb0\x8e\xfb\x12\x06\x85<t\xe2\xd5\x015#\x03\x13mf3\x0e*\xb9\xaf\xb9\x11\xbf\x16\xa4\'\x17\xedF\x94\xfb\x0e\xe2\xacS\x0e\xae^q\xb0p")\xb4\xd1}\xec\xeby\xf1\xd70\xe9Y t^\xdb&\xd7\xa6\x1e\xb7\x84\xad\x8f\xd4Ov\x81F\x81\x04/$\xcb\x9e\xfb\xd8\xb0\x0b<=,\xfd\x8a\x15B\x80\xb9\xd1\xcb\xeb\x9d\xab}\x03\xf4\xa7\xe3M\x8f wf\xc7\x00\xae!)\xa7\xfb1FH\xd3\x0b\x94\xa4\x14\x9a\xa8\xa5\x83\x0c\xe71\x12\xdf\xcfE\xebk\xfb\xcf\xc8\x1e\xa2\xcd{8,7y\x86\x7f\x13\xc5\x8cm\xc2*\x842\xdf\xd5g\x8a\x15\xd3}e\xb7\xfd\t6IE\xdfH\xcf\xd2\x86\xa0\xb7$\xc2.[\xdaZlOY\xc4\x9en:+\xa6T&%\xc3d\x87o\xba\xba\xf7\xbc\xd9\xaf\xb1&\xa4+I\xad2%\x87\x07\x99\x15\xe0\x13\x08\xc7\xc7\xf5\xb1\xa6\xf5\xe3\xa8\xa1\x0cK\xc6\xd5VYw\xa18\xba\xaa&\xd2J\x8a\xcd\x8ac~H\xc92\xca{~%$\x92\xe8\xa8@\xffi=\x1c\xfa\xe3\xf3g\xf3\x0c\xd7\x08n\x10\xecH\xf2\xad\xf1\xb1f)\\\xae\xb8&3\x96w\xff$\x99J\xb0\x88\xaa\xa6g8\x04\xc5-|O2\xd2\xd4.\xe4\x9d\x00sjz\xb3\x04\n\xca-.\x03\xb4\x94\x0c\n\x85\xb4M\x15\xbe\x99\x8a\t\x03\xbd\xbd\xd2\x9e\x16\x14\x80\xf2\xd6\xa0\x9f\xb9\\J\xad\xf5z\xe3~,\x14d\x1d\x9a)\x0e\x06\x97C$|KPC\xa6\xde\t\xca\x806tW\x9c!5u\x0fbJ\x99H\xe6\x8f\x08\x13W!\xe5\xc4\x19\xe0\xb7K\xe4@\x1e\x14\xf8\x9b\xdfJ \x855N\xbe\xe9I\xc5\x01]\x18\xf0\xcb1\xffn\x15\x17\xb9R\x8a\xae@\x85\x80\x9d\x13\x132k\x10\x0e\x00\xa2\xbb\x83\xbe;V\xcb)_a\xe1Q\\\xff\xcbv}Z\xa0YD\x84\xc2\xa0\x8e2|\x83\x97\xae\xb2o\xc8\x8f\xf9P5\x04Y\xd4\x8d]\xb4\x07\x01\xd8\xb8\x98~?87Q`\xc7\x08\\w\xf24Xm\xbd\xea\xb0-i\x9e\xa1\x8fL\x15\xb6)\xb1\xa5\xf0\r\xffRd\xa3\xb5\x9c\x0f\x9e\xc5\xeb\\\x9f\xf8\xd4\xe03k\xce\xc00c\x05,7)\xbb\xc2\xb5\xa4\x15\xab\xd3\x8f\x19\xc5\xea4f~g\x85\xe1\x8b \'\xa3%\xd6V\x9a\x87\xe06\x05\xcc\x8f\x91\xbe\xca\x9c*\x91|\x9bMB\xe6\x83\x97\x8c\xc7\x1e[(&H\xd5J\x06:\xc0\xd8\xf35H\xe3O\x9d\xbc\xc6\xe0u)h\t\xe3=2\x84\xa5\x8d\x8fO\x1f\xfc\xba\xc8yU\xa6m\xac\xbcp\xc7$\xb0\xe6\x97H\x850\t\xfc\xb9\\\x1e\x05\x8c\xe2\xf2\xfa\xabY\xa8W\xd0\x8bO9\x16M\xac\x06L>H+\xdb\x14,s\x96\x15\x15\xf9j\x83\x8f\x8a\xca\xb5\xa4m\xac\xb2\xa0\x14&`\xff5]4[=\xae\xd0\x98\xf5W\xbe\x00\xe5\x0e\x17`\x8a\xc4P\x98Y\xa9\xbfR\xa8\x95\'\xe1dj\xb7\xb4$\x9f,\xde\xdb\xe7\xa0\xd6)\x9e\x1e\x7f\xaa\x91Hz\xd2\x122\xaf/\x1e\x96\xa0\x88\x03\xd0\xbe\xdct\xec\x1d\x1f\x91R&,\xc2\xbfH\xd6\xee\xac\xa9\xc3\x00\x12\xf2Gm\x8fz\xaf\x1d\x9f\xa3\xf8\x9d8\xe0\x96mF\x93\xa0\x83\x14\x98;\xf3\xe8A\xec zP\xfcW\xe8\xe9\xf4\xba\xfaisf\xf2\x8f\x8c\xacV`\\\x02=\xfe\x96\xbb\x95YJ\xf4\x96a5)H{\xf0[Z\xf3\\e\x98\xd7\xf3\x94%T` \x0bCH\xda\xc2\x04\x81-H\xd4\xa4\x84\x1d\t\x11 vg\xab\x87\xcc\xc6\xc1\xec \xd0\x8b5Q\xcew\xf9a\xd5k\x83f\xc4\x82G\xf6\xa3\xa0Ss[\xb1\xe7\xda\xb7%{Z\xb8\xe5\xd9\x1c\xb7t\x9c/Jp\nc\xa6\xd1\xae\xcb\xce\x9d\x13\xbe\xc1\xa3\xa7\x08x\xcf\x824\xb5\xff\xbb\x9d\xe8\xb8\xcd\xfc\x88:\x81\x11\x0b\xfeD\xaa8|\x14\xff\x9beH\xd527I\x8bO\xd9e\x18\xe4Yf\x1fS\xeb\xfa\xb7\xbc\xb3\x8f\x16\xbf\xf2\x97\xde\xeaH\x14E\xea\x81\xa3&\xdf\'\x823\x1f\xc5b\xec\xbfS\x90Xn\xb3\x8dL\x86!B>\x1a2\xf2M\x1br9\xd9t2@G k\xdb\x06\xfb\x11\xecJ4\x12\xac\xcd\x184\x1aE\xc9\xe4\xea\xf4W\xa67kD\xcb)a\x02\xeb\t\x9d\xbb5*6\xc2\x16{\xe4\xc3\xfc\x8a<\x9358t\xbdA[15\xe7\xb6#\xb2\x19\xba\x03\x10\xaa\xcf\xaf9\x17\x7f\x1dxY\xc1=AV\xc2"\r\x9b\x01B\xba\xb1\x12\x96F\xed\xd8\x99\xca\x99s\xcbv\x89Rl\xb5]\x98\x88\xbb\xfd\xc7EK6\xc2\xf5\xd4y\xf4\xe6Q\xe6\xb9\x13|"nePy\x18\x8e\xf1\x8di\xd9rA;\xc1\x1c\x0b\xd9\x04\xa8\x1a\x87\x15\x96\x86\x9dFo\x8e\x12a\xbd\xad\x16i\x96\xb0F\xd1\xd3(#k\n\xaf\xb3\x16\xba\x08J\xa4\xa3_\xb1\xdb\xce\xd6\x03\xc2\xd4\x08\xb2\x87\xc0\xa3"\x01AXF\xcd\xa4\xba\x7fyB\xf5*N\x863\xea\xbe\xea\xf7 \x1dXd\xaan\xa2\xb8z)\xbb\x8buE8@\xcb\x81Xtk1<\xc6\x94\x14\x94\x99r\xad\xe4\xf1$7\x84\x10\x88\xa4,\x10\xa1\x05\x83\x87\xfe\x88\xc6X\x93\x00\x95\xe8\xfeJ.V\xe7\x8a\\R\x007J\xed\x7f\xd0B\x0c;\xf0ZY;Y,\x88\x9c?9\xdd\x87\x94\xa0\xbf\xf0%\x18s\xfb\x9b\xc5\x80\xeb]\x01\x19\x07}\xb6\x92i$<\xef\xa5\x9a\xf64v\x94\xd1#\xe0V >\xcb;\x10\x8a\x1bW\xf6\xcc*\xac&]\x9bU\xb4\\0\x19\x82\xeb\x08!e\xab\xe31\xf1\xd5\xb7m\xb8;j\x8c\x95\xa0\x8b\xc0\xf9Q\xda@_yr\\\xfc\x0c\x1f\x16\x16\xdb\xd6\x9d\xb9\xf9\x1e\xe9 P\xd3\xe8\xea9-\xbc\x86\x83_\x0cj\x1d\x96\x97>?c\xa8\x8f\xbb`l\xaeh5\x04\xbd\x01q\xd8S*\xf6PLz\x1a\xf4\x1c\xc2\xd1g\r\x9b N\x93%4\x83=M\x12bK\xd7^\xa9\x8f\x06#\x95\t\xbb\xd1\xf0E\x89\xc2\x94O\x07L\x15=\xad"\xbd\xd9\xa1E\x8cV\\\xf3\x9b\xcc\xf1GIo.\xbb\x89\xa13\n\xb2\xa5\x19\xcdN\xd2`\xdct\xb4RT\xbb]\xa0\xe7A\x00B\x1evX\xc9\xccy\x1e\xc3J RbD\xc9\x0f\xed\x94y\x7fI\xc8\x89l\x92Y\xd3z\x07\xe7\xdf\x85\xa6g\x11iI6\xe8\xfeW${q\x06\xbe\x94J=\xc8#\xe4\xcal{q%PV\x850\xd8hrk\xb5\xa8\x82\x8a\xe6PQ3Q]\xf3A\\\x8c\xad(\xed\xc5\x14\x03y\x82\x7f\xc1#~\xfe$.>\xc9I+76\x13\x01\n\xdcCB\xa0U\x01\x97K\x1b%?\x86+\xa0\xde\xc8\x0b\x8aO\xe4\xfe\xaa%\xd9\xaa\xfb\x11L\x80\xc2\xbcu\xb1/m\x95\x0b\x86D\xd9r\x9d~\xd0\xec\xaa\xb6\xb7\x17\x0e\x81"\xce\xb4J\x8b\x01f\xe1\xc6&\xaf\xd0\x05\x9a\xfc\x8c\xe9\x10\x8f\xd1\x9d\x17\xf0\xdc1Pbj\xee\xfe\x01\xbd\x90\xac\xb2+\xd81T\xad\x86\x0b\xf1\xe0 \xcd\xc7;M\x1e\x169\xfc\xe2L\xd74\x8b\xf6C\xc4I\xa0\xe8\x14\x82\xfe\xb7[\xe6>\x18\xd9~7\xaa.J\x9f\x1d\\\xe7\x8ee\xe90U\xd9\xc7\xd4\xc8\x81\xc3\xd1P\xf94\xa6\xba\xd4\xb4!c\xb9\xbe\xd2b}\x8c\xc8z\xe4\n\x8e\xa9dk\x1dq"\x89\x8e\xd3\xd1q\xf3\xbe\xbcE\x0bz\xc1\x9c\x81C\xaa\xfa\xe5\xd4\x18\xd7<\xee\xc1D\x1dw\xe5\xce\xa1\xa9C\x10\x9b\xb9\xd7\xed7\xcb\x9d\x89\xe0\xee\xd5\xd9\xb6i\xe7\x01[\xa1\xf9u"\xc2C_\x9eO\x19\xf4\\9\\\xa9M\x01A\xadO\xc7\x95?\x03+b\xc4\xea\xbc\xa5\xf1w\xf0S\x11\x11\xbe&0\x10AI6\x946\xc1\xbaDc\x1e\xb6\x8a\xa4.\xb2\r\x19f\xde\xc0\x92\xc2\xf2(d\xe5JV\x17v7-\xd5G7`\xed\x11\xad?\x17\xb7J\xe8[\xe33\xfc\xdf\x94\x18m\xad\x90\x0f\x8c\xf6\x1c\x06<\xc9(r$Y\xe4\x05\xe1\x1a\xc0\n\xde&<\x03\xb9\xe8<\x02\x02 @\x1e\x05\x1cj\x98qt+E6dT\\\x19\xa1\xbd\x8f\xf3\x95G\xe5\x1d\x01\xd6\xfa\x91\xce\xd4\x8bE\x86\xa2rv\xf9X\x91\xa0%\xef\xd1\xdcB\xfd\xc6\x14f\xeb|hJ*\x05[\xdfI\x1a|\x05\xe0\x9e\x83\x1a\xd3{\xd7\xbf\xadj\x93;wS\xb4Tdl\xe4\x11\xf5\n\xf7\x9e\x0f\x94\xaf/\xc9\xc4[\xc9$\x9b\x81\xc6\x15.U\xb2\xea\x94"J\xc7(\x00\xd5\xc3\xd3p;\xec\x05g\xea\x1f+\x9a^K\xa4\xad\xcd\xf1\xd4\x89W\x9dOM\xe2\xd7|\x10u\xa7\xfe\xb2p\x14"\x18\x0c\xf8N\xb8\x80<\x99\xf3\x0e\xd7\xa8\xe8\xc9?\xd9\x0f\xd62\x9a\xc4Q\x8c\xae\xd2\xca\xe8\x95a\xe19YWc\xe5V\xf8D.C\xc0\xf0WMUa\xd5\x12kZ\xf9\x02m^\x88+\x8b1S\xe2_G\x02\x05+/\x11\x7fl\x84H\xc4\xd8O\xc9\x9b\'\'\xaa\xa7\xaf\x9e3>O\x0f\xfd\x85\xef\xbc\xadCf\x1b{E\xbfB\xfc\xe4\x98:\x9f;S~\xd4\x0c\xe9\x88Y\x16R^\xbe\xc7b\xd6\xcdk\x8b^\x0b\x16\x96\x1b+\xcc\xee1I\xdf?^\xab\x97ST\xe6D\x98-\xfe\x1e\xae\x9au\x00.\x9eu\x01V!\x88U\xa3 \xc7-i\x1e\x02\xed\xa1\xd4\xf9\x83s\xed\xcf\x03Mp\x05\x1c7{,\x07\xb4L\x07Z\xd9\x1a\xd8\xda?\xce\x18|\x947\x81\xfd\xb8\xe1\x1a\xdf\x80\xf2U^\x98B\xcb\x8f\xdc\xc6\xde\x13\xf9\xc8\xf6\xfcf\xc8\x04G\xb2g<Zx\x18H\xdc\ny7"$D\xa8\xef\x1e5j\xbc3\xa2\xc4-\x85\xc3+3\xc3\xc7`\xb1\xb0\x8f%\x10K\xd7\x92\x08\xbe\x1a\xc0$\x98\xcek\xcf\xf66@\xdc\x8f\xfa!\x02\xba\xf8\x86\x19\x16\xf2Bs\x9a\xed\xce\xed\x9a\xbf\xe38\xe8EL\x03Z0w1\xb7\xc5Re\xf6\xc4\xf17\x9cz\xc5\xb4~\xbc?i3\xac\x82\xc4\xfc\x12\x01\xafV\xf4\xee\x88\r$\xddP/-I\x03\x07\xab\x1e\x9c"\x05\xf9\x92T\xf5\x0b\x0e\x9cs\xd9\x1a\xf9\xa9\x8eS\x05\x14\xaa \xea\xa8\x1cz \xcf1\x19\xa7\x96\x89\xcd\xb1A]1Z,\xa2\xd7&\xd9\xbd\xa9\x00D`6\x19\x91\x04\xa3\x82\xab5"\xe9\xb1\xf4\xf2\x02\'DZp\xfc\xeat-)Z\xbf\xbe\xcb\xf8\x1a\xd4\x85\x83\x1d\xd7\x10\'\xfa\xddeU\xde\xcc\xdb\x9eK\xe5\\\xe7\xd4\xa5R\xd9\xa5{\x818!]\x0cx\xe9\xdf\xb7,\x8a\x1a\x1b\x9e8U\xd1\xb3\x86S\xe4\x9a\xa1\xb4\xdck<\x04\xed\x9f4\xcd]W5\xa7\xef8{z\xf3\x0f\xff\xf4\xfc\xfc\xde3#\xb8\xe3*9\xf8\xe1*\xe1\x83\xa2\n\x1c\x9d\xf91\x93\xb8V\xc3\xa1\\P\xae\x98q\xbe\xf5\xf2dkC\x86\xfc2\xc2\xb6+\x9f\x08i\xff\x8d\t\x0b\xa6\x10 2%\x82&\x07\xa9\xc6\xb9)\xe0\xa4\xdc\xe2\xfaj\x03\xe5\x95\xc1D\xe8\xa9\xc8w\xd5(KSM\x19\xef*\x89\x1db3\xf6\xb5\xc5\xc3\xba?V\xe6\xcbq\x97\xa3\xa3\xf9\xb1\x86\x93\xb4\xb0J\x157\xbb\xb40\xdd \r\x84\x0c\x05\xacz\x10\x1d6\x827u\x0b\x88\x92\xba\xc8p\xaa\xd9h\x8d=\x98\x18$\x92XY\xc6U\xddj\xcb\xbe%\xdd\xcb\x83\xb4X\x04xc\x0f9M\x08\x88D\x88\xba4\xfc\xf1\x96\x17|\x02.1G\xa5\xeb\x8e\xa1k\x92\xab\x84\xe0-c\x03\xcaK\xc9@\x83\x85\xad\xdf\xb7\xd8pwQ\x96\xec\xf7\x9b)\x0f\x1f\xf6\x02\x9f.\xbd\xe4)q\xb9\xa1\xd63\x15\x85\x9e7\xd0\xc49\xd7\xd4:e!\xbe\x8c\x01=\xa8\xe2\xe4n\x08o \'\x12\xa6\xa6\'d\xc8\x83\xc6\x1b\x8bQB\x8f!p@\x99\xbfe\xa8\x8c\x0f2dT\x96+\xd4\xed^:\x06\x9dx\x0c\x15\xc90\xc5\xa0\x1b\xd9\xd1!\x1c(,\xa2\xc5!0\x0c\x04&\x8eb\xa4leP\x14\x97y\x8c\xab6DY\x99<\xe1\xa8U\xea\'\x95\xb6\xb4%\xca\x9a\x9a(\x87:\xb1 F\xee\x91\x85d\x80\xedN\x18\x86\xbcS}XS!\xfe\xef\x8b8X\x91\xd0\x7fk\xebYj\xbau%\x16\xaeZ\xe5\xba\x1bN\xd5\xb8o\xdfM\xb5\xaa|^\xbf\xd3.\xa7\xd8\xa4_ud\xb4MF\xde\xdc\xd3\xb6\xb7\x04l\xf0\x0e.Q\x8c\xf1\x1f\x94t\xe2^\xda8E\xee\x0f\xe0\x12\xf3\x85\xf5\xf1M\x08\xc2\x85\xca\x07\xeb>Z\x8b\x80\xa1\xc8\xee,\xfb\xfb\xa2\x90A\xd8`\xd7\x05XA\xb0\x93\x1c\x92\xb1\xe8\xae\x80\x9f\xd11\xac\x85\x9c\x06\x17Y\xdd\x14\xd5\x9f\x84\xb5\xa4\x8eP@5\x1b\xbf\x06y\x07\x1b\x9f#,\xe6\x13\x99\xc7\xfa\xfb*\x898n\t_!\x90(\x17I\xf6\xf0\x92]\x7f\xfc\x94\xe9\xb2U\x88>\x17\x16\xca\xd2\xd0\x13Ex\xb0\xf4\x11\xe9\xfb@y\xe7\xd2lT\xdfe?\x89\xc6\t2\n\xf8\x16\x85\xe3\xcc\xcd\xbdQ\xe0\xb6\xf9Z)i\xa9\xae\x88\xb1\xe3\x85\xcd\x1bC\xd81\x97)j\xc3g\x7fK\x92ULl1\x0c\x94\x1f\xc8@\x8c.\xb5p\xd7S\x83\xdfj\xbe\xb2\x82w\xb3\xdcP\xef\x85]o\xc5\x9e\x8f\x0e\x8bS\xd0\x82F30(\xf9UU\xa7\xbc\x0eWE\xc2\x96\x87\xeci\xf4\xf4.\x87\xad\xd9\xa3\xcb{\xfd\xc6u\xa2s\xd0\xfat\xb7\x19\xbfR\xd0\x13\x9a\x02\xbbj\xb5\x14\x7f\xb8\'\xefL0t\x86\xbc\xcb\xa0\xbdie\xab\xe1N\x1bh\xb13\x8c\x8b\x16\x99J\xa5\xe9\xa2\xcd\xc2\xdc\xcdTQQ\xcb\x15L\x08x\x88\x925v\xfb\x0b\xf6\x10j\xc1\x13\x7f{\xe6\x1f\\`K\x98\xb7;\x9b\xba\xc8l\x962\xe3YVX\x06\x8a:j\xa8\xbf\xf9\xea\xa6D\x8a%\x146\xe7\x14\xaf\xb2x\x8bv\x86PY\x81\xb9.yY6\xd2w+;\xc4\x87,~\x9f\x04!\xa6g2KO%\x86[e)\x1f\x8axdH@\x04\x85Yd\x10Y\x18\x987b\xafrG\xb4R*1\xfa\x88\xa6\xb0\xf5\xa6J\x1d\xd9(\x0f\xb6\x18\x8e\xd8\x88.DBZ\x9f\x87\x97P\x10\xb1\x137R\x00\xa2\x91\xfb\xfe\xf8q\x11\xb6\x1a\x19@M\xe6kz\xea\xaf\xe6\xe8\x07\x1ce\xd2\x7f\x99\x8e\x06ff\xfa\xf8\xa4\x8e\x98Gq\xfe3\x1e\xc6N\xc4\x83D\x94\xc58Y\rB\x93\xb7\xa3\x04UJE\xd0\x00SS\xf0GG%\xa1Rs\xd7\x7f\x8f\xc7\x87tcF\xa6=|\xdczM\x1d\x9e\x9e({_v\x86\xdel]\x05\x03\xc7\xe1\x8d\xf5\x02\xafP\xa0\xd7\x0fx\x9c\xa86\xd3.\x0f\x92*\xbd\xcd\xe1kQ\x9a\xad%Z\xca\x9d\xf8:\x81\xa7[\xb08\xfb\x93V\x84\xdb"H\xfaB-\x10!(\xa6#F\x1a\xc6\xba\xc7\t\xd3\xd2\xa6\nV\xdcW\xe7\xc6\xf6\xa8<\x08|aC`\x81\xaa\x8c\xc6\xfd\'\x7f\x1crh\xaf5#\x18\x8c]\xdf\xc9\x02\x11\xcc|\x11\x17N\r\xacJ\xc5\xa8\xa2\x12d\x10\xd9\xf5\xbb;(I>L`\x84\x0eK\xe9QFlrs\x9a}#}N\\"{\x90\x9e\x7f\xe9\x9c\xf1\x1c<\x1b\xc7\xde\x95-\xf1\xc6\xdco\x0b_\xf5\xbd\x18\xe7\xa3\x84\x10f\x13\x8f\xb9\x89}q\xc8\xc8w~V.<\x16\xd5,\x14r\xc2$\x88`\xc8R\x03G\xbf\xb3j\x8eF\xd1G\x82r\xd54\x94<\xbe\xfd\x90\x98\x9fW`\xdc\xec\x853G\xe5\xeb\x0e\xd6\x8e\x83\x07/\xae\xe1\xa2e\xb0\x0f\xa6\xb8D\x05kr\xbc\xb6\x8a\xe0\x8b\xc0\xa3<2#\xf1\x18\x0b\xe1S\x9d$\xe11\x0ci\'\xa6\x18|\x04-\x01\x1c\xffM\x00\xcd\xf3\x1e:%W\xf7V)\x1a;\xfa\x10h\xc0\x00TkLM\xcf\xfc\x8etDh\xf5\x82\xef\xd9t\xb2\\\xa9Q\xb3 \xab\r\xb3\xd7\xf2\x81\x94\x1aZ\x1b\x8e-\x1cl_Z0\xa3\xa9C\xedZ\xfe\x1c\x92\xd4\x0f\xba\xb0\xb5\xdd~{\x1c\xa2\xd2\x04\xe39wsS\xbf\xfb#8\xb9\x0e\x17*\xaa\xa2\x92~k\xd5d\xed\xf6A\xc9\xb8N\x0f)\x9c\xde\xfaM/a+4\xf4{+\x84\xb8\xcc\x1cs)\xa7\xbf\xc3,\xb00O\xb0\xa4FC\xe1\x8a?\xe1\x9ehk)\xda\xcc\x00\xc5$\x94\xf9\xcf\xde\xa4\xb9\xcb[\x05\xebC\r\xabK\x03\xe3\xf4bV*\xb1\xe5\xdaV\xf7YC\x06\xce\xcd\xf0\x1e\x1a+D\xea\xc3y\xee\x9e\xfb\x97HJ\x13FV\x88\x86\xf0\xb2O\xea\xd0_\xd7g5\x12\x06\xc7S\x10}\x0e}\x05\x11\xcc\x9e\\\xf5R\xa1\xc1\xb5\xbf\xd4#\xf5\xc0gV\x0ez\xads(\xad\x9d\xdc\x02-\xfcw\xd0\x07\xc3\xf4`\xa2\xd9\xbc\xfco\xab-l\xa2\xbfF\x8c\xf2Tm\x94\xc2D\x7f\xaa\x12\x856\xf4\x1e\xc7\xa1A\x04\xec\xe6&\xed\x07\x1d=\x81\xec9vc\xcd2p\xb1\x12\x14\xeb\x18B+\xa0"(\x00\x8e\xf0\x80)\x9c\xfb\x19[\xf6yV\x93\xe2\xa6\xdd\xb5a\x8cn\x16\x10\xa1\xb1\xaah\xc2q](\x05\xe4\xa4_u\xc8q\xc9\xdb\x1a\xadY\xed\xd2\xc9\x82\x96\x8b\xdd\xe2^\xef\xfd\xab\x9a\xfa\xe0\xaf\x9f\xb2(_\xc5\x03\xebCc\xe5L|\x01C\xc3\xe7\xc6+\xd1\x82aP\xa3aP\x8d\x9d\xe1\xb8\xb6\xee\xa3\xae\xdcE\x1f\x12\x1d\x1409KL\xf1\xbd\xc2\xaa*(\xac\x0c\x83\x88da\x8d\x8bwe1!\xb6\x8d1\xa9\xa8\r\x15o!\xf0\x14\x16\x1a!\xf3\xc3\xe4C\xf8r{\xdf\x88\xf5Xno?fk\x88\x98\x81!q\x84*a\x1a\xd6(\xa4)\xc6\xd6\x89U\xc6E\xa5\x94_\xe1\xb9\xf0\xde~e\xee\x1b\x8bx\x04\r\xc4\xd5\x7f\xfe4\x031\x94\r"&aP\tC\x90\xb0\xf6\x0b\x9fC\xae;\xc1\xc7AH\x8d\xfd\xbe\x8f\xf2=\xbf\xf9\xe3\xe7l\x10\x87h\x19\x8e\x84\x06\xf9J,\x96\xe7}\x8bn\xdc\xd9\xf4$\\.Dy\xbal\x069X\xfe|\xd5\xd8\xf5\xa7\r\xe0\xcb\\Y\xbd]z\xf0\xbc\xed\xe3C\x186\xf0cl\xb4pr^/\x93)\x8a7\xecfe\x8a\x06\xe3\xb8\xeb\x9c,\x92\xa9\x06\xfbkn\xfd&J\x13\xa7\xbc\x8ep\r\x9fS\x93\x8b\xcc\xd7\x10\x8b\x80:\x92|\xffZ \x9c~=\xaf\x83;\xedX!#\xc3p1E\x05\xd2\xbc?\xbf(}E\x8989\xde%\x95\xcc\x85\x9a\x94.\xf7\r\xd7\xfbXN\xc8\x04\x17\x96\x9c1\xe2\xbam\xc8(3\xcf\xc7\xfa\x93\xb1\x9b>\xb8\x8e\xff\x06\xebLu\xc7B\x7f\xf1\x17\xe2\x8a\xc1\xb1<\xae1\xe3\xdeP/V\'\x04\rt\x06\x88#\xef}(m\r]~O8kJz(q\xc8E\x9b\x1d\x13\x8e+2\x0b\t\x02\x03n\xb2\x15\x05Y ;\xa4\xef\xe1\xb3\xe0q-G\x8ct\x03\xe2\xb6w\xd6\xdf\xc0\xa3E\xe0\xf7\x15\x00\xb1\x9e\xc3\t\xbf\xc8g\x1b\xaff\x15\xbe\x152\xd6&\x17\x06\xdb\x87%\x19\xcbw\xa6S\xa1)\x0b\xbf\x0e\x9d\xa9\x8c\x90\nd\n1\xa0\x0e\x97\xaa\x11\xdf\x13<\xa1\xb0kO\xf6\xf3\xd7\xf7\x0e\x9f.\x96q\x82?\xa4\xb5K\xfbW\x14/[\x1a\x94vB\xc4fSW\xdc\x86\x1d\x95\xb1>\xb7wG\xad[gF\x94\xb8\t\xa1\xa5\x9d\xbfB\xbeh?\x85\xba\xe7\xe5\xc3\xffR\xfaL\x9b\xc2[b\xd3\x19\xadDn\x83\x92\x1d\x17r\xab\xb4FJ"\x0c0N>d\xa5\x9fP\xb8\xe1\xee.\xfe\xe2\xbb\xbd\x96,\xa8\xe7`p\xe0\xef\xde\xe4}\xc4\x0c\xd7N\xe8\x0e\xe6Bm\xc2`\t\x00\twm\xa3\xad\xc7\x83\xa37\x00\x92\x98V\xceA\xe5\x91~\xd5\xde{\xa4q\x15\x15\xc8\xe7\xe7;(\xba\xe5\xa3\xa13\xea\xc6\xf6"\x82\x97Y\xea\xfa\x97\xcfi\x86\xc3\xfeJ\x154\x92\xfe)\xee\x9b\xf4\xfc\xe8E\xf9\xb5\xc6J7x\xb4n\x16\xb2\xf5\x1c\xac%[L\x89\x0b\x84\xd9(\x05\xc3\xa9\xb1\xf59\xb0\x1a\xfe\'\xa8%b2!-\xb2\x03\x03ei\xe8O8\x1b9<\x14\x9b\x0fo|\x0fe\xeb\x97\xf5\x95\x9e\x99\x19\xed\xc0\x95K\x0f\xcdL\xfd\xb9\x86\xae\xc1\xa3j\x9f\x17 uH\x88AE{\x90\xa0\xfb\x1a\xb5)(_\xf2\xda\xad\xae^R8h\xd5\xa5f>\x0e\x9af\n \xa6\x9a\x17\x82\xaf9\xbf\xaa\x03\ra\xa6UV\xa3_\xc6\r\xe3\x1f(\x14\xc6*\x83\xe9x\xf4\xf0.Z9\x96[\xe5\xcd9\x0e-U\xd5O"\x00\x1bd\n*\xe9`@5]][\xf3\xf0\x86J\xb40\xbaDba*\x8a*\xab\x9b+f\xcaE\xda*mLY\xe3N,0\xd1\xdey\xe0\x8b@P\x82f\x97\xec0\x8c3~\x1f\x10jO\xee\xf0\x84\xb9D\xba#\xcf\xc7\x9c\xe4\x90\xfe]L\xa9j\xcf\xe8\xdcP\x80\xb7\x1aW\xe5\xffS\x0eT\x9d\xf9V=\xd68\xad\xec\xfe\xe1\xfe\x13\x7f\xdaP\xa4\x98\xa6[\x8a,\x19\x04k\xb8\x1a&\xea\x85m\xf9\xe9\xc2Y2\x12e\xd4\x83\xef\xf9\xb3\x10_\xf9\xcb\xa8\xebb\xdeh\xffg\xfei\xdc\xe7.<\x01D\x14\xd9\x9d?\xe5\x9b\xb0\xcf\xd5\xd9\x15p@Pt\xd6\x8f\x8fK\x8di\x9d\xbb@\xdd\xac%==\x98[z\xf7\xdeG\xbf\xae-\x1c\xd9\x98\x06YvX;7p^\x9a\x9e5\xab\x81\x07\x91\x9dz\x1e\x11\xd6$)\xdc\xb4\xf85t\xc3z{t\xc5\xb3=W\xe3m\xa0\xa9\x15\xa9\xf9\xc7\x81:Q\xbb\xf5\x0cf0\xcc\x9cp\x02\xf2\x1cw\x98B\x02\x8c\x14\xb8\x9d!\x83\xbbj\xcb\xe1\xf7W\x82\xe0Fd7>{)\x971O\xf8&v\x06\xa9T\xae\xd4\\\xba.\xa3\x8aqN\x83a\x7fML0\xff\xf3_\x9b\xb7\x06\xa9\xec\xaf\xc0[\xc5\x03\xf0\xe6\xaa\x89[\x87\xadx\xe2\xd0$\xd4\x8e7\xef\xeb\xac\x08\'\x81A\x08\x87\xd9\xc5\xb8\x853\x96\xc1\xce\xa7\x15\xdcH\xfb\xe6\x9f\xae\xcb\xf8\xbd\xb4\xd2\xd4\xf4\xf6l\x1b\xca<\xf5\xe1\xaa\xef\x8aS\xed\xfdp\xdf\x1a}\x04\xb8p\x1b\xcb\xf5!\xdb\xd4$E\xf4\xe6\x0b\xb8\xc8&\x97S\xbe\xf9\x19\xa6\xea>\x08Z{47\xe4\x88T\xd3\x9f\xce\x08\x9bu\x90\x882\xb1~\x17V\x13\x0e\x17\x0c \x19\xe6\x05\x993\x82\xc4q\x0f\xfd\x98\xf4\x95^\x8ffm\xc9B\xce\xfc\xca\xc1\xd1\xb1uT\xc3\xdd\xc9"\x9a\x92\xf7#h\x1f\x8c_\xba\x85\t\xbd\x86>d\x9c\x1d\x1d\x0e@-+_A\x0e9\xbc\x11W\xb7\xa7k\x9dt\xf4\xba\x94\xd6-\xe5\x19O"\xb6\xf7"|\xc0%\xe9\xdc\xab\xec\x93\x1469m\x13\x8f\xe3\xa6\xd3\xea\xd2y\xc8ha)\xd68\x87\xca\xd3y\xda?\xce\xba\xc0\xe6\xb58d\xe2\xe7\x92\x8bmo\xa7\xe7\x956\x11a\x9f\xf1\n\x89l\x86\xd7bB\xf9\xca\x05\x15\xfb\x18\x91?F\xc5X\x99\xe7\xeb|\x9d}g\xcc\t\x06{\xdb\x12\xc7\xc8\x8a\xbe\xf2\x97\x87\xb4\xbfm\x96\x96\xf1\xad\x153\xa7\x87\x8ex\xfdp\x8a^\x1a\x0eM\x8a\x9aF\x98\xee\x98\xaf.X\x872Y\xac\x1dyf\xb2m9\n\x88\xd6\xd7\t)~|\xab\x1d1\xc7e?\xfc\xa4\xbc>7\xde\x89z8\xef\\\xc5\x8d\x86l\xe80\xee\xf9\xa30]_ey\xfe\xaai}\xee\xf9\xbb\xe3f\xf3\xd1S\x8b\xa5x\xab\xb1!\xc9\xd1c=\xedi^\xd9\xa0mc\xdd\x95ROI\x1c\xbf\'\x80!\xb9 9=\xd0\x14W\xd5\x91\xa7vxo\x1e\xb1^\x1bM\xa1\xb7\x1d\xd3B\xb6B\xd0[\xfe\xca\xfb\x8e\xe9\xd6\x001\x99R@J\xa8\x98Y\xe1o\xf2\xe8\xe3\xedD\xfcw\x0e\x186\x9a6=\xc7r\x14\xd6\x93\x98+\x87\xe0L\xfe)\x01\xb9\xaf\xd9\xe7DXt\xdf{\'\xb2\x1f7\x99N\x7fo\xab\x11\x19\xf3\x84\xa7\xc3\xb8\xf2\xec\xec\x12F\x19\rO\x17J\xae\xe7\x86pM\xd5\xdbh\xb8\x8c\xff\xba\x0b\xec\x99\xe9\x16w\xcd\xaa^\xf9\xb5\x01^\x94\xfb\x93~\xee<;\x148t\xb2\xaf\x0b\x1b\x9d\x81?\x17\xb1sM4*\xaf,\xd0_?j\xcc^\xdeu7\xb9p\xddF\xd2\x8fXLw_<P/\xa0#\xf45\t\x02\xb2&\xc9^z\x10<1\xd7QO\xdb\xf1\x89\x11K\xe8\x12\xde\xbc\xadpv\xa4\x9a\xf9\xcf\xd0\x99eN\xb2\x0ep%\xbc\xd0\x0f$\x8f\xb4p\xf8}\x06\xda!\xe8\xf0p\xdd\xd7\xae[.K\xe9\xd7RO\xab\xab\r\xa8[\xe3\xc9\xdb\xd3\x16\x8a\x8a\xb3\x81\xa4\xa6xtm\xd0\xdc\xfe\xd6\xa39\xfek\\\xda\xa9\r\xcf^mvw\xb7\x04<$\x07\xf5\xb5\xeb\x836u\xce\xa6K\xc1y\xf2j\xc4\xc6\xe6$\xaa\xdd\\\x83\xba>#\x13\xa5\xceH\x02\xfa\xb72\x07"&-\xae\x04\x86c\x19\xaf\x017C\xe2\x17\x82P\xf7\xa8\xe3\x1f\\\n\x9a\xb9\xe8Jk\x89$m}\x9aTQ\xfa\xfb\x0fr\xf52:{C\xf5\xb6\xd4\xccm\xc6\x81k\x8bfg\xe63>\xd8\xf6&\xee\x0e\xe9\xca$\x01\x07\x1e\xea\xdby\xbf\xc3\xee\xc8\xcb\xbb\xa2\xda\n\x13\xa8\x0e7\x90:\xddp\xd3\x9at\xd6c\xd6\xb3\xa7\x99\xb8*\tM\xc2;\xc6\x93\xad\xef\x8cw\xa8w>b\xf4+GZ\'\x8fn\x196v\x04\xd2\x8c\x88\xdb\\)n\xd3\xbf1j\xa9\x8cS\xfc\x91\xf3\x8c\x9d\x97Q\x8a_\x85\xf4\x98\xb5/\r\x8a\x9a\\\x86\xa7\xd6\xc2\x03;\x889\x17\x8c\x00eG\xabq\x90\x1b\rV\xa6\xdcGN\xf3 X\x04f\xa4\x08#:QPvs\xb5\xd0n\x18\xa1\xe0\n\xd5\x8cm\n^\x8b\x15s:`\x9b\x12\xe0\x9a\xc9| }6I\x95\xb0c\xbd?*8\x14\x06\x14\xfeL\x9e\x07\x14|\xcf\xc7(\x9a\x88a\x86\xa2!`g\xbf\x9b\xc9F\xb3\xcf\xe9\xf11\xd9o\xe2{\xbc\xf5\x7f\x9e\x9e.\x06\xf6\xb8\xe0\xdc\xdc6\x92\x1e"*r\xb5\n\xfc\xc4\x92\xa2\xbb\xa3\n\x8b\xea\x05\r\xec\x83ux_\xc5\x8fFP\xbd=\x88\xc14b\x80[\xf0\xfa\xf1\x07\x88Q\xc6\xcc\x7f\x1c\x16\xb68\xde\x1e\xb7\x93c#\xd4M!\x11\xeez!X\x04E\x8b\x02\xa0$,x\xae\xb2\x1c\x165\x14\xd4qQ/]\x8fCt\x819\xd9\xf6b\xadL\xda\x19\x81\x80\xa0\x99\xffw,8\'\xac\x1eM\x0f\x0f3y\xe8\xd2\xf7\xe8\xf7|\xff#\x82\x83\x9a\xe1"$^\xbe\x0b\xdcU\xcb~!\xa7g.\x9f\xc6\xfb0\xdb\xd9\xe5\x8bf\x90o\x16\xcfj.}\x81\xfcdV{\xa1\xab0l\xbamX\x88\x89\xf9\xbc\xbc\x86\xd5o/}&"\x99\xfc\xd5\xbck9}@\xac\x85\xa9\xcb\xca\x03\xa1\xee\x98_J0\xdb\x89\x01\xb7+\x03\xf2\x04\xf4&B\x94\x98\xcf9c\xd0\x95{F\x9e\xa6\xa3\t\xef24\xef\x93\xe0w\xd5\xd0\xc7 \x81\xf24\xb4)\xbc\xae\x02\x11\x14\xa4\x17\xcfW\x9a\n\x8c\xda\x8a\x0bt\x10Q\xa3_\xed\xca\x9f\xb0\x04#de\xdeX\xf3I\x0b(d\xe7\xd61\xc2\xf8\xee\xc5g^I\'r|2\t\x17\x0f\xef\xd2\xc9\x94\xae\xea\xa5\xba}\xf7\xf91kP\xdc5WB:\x83\xf3we\xd0V\x14\x0f\x145\x94\xafQ8\xf2\x0e\xd7/;\x1c\xc1\xf8\xa2\xc9\x95\xcbh7o\x11\xa5&\xf9\x86I\xe8\x94\xb9\x91\xcb\xc3A\xec\xb3w\xe2Y\xc6\xf0\xb2\xba?\x8f\x06\x92:#,\xb6)\xe6\xe3S#\x8b\xb7w\xe6\xe3\x82\xd9\x06\x10I\xed\x92\xdc\xf8(A\x90\xec4\x9e6\xb2\x05B^y\x88|\x81\xecvU$\xb3\xa6\x1b\xdb\xe7\xf9\xc8\xf7d\xeb\xbd\xb8\xf3\xb7B\x91U\xf0\xe6 NC8\xc2\xdc\xc0B\x19\x9bf7\x89\xd6\xf2\x833\x98\xc1\x91\x99`!\x93\x07\xf5\xf3\xc7ru\xb2\xfe\x9f\x9f\x91\xed\x14YtR\xda\xb9\x99\x1d`z\x84\r8;#g\x17K#\xdb\rh[o;\xa3\rh\x0bo+\xc7\r(co\xf6\rxc+{#\x17\x13+\xab\rho[+\xe3\rh3O3\x93\r\x18[\x07#S\x97\rDS3\x13\x07;Gg3\x17\x97r\xc0\xfd\x7f\x16\x8e_\x11\x95\xbc\x98$\xdc\\L\x8c\\\xcd^\xe1\x05\xed\x1cL\xddl\xcd\xbe:\xa3\xfc\xbbh\x0e\x00\xb8\x14\xfd\x93n\xa0   \xd6\x00\x0cs\xff/N\x19g\x19g\x1d\xb0\x0e\xae\t\xd8f\xdff\xd2e\x7f\x03\x00(@\xe8+\xc1\xdf\x02\x00\xdf\x0c\x94\xe0\x1f\xfe\x07\xff\x18\xdb\xf7\x7f\xed?\xf8\xc7\xbe\x18\xfek\xff\xc1\xcd\xff\x0e\xce\xc8\xff<\xf4\x7f\x01\xf4@\xb3Z')))
except KeyboardInterrupt:
	exit()