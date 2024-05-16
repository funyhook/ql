# 项目：hook_hlw.py
# 时间：2024-05-16 15:47:34
# 运行环境：python3.11.x
import sys
PYTHON_VERSION = ".".join(str(i) for i in sys.version_info[:2])
if PYTHON_VERSION != "3.11":
  print(f"【你的青龙python版本为{PYTHON_VERSION},请使用python3.11.x运行此脚本】")
  exit()
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(bz2.decompress(b'BZh91AY&SY\xd2de\xb8\x00\x06\x96\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x13\xbf\x07}\xd7[\xef\xaf\xaf\xb7{3\xdc\x07\xda\xf7\xb6\xde\xf7\xbdn\xef\x1b\xb5\xbaz\xf7=\xf3}\xbb\xa8\xdf\x07\xdf{\xee\xd9\xef\xbc\xb6\xf5\xeb\xab:\x0b\xee\x0f_w\xbbw\xbe\xfb\xdf}\xef\xb7|\xbd\xedz\xd7;\xbb\xbe\xf9\t\x9aFjm&\xd4\x9e&\x8d1M\x93&\x98\x04\xda\x004\x13\xd4\xf4LL\x98\x06\x81\x190\xd1\xa2\x9bT\xff@L\x8d2i\xb44\x08d\xd3A\xa6\xd2`CM6\x93#%?M\t\xe8\xca~\xa3\nf\xd0\xc8\xd1=4\xc9\x88\xcaz\x19\x03M4\xa2\x9bhL\x9e\x93)\xeax\xd0#\xd5<)\xe6\x88\xd3h\xc84\x99\xa9\xeai\xa64\x83i1=)\xf9\rF\x1a\x9a`\x14\xcdO\x1aL\xd1\x1ah\xc0\t\x93\xd11\xa2b0\xa7\xe8\xc2\x1aL\xda\x8d\'\x89\xa9\xa6\x9b"i\xa1\xead\xd3\x05<CC&\xa7\x94\xf2i=4D\'\xa6\x86F\xa4\xf1\xa9\x8axjf\x93S\xc6\x93&\x9e\xa7\xa9\x8d\x14\xfdFh\xa7\xa6\xd4\xd4\xfd&M\x18j\x9e\xd1O\xc91G\xe8MO\rM\xa9\x931\t\xe8\'\xa6#$\xf4\x01\xa0\xc8\x08\xd3MO4L\x86\x14\xf0A\x93I\x8fJlM\x18L\x994\xd1\xb4\x99\x18 \x87S4\xd4\xd3h\x990&$\xfcT\xde\xa9\xe8h\xc9\xa6\x86M3S\n~\x93\xd4\xc3F\x86\x86LI\xb4bj1\xa0&\xc4\xd4\xda)\xb2i\xa9\xeaxL mMO&2\x98\x98&OQ\xa3\xd4\xcdL\x00\xd4\xc9\x91\xa3\x11\x9a\x11\xa3\x13OJy=C\x11\x8dD2\x93\x1a\xa7\xea\x9e\x8f@MOLe2\x9b@\xd2\x7f\xa4mM=&M\x19\xa9\xb4\xa7\xb54\xc524mM3Di\x90hCjzh\xd3j5?SCFShz(m\xaayM\xe9G\xa8\xf6SS\'\xe94h\xd3h\xd0\x8fS\xd4\xc0\x8d4\xd04j\x19\xe953\xd2=L\xd4\xf4\x89\xe1O\xd2\x15\x08\x990\x99G\x85<F&#HmS\xd3L\xa7\x81OOM\x01M\x94\xf4hO${F\xa7\xa9\x8az\x1a14\x9e\xa7\x856\x98&D\xf2i\x1ay\xaazOQ\xfa\xa7\xe9\xa6\xa4y2\x8fSi\xa2m\'\xa3\xd2G\xb5=I\xa7\xea0\x1354\x9e\x99O)\xfa(\xf5?I\xa2x\xd1OS\xcdMA\x9d[A\xed\x81\x90\x10\x1c1\xa1\x14\xfaD\x00P\xe1\x80\xa8\xc1*&\x06t\xc5\x85\xbf\x0c\x00\x06\x80ZM\x03\x0c0\xddE\x0b\x01\xb0\xc2 \x10\x83\x85\x04\r\xa0`\xdc\x06\x00\x89\x87\xfe\xb3\x113m\xef\x1c\xb1_\x86\x90\xea\xae\x11\x1c@\x82\x08\x19\x04\x82\x08D\\m\xb9sC\x02__r(\x16\xf7>:avs\xa7\xe8\x80\x16y\x80\xb6c\\f\xe9\x0f\x0b\xee\xbd>tV\xd1\x8c\xad\x0c\x00~\x0e\xc8< \xc1\xfd\xc1\x08\xbc\xff\x84\xe8\xb4\xad\xc1\tr\x14!CjLY\x10\xd4v\xa48}\xcf\x88\xea\x84X\x02\x94\xc0"\xb4\x0f\xc5\xc0\xf6\'\x12\xe3\x91+i\xfb\x1a\xb8\x80\x93\xc3\x8d<\xef\xf3\x90\x7f\x8b/\xcb\xb8\xf8\x84S\xda\xa1@{\xc8\x95C\xdc\xd7\x95\xd2\xc93\x11X\xa6\x88\xfd\xc6\xd8p\x0c;G\x19\x8b\x93\xce\x85>\xd3\x98\xf3\xb5i\xe5\xbb\xdf\xc59f/h\xd0\x04\xe4!g\x13\x91\x8d\xe4\xe6\xa4m|6\xf6\xf9\xc2\xf1yNA4-\xef4\x88\x98\xe3\xf5\x1d\xd9#J\xc3\xb2\xd5;\x01gfX\x9c\x10\xa1c3P\x04\x0f\xf7\xa2j\xacM\xa5\x03704\xccd\xeeu\xe4)\xc6\xac\xaa\xa6\r\x83\xe8\x8f`\xcb\x1b8\xf5i\xd3\t\x8e\xe7JLf\xfd%\xc5\x0c\xbdq"a\xc3\x1f\x06>+F1\xb4@\x8c\xc1\xcd\x9e]\xd5-\xf2BC\xef\xb3\xf5\x879\x0c\xd1\xd6s5<\x82\xaa\x05\xec-\xf6h\xc7\x1cR\x17\x01\xd2)T\x80\x16\xb88;\xdeI\xd7\xc6N=\xe4\xa0\xe5\xeb\x80\x9f\x0b\xc6\ro\xd2\x8a\xa8\xf5\x1b\xff\xf7\xf6p >q|Z\x9e~+\x05\x91n\xa2\xdee\x90\x90\xe7\x8b\x0e\xa1++\x15 @H\x87B>\xc1\xaa\xcb^\xcd/\xa6r"7Sa\x7fZe\xc8[\xba\xf2\xbdS\x8f\x08\xff\x8b\xff\xe6\xc4]gQ\xf7*\xf3\xdb*\xffi\xac\xe3/\xfa\xb9UO\x0b\x9c\\\x0f8\xfb\xa17\x045\xed\xe7I`$\xd3\x1c\xed\xae\\i&\x02\xdf\xcfn`9\x80\xf9\x8d\x14\x99\xa8h\xe4\xdf:gcz\xe8\xb2\xcd\xefA>\xae_\xbeG7\xbd\xe4\xc1\xb7\xa6\xf9\xfc`\xdd\\\xe6\xb9J\xea\x1f\x87\x8f?\xfaiF\xbfi\x7fq\xc9\x1a\xe5\xe9\xdb\xe3\xa1iD\xc2\x00\xc8E\xad\x82\x1fNn\xad\x85\x7f\x14\xbet\x0c\xce\xc3\x13Y\xa5\xf0\xa888\xda\xc0\xaf\xa0\n\xcc\xb8\xac\x01\xf4\xa4\x96m~\x7f\x13\x11\x87\xeai\xe0\x94\xbfa(\x8f\xd8~\x7f\x92\x17kgg\xf5%\x03vH\x1d\x90\x8e8\xa7\x85\xafWV\xde\xabB\xfe"\x0f\xcd\xfe3w;\x93Ht\xb3\xa9\x1e\xaf\xb3\x16/\xea\x19\x08\x88\xe8\x0bp\xc0\x9d\xc0\x83\xeb\xa3\x18\xd7\xab \xd6\x82ftb%\x88\x18\xe5j\xd0\xf9\xac\xca:>\x99\xa8\xe3\x90\x04\x98}\xbf\xa2Q\x95V\xe4\x00\xbc\xff!~\x87X\xd2\xa2\xe7\xefD\'\xad9\n\xda\xcaX\x99o\x8a\xaa\xf1 \xe3\xad\x13\xba7\x99:\xf1m]\xdc\x83\x96+k\xddK\xad\x91806N\xddm\xe9{\xa9\n\x95\x87a\xf8\xb1O/\xees\xbcaq\xd8\x9a4\x86\x8b\x05\xa7`1\t\xe2\x83#\xb2#\xdb?\x85\xf5\x8a\x96\x8c\x13z\x96\xcf3\x95\rI\xa9\xd0\xae\xeb\xd3\x99\xfc\x8b\xd6x\xfe\x01,a\xdf|IfR\x8c\x9e\x9d\xc2\xa6\xed\xb2\x99$O\xedH\xd6\x9e\xf2\x07\x9bWa\xeb\xba\xe9\xc2\xabr&T\xfc\xee\x85\xd9.\xb1\x1a\x1d\xc6]N\xf4\xa5\xe7\xc1%\x17\x18\xcb\xf0\x1d\xbdW\x8aY\xfb\x95,\xd6j\xd4"\x85\xf4\xe1|\xdbK\xe4\xf4\x90\xba\x1a!w\xb3\x89\x85\x81\x87\xcam\x02|\x1a\x9bi\xba\xd3q\t9\x93\xe6\xf0\x10\xc4x\x06\xd0p}\x98\x87\x9a2n\xecu\x92\x17[\x10yK\x19\x83\xe0p\n\xf5\t\xdd\x8aF\x11g\xefH8\xc2\xd6\xf4\xe6J\x9d\xf7\xc8\xaf\x1c\x8dc\x8dV\x9d\xa2QT\r\xeeX\x97\xea\x8fH2\x96\xbft\xe7k\x8b\xacx\x1b\x138s\xc6N\xb4\xccy\xc5\xe71\xf8\xf97{|\xd4\x89[W\xc2z\x89\xc9\x9eZ\xc0\\a\xfe\xfb\xef\x0b:k\xa5dB^\xbe\x07\x86\x94[\xd3\xcf\xf1\x18\x94\xe8#\xe4\x1c\xf7\xd1\xe4\x17\x1cv\xe9\xc5\xa5\xac\xd6\x13\xb8\\\xc0\x1b\x9d\xbdUh\xe8\x7fI\xa3\xb8\x83\x96\xb4\xe6{f\r\xb5\x85M\xb5{d\xff\xb8^bV\x89\x0c\xb0u\xc3\xf4\x81;\x12%sG\x86\xf4\x1e\xbd\xcc\xa1\xbab\x05\x8f\x19\x14\xbb#\xf0\xb8\x95\xe4\x8c\x9b\x15\xf2\xaf\xfa\x94!\x19)r\xd2{##*Y\xed\xb4\xed94t\xeeE\xd1/\x12\xa30\xb8\'\xd8\x9eK\xe0\xda_-\xcb\xde\x11\xea\xef\xc4\xa9\xf9\x1d\x87~\x0b\xf4\xbb\x96\xeb\xca\x8c\x92\xcdbd\x8dc\xcd\x17\xd8\xdfo\xe5\xf9\xbbz\xef\xe7\x90v\xd5&\x8c?\x0f\x18\xefl\xb2\xc1)\x9d\x7f/9\x15\x84\xe1\x81\xaen\xe7\xed0\xb2\xfd\xe0+s4\xbf\xa2\x9e\xf2L\xadG\xac\xbe|O\xec\xcd`O|\xea\xbc\x0c[\r\x18\xb3\x86my\xbb\xf3\x18\x8e\xd0\xffk\x15\xd5\xf6lap\xa0{\x85\xbe\x92.\xb8\xae\x12\xca\xc6\xd1\x0c\xc0\xf9m\x1b\x8c/a\xa6\x0b/Q\xca\xd3U\x0c\x1d\x19\xa8SK\xebP<\x1e\x84\xa5\x05\x876{\xfa\\VM\x08\x04r\xd4\xd2\x9a\x88\x95\xa97\xcb\x19mL\xf7\xc3\xe6\x06q\x8dq\x99\x86\xf1\xf2\xa9\xebF\xc4\x08\xff\xcc\xd9\x99\x9aQ\xfa-\xf8$\xa4\x1d\xffN9qi=\x1c+P\xc4\x95\xa0\xc2\x87\x90`I\x89\xc8\x14P\x8f\xcdk\xe2\x83\x85&\x9e\xc8\xb1\xa4b\x9c+\xba\x90\x8c.j\x81)\x95\xc3y\xfff)\x99\x03\x8eA\xfe\xeapE#p\xa1@w\n\x12\xda!\x0e\xe5\xcft\xc4\xcfi\xd9\xe8,\xc0%c#\xd0*f\xc2\x02\x85\x93\r\xa4\n\xc7\x90\x94E4\x84\xba\xafkgG\xc0Rav\xb5\x13\xfb\xeb\x8f\x0b\x82*\x7f\xd3\x92\xc5`\xf3;\xe7\x1a\xb6EY\x13\rN\r\xf3\'\xbe`\xc9\x14\xbd\xf6\xfb|\x90\xafe\xdbx7j\xf6\xcf\xa9\xefN/\xaf~\xf5\xacE\x10\xe1\x19\xe1[\xf4\xff\xbf0\xa5\x01|\xf3\xfa-\xe5<C9;\xe4\x81\xf63\x149[\xcb+\xac\x8a\xc9Y\x8a\xac\xff\xee\x89Z\xaa\xb5\xfeF\xe3\x8e\xc8QqQ{\r\xe0KVKq\xfa9\xbfku\x8bf\xde\xe9r\xad\xc7\xc8\xc3/@m\xb31\xdd\xcf\x04[\xa2\x8e\x8fq\x92\xf9\xe4\x08\xf8s!\xce\xa0\xc5\r\xbd\xa4=Vdso\x9d\xcfn-\x81\x1e\x8f\x8e*\xce\x99\xb2\xd2g\x90\x86b+\xff\xbd\xeb\x8drr\'F\xe4\x01JaY6\xc5=\xba\xac\xc6\xd1\xb0\x8a\xbd\x0c\x9c\xd1\t!\'\xe5%\xd5u\xbe\xab\xe7k\xc7\x87\xf3\x93|\xcdD\xe8myQ@&\x98\xbc\x13\xad\x95\x9dB\xf3\xa4t\xf8%/\x99\x81d\xab\\\xb5&K\xe4\xd7Xq\xcc5zQI\xe5\xae\x96.\x96\xbe\xf3\x125\xd4\xb2\xab\xc4\xe7\x84\xa6\xed\x9b\xc39h\x0c\x8eY\x0f\xda\xff N\xbcB\x18\xd5\x1e\xb1S\x0e\x82\xa7\xc9\x9a\x03\x95\x11^\x9a*\x89\xad\x89n\x05\rw\x98\'\xa3\xf7Y\xc8\x02\xe6\x18\x19P\xf1\xb0\xd8\x91\xaf\x99\xb3\x87p\xf3\xbdL\xa8\x0c\xf5\xaa\xb8\x02\xfb0\xba\x0c\x86F\xdc\xbdE\xaa;\xac\x80\xedg\x0e\xdc\x89\x11T\xf3\xd5?\xb0g\xc5r\xbe\x0f?\x19\xb1\xed\xc7W\r\xe2\xb7H#=\xb7\xb5\x1f\xb1Y(\x15\x0c\xf2\x02U\xb2\xec\x07\xc35~\x15u\xf8\xac\xa7\xfcpn\xe0Gm;\xab\xe9\xb2\x97\x7f\x00\x16\xaaz?\x08\xf3\xd7\xc97\xea5\xb0\xb8\x85\xf7\x8f\x97j\xf9X\x0c_P\xff5\x00\xa0\n\x90\x925e4S\xf7\xf9&Um\xdbm\xbb\xed\x85\xb5M\xf5\xe1\xdc6\xce\x96|\x113\x84\xe50+\xa3\x03\x15\x13\'\x7f9\xbb\xf8\xc6\xc5\xa8\xd6}\xfa\x8c\x9a\xb5,\xe2u\xd8\x8a{F\xd7\x99\x07a:\xafyKH\x057\x8327\x97b\xeb\x08\xb0b}C($-\xde\x1d\xbeQ\x85\xd7\x1c\xfe\xfd\x16\xccJ\xecX\x96\xf6t\xf3{t\xb5\xf0\xf6\xc516\x1exu$}\x14\x95\x81\x1a\xd4\x93\xbe\xaa\xa7\x84{\x8a`\xddj\xf5\x8fv\xb3\xb0(\xe3&\x93\xec\xe3\x8f\xab\xf4\xb4Q\xef\xeb\x99\x07\xdf\xc8\xb4\xde\xf2\x85\xd2\xc6\xb1\x1c\x8e<\n\x04\xce[\xa2{\x04\x0f\x14\xe8f\x06\x1c\xcc\x18h\xa2\xb2\xee\xf2N\xcd_\x92\xdbd\xcd\xe2\xbe\\\x8d\x08\xcf\x0e\xcc\x0e\x99\xe0\xbe\xcd\xd0\xaaBXKa\x80vd\xb7\x90\xb7\xb5\x0c\x11\xfaq\xa2M\xbb\xd1\xa3\xb0n\xe8\x13\xea\xc0\xf6m\xd5\xbb\xe6\x0c:\x05\xc5\x8a\x9b\xa4\xe3\x9f\xc67\xfd\x04\xc7\xc9\x14u\xa2\xff\xb7\xaa~\xda\xad,\xab\x9a\x04\x12\xbc\xddq3\xf7\xef\xe7\xcc6f\\\x08`rE\x05\t\xe6\xddTo\x19d\xbb\xdf\xd9\x0f\x02\x8a\xc6\xbc\xc8||\t\xcat\x01\xef\xfd\x19\x9c\xd7,L\x82/\xe9i>s\x07E/\x02j&DM\x07\xacD\xaa\xfd\x80]\xe1[\xdb\xbbP`\xda\x92s\x06S\xe1\xab>P\xaf\xf8m\x1b\x10}\xa3\xd38o\xa3\x8d=\x86\x9e\x13\x90\x80\t\xe6\xa4Y\xc9\xa6\x0e\xb7\x0f\xaaP\xf7\xf0kc\x05\xc8\xbcQ\xe0\xc0Y\xad\xb8\xef\xbb@\x1d\xc4\xcd\xf3.\xfcG\xb4T\x109\x15\xdd\xbe\xcf\x1f&\xdf\x90\xdd\x8d@<\xcc\x7f\xb1\x9ex\xc5\xfa\x8a\\\x91\xf5\xeb\xfe\x8da(f\x07\x9cwT\xe6\x10)\x04KG\x98s\xe5\xc3r9\xec\xea\x19]\xef3\x16\x98\x18I\xa2\x18hS\xfdD\x93\xee3\xf8\xc0\x93^5d\xc3\x13\x97\xa6\xb0\xb2I\xf9Qg\x1b}\x90<j\x17p\xdd\xb9\xc5\xbe->\x9f\x97@\xa8\x7f\xa0\xe3\xc2\xc6\xaa\xe0\xe3\x7fY-JWMN\xc2\x01\x18\x96\xec\xd8\xb7f\xe5\xe6E\xc5k\x03\x1eo\xc7\xb8\xdc\xe9\x855\x81\xf5Z4\xec\xfb\x17\xb94\xae\x84\xa1k\x01\xf8\xdd\xb6\xf5\x1eE\n\x9e\x88Vqh\x0e\xc7\xd6\x18\xd1\xfe\x9a\xd9\xb4\xfbL\x00\x972\xea\x03\xe2\x8eH\xdf\xd9p\xa2\x93\xf0\xaaXww\x8a\x9c\xb9\x04}\xed^:\x98\xa0\xd6#\x91\x1f\x07B\n\x00\xc8\xe5\x98\xff\xbau\x99NN\xbc\xf0[\xdd\xe9H\xee\x12Z\x9e\xe8\xde\x81m\x02X\xbe6\xc3\x8c\xc4\xfd\x9e\x0bE%%\xeaJ#\x94"\x06.\x96\x95B\x8f\xcf\xd1\xe5\xb7\x1e!\xf5\xfe&p\xb8\xddw-\xb9\x88\x95\xfe\xc6\xb0\xe91\x0e\x17;\x7f\xd9\x9d\x9du\x0b\x16\xdf\x0c\x9d2"\xd3\xb3\xb5^\xb7n\xd0)M.&9\x8cm\x175\xff\x85\x85\xe0\x00\x0em\xe2\xc0\x81\x03\x8b\x8b}6>\x9b\xec\xfd|\xc7\xfe\x9b\x87\x16\xfe u\xc5Yi\xfb")4\xe8I\x98\xd8[\xef\xf0\'l\xa8\xde\x84!\xbb\xb9{\t\x0b\xe2#{uG/uU\xc5\x1e,\xb8,\xec\\\x8dJ\xf4O@\x02\x94\xfe,\xa4\xd9\xca\xa2Z\xf6\xa2\xe1\xc9\xdd\x0c\xf9\xa6\x93\x8c\xd0\xaar\xdc\xcc\xb38\x02\xb4\x97\xa8lv$\xc7n\xd6F\xfd\x7f\x88\xf1\xcb\xb2\xb1\x93\x83\xea\xce\nk@\',/\xe4fi~\xde~&<\xe4\xf3>W\x06\xd4\xb0\xd3n\xf8\xe6\xcd>\x99DD~qV[Z\x0c\x0c\x7fy\x8a\xba\x18EU9e\x14\x84\xf5\xe4D\xe2=\'\x93l\x8f\xd4\xd3\xc0\xd4pmW\xa5\x92\x7f\x8e\xb4\xc4\xea\xb6\xec\x1e\x10\xec:\x7f\xab\xad\x86\xd0\x96\xa6Kw\xc5\x18\x1a5.\xd6u\xc6\x02\xa69\xbb|\xbd=\xd5\x14\x17\xb2\xe8_I\x8b\x00\xce$&R\x99\xd0+\xc3\xd1\xd1\xbbQ\xd7.\x9fF\xe3>\x85\xd0\\\x9e\xa7\xa3$\xb0\xd9\x04\xc9\xd5\xd3\x1e<\xfe\xa07\x8c[\xba\n\x8b\x8a\xbd@D\xe6[\xfe\x11\xaezz\xdf\x90\x14\xccn\x16\xdd\x04\x9e\x11\xdf\xc6\xaciLG\x01\x044)\xcb\xdc\x9aGQ\xab\xb3\x82\xfb\x17\xde\xb4\xaa\x02 y\xdc|`\xde\xd6\'m\xa0V1n\xe0\xab\xafl\xa5\x04\x04\xf6r\x15`$C\xfa\x13\xf9\x93NF\x14h\xb1j]\xfd\xc4\x9aU[V\xbd\xef\x12:\xd4]DY\x11\xa4(\x06\xea\xb8\xac:|\x19(\xb9\xc4\x97\x06\x90\xf5\x0fT\xee<\xb7\x07<\xcb8Rt\x10\xe1"9\x03\x9c\xbf>\xb2\xce\xb4\xf9)R\x1e\xea\x0b\x02z\xefuo\x85\x8f\xbb\x85\xaf\xdf\xc1\xa80\x0ce\xcb\xd2zV\x8aU\xbd\xce\x9a\x8dx\x9d\xe5\xefk\xcd\x18\x1f*\x84L\x14\xaf>\x99p\xab\x96\x9e\xc4cV\'\xa4\x08\xc1\'\xb4\xe1\x9e\xcd\xd1\xab\xa0\xf2Y\x91r\x86\xac4H\xce\x91\xd1Wu+\x9fUV4\xec\x1e%z\x0f7\xfb\xd4W\xc6\xe4\xa9~\xa7\x0eI\\-J\xf74=I\x1b)i\xedkHs\xc3\x88\xec\xe9n]\xb5\xc3\x06\x85\x10\xc7\xf6\xe1\xd73d\xb7\x9epe\\\x86)\xbf]\xf9\xa3\xe1\x0b\xfb\xc5\xa4\xc6\xdc\x83\xf7U\x93 \xe7<\x91\xdc\x9c\x90\xeb\xaezH\x93\xf8\x1d}\x16\xbbc\xef\xdb\x16\x1aa\xa2\x19\x92)\xc3+UX_{\xc1\xf5\x8a\xdaZ\xe9H\x8fzx.\xe6\xf1\xd6\x04m\xe1\xef%\xf9W\xe5KtWD/\x92R`^\xe1\xd0d\x06\x84\x9d:\xb6\\\xbb]L\xfeW\xe28B\xe5\x82Xt\xd8)\xcd\x86\xb5S\xa6\xe7\xd8O/\x17X\xd86\x90\xaf\xfd\x91\xb5o\x01\x8bTV\xa2\xc2\x089CW\xd5\xa9\xb8{\xa5\x992\x15=\x1d9\xc6r\x0b\xbb\x05$\xa9X\xd6*\xf7\xe2\x96\\\xc0>\x1d\x15\x7f\xba\x14\xbc0C\x11\xbeps\x9f\xf1J\xfc|\x95\x8e\x9d\'Z\x9fL}A\xe6c\xb3a\x06J\xbe\xb5\x87b\xf56>\r\x1a\x18\xa9\xa0\xa2r\xec\x95\xdd#&\xb5\xe0\x9c\xad\x9a#\xd0$\xc2\xf2?{\x13\xa8r\x94\xac`\x11\xaf\xf3\xf8\x1a\x1d8\x82\xf5\xcf<K\xa6\xa3.\x0f1\xab\xe3\xa6\xde\x1f\xd9\x8f\xc7\x8c\xecS\x96I\x08:\xb7\x11\x84\x1b\x8c\xec*<\xef\xb2\xd0F\x10T\xb9\xd3\xcbt8\xf9\x03\xf6=\xd4H\x86\x1b\x8cB^\xce\x9e\x18\xeb\x86\xb2\xd3QXm\x9bjt\xe5\xe5\x9f\x0e\x96\xdd\xf2\x8eb`A\x96\xc7\x1e\xef\x13D\xf4"\x15Z)\xf6I\xa5\xac\x1c$\x97\xd7B\xfc\xaf\x96\xefp\xbd\x9c\x16\xd3\xbe\x8eJ\xf7\xef\x86\x18\x1b\xdf \x8a\xfc\xcf5\x9ezQ[\xc9\xddoh\x1ex\xbaGB\xf4\xeca\xa6X\xdf\x9e\xaf\x90\xdbh\xc3s\n#f\xa3\xec8\xd1&B\xa1\xbc0\xd1VZt\xf1\x16J\xfb\x86m\xfb_V\xef|=\xfd\xc0\xb6V\x9c\xa0\x19\x98\x0bR\x19\xc2\xc9\xd6\x90\x1bW\x08~\x0f\xeb\xa5f\x19\xa5\x8a\x85\x13\xaf\x8b\x05\x144h&\xf3\x90]\xd1\x01\x16\x1b\x96B\xf4G;(\xe5\xbc\xde,\xa8K\x1f\xf3\x82\xb7\x95K\xc3\x1d\xde4fY\xb6v\x87\xc1s\xf8W\xa2\xd4\xf8\x12A\x08\xd8~\xb0\xbb\x1c\xbd\xf4fy\x8b9\x17pr\xaf;\r7\x95[}\xdfW\trSX\xfb\x80ri\x81\x1b\xa2\xbdL\xc2Y\xa2\x7fi\x90\x94s\x00.\xe4sM\xc2\x9f\x98\x96_\xf8-\xe2\xfa>\xfcz\x17B2\x81\x9f\xb9\xb6\xd3\xa5\xea&\xb9\xd1\x88\xb5\x0c\xd3^\xb9\xdd\x86\x15\xc5K\xaf\xf4*\xb00}M"\x8d}\xa1+\xb9\x89A\xb3W<\x90\xb2\xf2@\xf2%J\xe6\x8e\x82\x9f\xa1\xceod&\xf4\r\x81\xdb?\xa1Odtw\xc4\xf7\x8d\x89\x8eM\x86r\x03\xc8K\x12\x99\xc1\x8a\x10\x05|*\xc4H\xe23sc\x0c0\x91(f\xa5\x07vyG\xb9\xb1\xef5F\xb9\x05\xb2\xfc\x18\xdbb\xf9\xad\xf0)\x16\x94^\xdc\xc7\xf21\xe6/\xcf\x88\x03A\xe1\x02[\xf8\x83\x90\xde\x8c^\xb3\t-\x89\x04\xf6\xb7\xf4\xca\xcd\xe9\xea4;\xbe\x00\x87\xf4\xd1:\xeb\xb8\xee\xfe\x90\t\x9e=\xf6}\x0f\xdb\xec\xde\xe7\x1c\xe2\x8a\x08R\xa0\xae\xc7`\x02\x91\xc0]Z_\x8f*\x87\x90\xed\xc2\x9f\xca\xd7j\xa2c\xe3\x86\x16\tnS\xc4\x86\xe4\x0e\xc3s7\xc4\x912\xeaQ\xd26\xf1\xcf.\xdbh)\x8ee^\xac{\x05\xd2\xfdI(\xe8an\x97\xeb\xe12\xbf\xca\xf3\x1aP~\xd1\x10\xff7\x17L\xd7\x9bY\xba\x92\x19\x07+?\xe6J\xc5\xa9\x10\xb3\xea\x15DC\xa9\x9f?AT\xae\xdfI\xfan\xa0\xfe\x7f#\x08"Y\x01\xcdQ\xa0\x8f\xab\x8716\x02\xbe\x00\x86T&\xdb\x85\xb6\x94\x17\xbb\x8f\x04}Ie\x9a\x04n\x86*3z\xf5\xf4\xae\x12*\xb6\x99Z6F\xcc\xff*N\x9b\x9c\xba\xdb\xb5b\xcc#\xea\xa9\xa9\x81\xb0\x9e/]-\r\'>\xd1\x8e;9\x1b\x81\xbf(\xe7\x058\x037s\x96\xfbn\xa5}\xda\xabo\xbe\x98\x98J\xa7\x81-\xbdKb\xee\x17t\xf7\x9a\x9c\x9b}O\xda\xb9\xef\xa6b\xa2\xba\xb9\x96\x99\x96\xe0\xcd\xc77B\x90\xe6\xfd\xd2\xc95\xa2\xb6\xda\xaaV\x9f\xc0\x8e5(n\x8d\x07\xb4\xbfA"\xfc"\xdc\x9c:\xce\xb4\x85S\x91xY\xd2\xca\xd8L\x98\x8c\xb4\x9d\x93"\xf3C_\x08\xed\x86\\\xcd\x9c\x94m\xb0\xb9\xec\xfb\xe7KQ \xd9D\xfb\x1e u\x84\xd9\xc6Sp\xf0\xf7\xb9\xdeyb\xee]\x9a:9!\x0b-\xfc\xcd\'\x1fN\xb3\xd8J\xe2%H\xe2\xa3xhX.\xdd}\x9b\x95\xd9m\n\x8b\x0e\x93\x9f\x17\xb3\x9a\xa4\x102\xe7]\xc4E\x96-\x1f\xd3T\xb7\xbd\x05\x1e\xc3\xbfs-T8\xdb\\y\x84k\xa7\xc5\xdd<\xf1\xeet+\xa5X\x83\t\x0b\x128\xeey\xfb|n\xce(\x965c\x02\x86)\x92\x0f\x8a\x8d6\xa72\xfb\xc9\xbd\xd5\x03\x1eI\x99\xf1\xda\xacag>\x94\xc7I\x8bG]^\x98\xf0jG\xb2t\xcf\x92;*\x878\x8eZ\xfd:\x8e\xc4\xb9%\xe3?\'R\xa0*\xa5^\xb7\xf1\xa4\x15r\xc2@\xe7\xab\xa7\x9f\xd8CDg3\x0f\x15J\x9b\x8f\xe1F\x12\\\xc0\xa6[\xba\xab\xfe\xc2\x8a%\xa3$\x81U\x17l\x7f\xafj\x0f\x0b\x1fw\xc3\x9b\'\x8e\x7f\x95\x1a5z %\xe0\x95\x14/\x08\x0f\xa7\x1c\x84\x83\xd9\xc0(\xda\x0f\x96x\xfc\xf0\x9bi\x8e\xfa\x1a9\xdf)G\x98\xf5\xca\x8c\xb5W\x07\xa3\xc1\x95joc4\x83-\xc6\x0f\x18\xa6V\xa7%A\xf6\xddP\xd1k>\xb2\x11\xb7b\xf7\xfar\x99\x87?>\xde\xabY\xbaEt\\@\xbe\x87\xdcc\xe1`\xc2\xc5s=\x03u*\xe4\x0e\xeb4\x9e\xfe\xbb\xf9\xa7\xb1\xe0\xa2W.<\x05F\x8a2\x1d\xfe\xe6_\x1bc\xd7\xe4\xf9\xdf\xe1\x1b\n\xf7+9C\xbf\xa2\x90\x9b)\n\xce2\x18>e\xbe\x11\x99Z,\xcb\xe7\xa7\xf5\x0b.n\xdbQ\xbc\xd8\x8fx\xae\xae\xf5M\xd1\x13^g1\xb5\x87\x99\xaefZ\xe2\x8c\xa1G\xcb4\x9d\x16\x85Q\xc6\xb6\xbdi5\x98C\xd3\xac\xb7->H;\xf2\x03d\xe7\x9b\xb1\xf8\xcaE[\xeeQ3bi\x94E\xc2\x91[\'O+\xcf;\x9a!#\xd7[d\xc5+.\xcc\xccv\xd0\xa8.\xbb\xed5=\'\x84+\x16\x0e\'\x93\xfb\xfdc~\xc0JG\xcc.\rQ\xe2@Y\x10\xb44\xd0c\x0cm\x14\xb1M\xf8\x16>\xd2\x87\xed\x81\xd9E\xd3\n\xfa\xaf\xaf\x07\x07\x1b;2\xcb|\x8d\x96\x056J\xe1\xda^s\xf15#{YF\xa6a\xf3\x84H6]\xa54\x98p`v\x1b\xff~\xdd\xd8M\xac\xe9\x9b\xe9\x8c\x9e%\xf5\x05\xca\xec\x0c\x8d\xb0-gK\xba\xde\xfb\xf0=2\x83\xce\x17\xa8\x8f\x87T\xe7\x02J\x03\xee\x1e\xcd\xaa\x1f\xd56.[\x91g\xa4!\xa1\xb7\x1c\xd9\x84\x07#\x06\xc2\xa4\xe9\xa3\x80\xdbS\x15\xfc\x9f\xd4arj\xf4\x0b\x85\xd82\x92\xf6\x9e+\xac\x18\xcaq\xa8I\x0e\xba^\xfb\x18\x8c\x95\x13\x00#u^\x90\x94o\x13\xf0)I\x00\xd2\x03!\x1a\xbe\xf7\xe7\xee?\xd1\xf5\xb9\x985\xb5\x9d%TP\xb0\xa50N\xaev1\xd3\xcbV\x82\xaaz\xc3\xf1\xc5\x91\xee>\xdb\xf8\xa9`\xe8X\xed\x93p\x8cU\x8c\xdc\xb5\x1a\xde\xe8>9\x0b\xab\x10{\xcc\xe6}"\xd2t\x1b|\xe5\x8f\xa6\xee\x12H\xe4\xc3f\xb8\xf2JV4\xc6.\x90\xb2c\xbb\xed\xce\x94\xd7\xe7V\x05\xe9VL\x84-z\xc9\xf0\x9d\xbb\xfc\\w\xb1\x1fI\x05\x08A7\xdddZQM\x8a\x90\x8c1.\x1f\x14\xac\x17\xea"Z\xa2\x1e\x08.\xc4bTn\xf6[\x12\xdc[\xe4 \xc5:\xbf\x8c\xebd\xda\xb2\x7f\x80Ll\xd2\x97z\n\xd5\xeb\xcc\xa1m\xb7\xac\xea\x94\xfd\xb4\xdcH\xb18\xefq\x0468\t\xd7\x17N\xdb\x04\x9b\xa3\xb7\x8ay\xa94\x08|"\xa8*\xae\x9d\xceT\x9e\\\xeb\xcdH\xd2\xdbw\xb8\xa8y\xe7,C\xe0\xb6pDQ\xea\x8b\xc6\xdd]w\xc0\xb5!6m\xe9VEv+\x83\xb2\xa2\xad>s)\xb1\xfe\xd3\xbc6~\xfbNzg|\xd6\xd1V\xe9\xcek\xa1\t\xa5\xb1\x87\x068}\xfa\x15N\x98\x96\xe6\xb4\xb1\x8b\xbd\x9f\xb4g\xb2\x8f!\xa6\xdc\x00JF\x0b\x8a\xe4\xdf\xc6\x99\x1c\t\xd7"\x92h\xf2\xae\xbb\x9d4\xcfSB\xb5\xb1T\xc9\xb9\x98\xed\x17t(\x90\x8d\xd8;X\xf4\xf9\x8ez\xe8x\xe5gX\xf0T\xd0\xc93M\xc9\xdd:\xbe\xf8y\xddh+\x15\xe3\xee^0\x88\x9a:h\x95\x1e\xe8\xe6\xac+\n*\x03\x82P\x84\x1eO\xcf\xcd\xe6\xb6\x9e\x8a|t\xc3\x91_\x93\xe6\xc18&|\xba\xd5"\xf9m\xba\x98\xe3Rs+\xe5X\x1f5G\xbb\x8d\xae&w^K]\xc0\xb2z\x06\xcd\xf7\x8f\x96\xa8\xa0#\xf4)\x88u\xec:j\xa0\x011NR\xea,\xe4\xb7<29\xcd\xa8\xb2\xca\xe2\xb7\x12\xdc\x9f;\xd5\x93\xc3\\\xa1;u\xad\xbav\xba\x86\x86\x17\xday\xeb1\xec\x87\x02\x81J.\x88uO\xc17\xf6\xb5P^\xb8\xcc\xf17e\xae\xadV\xe6#%E\xe7BZ&\xa7\x84\xc6H\x0b\xe0\x99\xc3A\xf0\xb5\x0b~\x97\x0e\xe0r\xb5$ >1\x1dw3\x0cOH\xa2\xc5\x145\xaf\x0b\xc0S\xd9\x7fW\xe3\x04\xc4ix\xdd*\xcd\xa9\xd9\x91}\xf4#\xec{@\xcf9\xa2\x1a\xa9\xb7\xb4\xf9\x99!\xbc\x7f\xdb\x8cj\xd2@\xd9)\xf0\xdakh-\xabf\xced\xc2\x16\xe6\xfaF\x90\xb9[\xfb\xba\xd0\x08\xb2\x00jQe\x18\xb7FQ \xad\xd0RQ\xe2\x8c\x91z\xa0\x0e\xb3`\x08\xaaTp\x92\xd9\xd5\xabq#f\x85\x9f\xef\xb6\xd5s\xe0\xdf\x162\x1c\xf0/\xdc\x86s2\xbaY;\xb5\x08\xce\x05j\xce\x08V\x07\xedW\x9dL\xf7y\xe7\xb8\xb3\xedU\xf4a;P\xda\xbd\xdd\xfeY\x1a-\xf1*w\xf6\x8f/\xa3\xcf+\xd3&\xcb\xd1Pc0\x19m\x93L\x0ez\xd1\xeaP\x0b.O,\xf5\xfb\x88\xc1\xfe\xc3W\xd0\xe8\x1fViT\xa5\x91+c\xaa\xda/;\xcb`\x8d\xa1\xf5\x83\x880\xc4Q\xad\xc7\xc0\xd2\xec\xebX~\xa5\xaf\x97\xff\x18\xd1\xc8]\xd6\xc5\x0e\xec/M\xf5\x1c&1\xbc\xd1\xec\xd0Py_,\xa5\xf2\xf3{\x9c\x9c\xd4\x9d\xf5z\x89\xa5h4\xb0\xc2]\xeb\xf3\xc7l \xe7%\xb2\x93\xaf\xca\x10)\xb9\x8ej\xf3\xaa\x92\xb27D\xf2b\xfd\xe5\x0c\xe7t\xa3|\xa9\x0c[p;F\xce\xae\xb3\x10\xc9O\x95\xf9\x1a^n\x1a\x8f\xd5{U?e\xac\x90&\xd2\xa3r\xf3\xe9/9\xaf\x9d\x87\xd4[\xfa9\x8a-\x9d\x17\xb0\xf8\x83aG\x1d\x17H\xef\xe1b\xc8$\x93\xb5r\xfa\x0e\x9f~\xb7\xb8\xf5\t\xd9\xaf\x82>\x9c\xe5\xd9_}\xc1\x18\xcb*\x1b,\xf8\xd9\xe2\x81\xb5\x07\xcb\xf4]\xa4\xfa\x15\xc6\xd9s\xa3\xc9\xd950\xbe\x8a\x9b~\xdd\xd6j8}\xbf\x03\xc8\xd97\xeb\xafC\xa6\xf0\x12\xc4\xaf\\a\xfe\x06Z\xd8\n\xd7\xcf\xdch\x8aL\xbd\xbe\xd9\x1e\xd1&D\xc5J[\xcas\xd0U\x8cY\x1d\x1b\xe2\xfcr\x17\x9f\xbc\xdd\xdb\xf51\t\xedP\xdd\xcaI\x1fj\x17\xbc\xa5\x8f\xa81<\xc2\xfe\xfeU+]\x84\xe5\xde\xaf\xdf\x1c\xf0+[\x97\xed\xdcmC\xb1\x08\xf7a\xd1HT\xc4n\xee/\x155\xb0%aW\x13V\xbcT,\x93n5d\xd2\xd5\x18\xf7\xd6\xd6?6\x8a\xf9\x93X-,\xd3\xe0kp\x18\x89\xc0\xa7\xd6\xd0\x10\xfb\x8e\xca?\x01ZBB\x0f\x11@\x94s\xb1\xda\x94A\xce\x9e\xa1\xf2\xa3:\xc8F\xbe\xfe\xdb\t\x901\x83\xca\xf1\xe7O\x86+Ehh\xf1(V\xc9K]Tp\x85\x8d]9\x0c\xc0\xb2}\xfa\x80\xa1\xf2\x03[\x9f\xf3\xaa6\xde\xbf\xd4\x06\xe7\xc9\xa2\x8c\x91\xc9e\xe9P@@\xef\xb9\x0ehR\xe6\x11=n\xf5\xc2\xb3@\xed\xf4k\xcf\xf3\xd3_u#>\xbc^\x02[*\xa9\x13?P\xecU\x1a\xa26\xf3_\xfap\xcd\xb8Y)\x9c\x94\xb3\x18(6@\xbe\x90|N\xd3\x84\xb8G>\x84{#J,\xb9.\x9a\xca\xd6\x0b\xe5\xb6\xa5\xf0\x9eB\xdf"\xbe\xc2\xa2l\xa6\xebR\x94g\xe4VI\xae`a)\xe2\xc8u\x950\x9cf89\xd7>Y\xf4\n\xae/R\x1d\xbf\xc2\x1d\x87\xdf\xfd\xcf\x1e\x14\xa6\x1e\xe6a\x859\x8d\xd3#Y\xf0\x80`\xaf\xf3\x96Ox\x97\xe9\x84\x92Xx\xe0\x19\x05Y\x13\xce\xa2\xad\xf2\xab*>\x0c\x13\x87Q8\x82\x05G\xab!\xe0+\xdcx\x96A\xab\x86Z\x88\tU\xa0\xb8\x05\xb7\xacy\xcf6\xcfZ\xc9mp+\x17ph\x7f\xed\xc6\xa8\xc9\x88\xe8\xfc\xc2)\x190\x1d\xc3\xbe\xdd\xf2\xec\x14l\xb1\xe6Y\xa8-\x16e\xc7\xe8\x1fV\xd4\x96>\x1e\xb0D\xc1~\x866\xb7\x90\xff\xbc\x8drC\xdb\xc12(2\xea\xe5\x9aps\xed\xb3\xba\x17\xb4\nv}o"\xe3\xcd\x9e)^,\xdf\x04\xa7\xa99\xb7\xa5\xfb\x12\x11D\xda\xdf\xb43\x12LbG\xcd-\x00\x1fN\xe0\xf2\x89\x9a\r|\x98\xfd\\\x0ez\xfb\x8b`&\x1e\n\xdd\x83\xfa}t\x17\xb7\x95\xaeVp%g1d\x1f\xbe\xf6p?\x01\x9eY*\xce\x0c\x8d\x8f\xa4\xed\xc9U\xa0\x99\x88\xa0eV\xbd\xf5Uw\x05R\x0f\\\x9f\x8c\x15\x0e%\xc9\xa4\xa3$+\xa1\x07\xd8$r6\xfd\xa0\xf5\r8\xe0\xcd\xdbe$ZN\xfe\xd8\xf9Y:\x94}\xffZ\xcd1\xd7\xf8t.c\xaa\xfck\xdcz\xee,\xacx?\xde\x83i|\xb0\xcb\xaa\xbb\x15c\x9d-\xb0#\xafMI\xc5"\xf7\xae\xe5\x8a\xbc\x89U\xb0~\rk\xf5}\x8f\x131^#YST\x99J\x17Hhe|F\t\x1blQ\xb9\xb9\xb8\r\\\xa1U\xae\x07\xdc~\xfe\x19\xd8\x90d\xc9\xb2\xf4VN<\x91x\xb9\x0c\x85E\xfb\x80+A\xe8\xe2W\x0eG\x004-#\xace@\xc1\x9f|\xfc\x1f\xd5h\xd9\xe5\xabR\xd5\x8e\rL\x87\x90\x9d\xd9@\x95\xe49O\x81\xc3\x17\xd8\x02-\x18\xed\xce\xa0\xf5P4\x0e\xa6\xec\xa8\xbaQsH\x15\xf81\xfd\x17\xd3=\xc3Y[\xb5 \xd5y\xc7\xdeCK\xab\xeb\x9f\xba\x05<vY\xa6\x93\x04,D\xd6\x8eH\xd4\x85\xf83,a\xfd\x136;W\xe6\xbbI?\x0e\x02iZ\xf8&C\x1d1`\x17P\xc3l\x8d\xa6o\x19\n\xb6k\x8c\xc5\xe7)\xc5\xc2\x98\xdcx_\xfa\x81\xc4!5\x8e?\x9d@\xef\xd5\xb3\xec\x03\x99sAe\x07\xbbyt\x81\x14\xbco\x0c\xd4\xeb\xa0\\$\xf0\x90\xc0\xe6\x1d\x89\xad\x9b\xe9a>J\x8f\\\xd6s\x1b%\x8f\xabu>\xba\xe9N0\x19\x0b9G^\xb0\x83\x02hZ\xf3\xb9\xd6e\xc9\xa8g#\xc7C\x86\xc2"BOMD\xf3\x013\xbc\x11\xfd\xfc\x1c\xfd\xb1\xbe\xbb\xdb\x8d\x0f\x0c\xed\n\x14\xb7R\xc7\xe2\xb6>~\x11\xc8\xdc"x\x0b\xa6\xeb\xfb\x1fh\x07\xc3j|\x1b@\x87\xe9\x12\\=w\xa4\xd1\x7f\x82\xda\xef\x05&O\x9a\xe9\rI\n\x17Og\x8e\xc0\xben\xd2/)Q=N%n\xa6\xb4W\x01d\xfb,s\xf4\xf5\x11\xa0\x92\x93k{?\x91\x1e\xd5\x1cW\xa3b_\xa0\n\xa1\x16j\x8c\x18\xe5\xb3Z!l5\x16+\xcer\x0b!\xa0\xc5\x8d~\xcf?\x99\xd5\xb1\xcc\xb4n\xed\xfb\xa6\x16\x96\x98\x02\xcc\x85@\x03\x1a\x9bT\xda\xc3b)\x0fQUKn\xf5\xc4\xd7\xc5\xbe\xed\xa3\xd0\x0c\x98^s(\x1d\x90\x0f#\x14\x13\xae!\x16.;\xaf\xc5\x9f\x1cE\xb8\xd9\xc9\xdf\xc2\xd7\xdcZ\xcd\x10\x9c\x05+$)\x7f&u[\x88\xe3\xd4\xfdZ\xa7\xf3\x80\xbe\x89S=\xf7\x84l\xc6\xd3\nV\x82\\\xc1Mi0\xe8\x13t\xa4&\r\xfb\xa3\xfc\xa1\xe4(6\xc5[8\x9aV\x8f41\x19\xf8#\x84I\x8aMyJN2\xc2\xd6.\x11jx\x02\xe5H\xceL\r\x0b\\\xe6\x0c,9{J\x06\x0c\x1f\x91D,\r\xf4\xbbb\xa4\xbf\xdb\x17\x84z\x88\xce\x96\xe1\xfa\xd2h\xa5\x89\x9a\x03P0\xcf\x11\xaa5\x90t\x8e2_\xca\xaa\x1a\xc7"\xcc\x1b\x00\x0c\x05\xc8\xc4\x95\xeeX\x9d\\\xb9\xd2v\xf9\x0e\xdf8m\x8e\xd9\x88\x87\xfb6\xec\x95\xd1\xbb\n^Y\x95v.=\x8a\xf5\xe9?4\xa3\xceB]\xa8R\xb9\xbd\x0c\xceV\x93\xc3\x02\x81f3\xf3\x00C\xd6P&\x9a\x89\xb0\xec\x01\x9e\xd2\n\xfeAI\xfaI\xb8t\x10\xea\xf9-Vw\x0c\xdd\x87\xa99p\x8fZ\x00\x93)y\x13\xf3\xc9\x8d-J[\xcd\xf8\x8dz\x88O:b\r\xb8L\x04Yj\xb5\xd3\xbc\xbb\xeb\xdd\xcd\xb6\\\x88IF\xec\xe5d\x92J\xea\x06\xca3\xfeH\r\xa9?\x8c\x19G\xf7\x95\x1d\x91)\x02\x98q\xb1\xc0M\xca/\xb2\\\x15n\x9e[\x19\x13\xc5\r\x82z\x1d\x07%\xe1\xb3f-P\xefi\x8fJ\xa7\xb1u\xde\x90\xb4s6Lo9\xe1E\xa1Q\x14\x0e`\xf2\xab{\x89W\x89\x93sh\xa7\xa2\x9aZ\xeb\x1f\xb5^\xef\x89\xac\nA\x04\x9c\x12\xb4\x96\xf1\xf5br\xfb/$g\xe1+&\xc3U\x82\xa3\x94\xfb\xdcA\x90^\xb2\x08}\x10\x9fv\x9b\xa4A\xaf\x1ea YD\xf3h7\x06\xd3\xee\x90%\x83\xdb4\xc3\xadv=\xd6\xc78\xc0\xec\xb7sX\x13FR\xee\xd5\xc8\xe0\xc5nv\x90t\xbf\x82\x93J\xe5\xa0\xa6\xee!|\xc6\x00\x9c/q\x02\x01\xc1\xf5\xb8\x83\x9f\t\xc7 \x9d\xc4w\x8fJ.v\xed\xc7\xf4\xccfpr~.x\xa3\xc7yl*i7\xa3o\x81\x80\xear\x12\x19I\x1cp\xf2\x9fS\x08\x98\xce\xf1&w/\xeb\xbc\xd5\\0T\'\xafa\x0bx\xfc,C\xa2\xe2\x98\x9f\xb4\xbc\x0e\xa2\xa9\xc5NS\xa4n#\x17\rz?F\x81#\x9d\xf7\xe3\xf9\x1c\xbc\xf8\'\x0e\xda\x80~\xf3Z\x1f\x04\xe4\xf4\xddm\xa6\xd7\xa0e\xd7\xa2\xfbm\x82q\x1d\xca\xe5\x99\xdf\x92=\xeb?\xd9r\xcf\xc5\xe5\xca\xb1\xdb{]\x1a\xf0\xe9\xe1B\x03\x8dU\x7f\r\xf2\xc4\xa2\xa3\xfb\x17\xed\xbe`\xfc\xfc\xb7J\xee\xa0\xadv6\x9d\xafv\xbeI\x8d\'\x9d\x8f\x86)\x86X\xb6\xfda\xc3\xb4\xdb&>\xcd\xbf\xab!\x1fy\x922@\x8e$\x86\x10Ev\x8aimk\x1d\r\xe6E+\xb6u\xe6\x18\xc5\xedh\x83>&\xa3\x15\xffd\xeb(N7\x14c\x92O\xcc,\x0c~\xcel$\x0c\xbd\x1e\x15"*\xfeJ\xee\xf4a\x1dW\x93e\xee\xa6\x14\xbeZ2\xd3\xccfa^\x9f`\x96T\xe9-\xadc\x1f\x19Q\x15UG"\x10\xfc.\xce-\xea\xa2\xbd)\xbe7\xa3"\tm/h<\x122\x92f\x13\x9f\x83\x9f\x15xK\xbd\xf2\xe0D\xcd\x0c\n\xa1\x83\xff\x8b\xb9"\x9c(Hi22\xdc\x00')))
except KeyboardInterrupt:
	exit()