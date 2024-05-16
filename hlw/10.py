# 项目：hook_hlw.py
# 时间：2024-05-16 15:47:33
# 运行环境：python3.10.x
import sys
PYTHON_VERSION = ".".join(str(i) for i in sys.version_info[:2])
if PYTHON_VERSION != "3.10":
  print(f"【你的青龙python版本为{PYTHON_VERSION},请使用python3.10.x运行此脚本】")
  exit()
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(zlib.decompress(b'x\x9c\xad{Y\x92\xe3<\x92f\xfeU\x7fu\xd7\xd4M\xca\xc2\xda\x82\xa4DE\xc8lz\xac\t\xee\x94H\x05)q}\x19\xe3"\x91\x147EhaP\xaf}\x91\xae\xc79\xc4\\$o0W\xe8\xa7v\x00\x8c5#+\xa7\xdb:\xcd(\x04I\x00\x04\x1c\xee\x9f\x7f\xee@\xa6\xdf>\xfd\xfb\x07\xb8\xfe\x05\xae\xa3\x06?\xd9\xb7\xec\xb7\xfa[D\xcb\xdf\xa2\xdfH\xf9\x87\xe8\x0f\xa4\xfcc\xf4GR\xfe\x1e\xfdN\xca?E\x7f\xda\xfe\xc3\xf6\xdb\xbf\xfd\xe3\xf6\xf7\x7f\xfbs\xf6\x87\xbf\xfd\xf6\xb7\xdf\xfe\xf5\xb7\xdf\xe0\xcd\xfa\xdb_\xff\xf8\xffp\xdf\xd6\xf1\xff\xb2\xdf\xbe\x85\xbd\xf0\xd5\xbf%\xfe\xb1\xf1\x8ff\xfa\xf8\x8fH@\xb1\xa0\xda(\x12\x8c\xa3\xe0uP*\x95\xd0\xf4\xa2\x9f\x1b\x95\xe0\xdbb"X\xb1\xc0\xd1\xf7H\xe9\xe4\xf1\xbd\xe2\xe7\xde\xf8>\x8aQ\x83\xdf[G\xc41\x9a\x9f\xa7\x88\xf6\xe7\x1cE\x951\xfc\xbcB/\xfd\x8bu\xb7\xc0\xed\x91\xdf/\x13\xfb9\x96T\xc6\xf2s\x06\xbfW#a+\x0bJ\xb7\x8a\x84\xa2\x12}\x1b\xea\x9dS\xf8\xae\x19\tl%5\xf6\xb2\x15\xacJ\xe2l;BJ%\xf2\xbd\x14!\xa3\x929\xdb\x1d\xeby\x11\x8a*\x85\xa3\xf5T\xd5\x8e\xde\xea\x1d*\x95\xb3\xd3\xb1^\x16!\xbe\xd2\xc6z\xba\xd1\xeb~>\xd7\xe0\xfbE$.d(\xcb\xbc7bYu\x9dH\xb4\x9e\x84vaD\xa2\x13\xcb\x8dku\xc8\xaa\x0c\xdf]Gb\\\x08l\xe7FbV-t[\x88\x1c\xafVt\x139\x82(\x81\xfc\xfc\xc8\x1er\x18\xc7!\x12\x1fsUu\xfd\xceV\x0b!\x97A\xce\xc6\x06\xfa\x17\xdd^8,&\xae\x89`\t\xc4\xc6\x1a\x12n:\xd3%\xb3\xd7\xc5\xeeb^\x85|%2\x83Y\n\x8fp\x9f/\xf2\xc39\n\xd2\xdc\xf1yn!\xee\xba\xbd\x1e\xd4\xfb;\xe1\xc4\'\xe2\x03?+\x97|\xf2\xf80\x8b\x172\x7f\xf7\xd8\x18Cu\'\xe6O\xd5y\xf6\xd0v\xba\xd6=\xdd\xed\xea\xf2\xee\xb6\xad\x17\xfb\xea\xdc\xdd\x1d\xda\xe8\xae9\xf2A\xdbL\xf7u\xb9\xa8\x8e\xfc\xb2\x14\xf8\xb0\xd4\xa0\\\xf1\x87\x01\xee\x1fg\xfca\x9b\xf3\xa1\x7f]\xae\xca\xcba\xbb\xbe\xebn\xb6y\x0ee\xb1\xdd\xba\x8f\xab\xf5l\x7f\xf6O\x87\xf3\x9a\xef\xe0\xef\xc3*f\xf3\xf5\x15\x7f\xe7\xd0\xe8Aw\x98\xc2w\xf4KwI\x98\xc1Z\xf9\xfd\xfe&\x0eNg_-\xb6\xbe\xde\xad\x9a\xe8\xb0\x1a\xfb\xb3\xbb\xc5\xa2\x94\x9a\xd3\xf2R\x97\x8f\xfb\xba\x88aN3\xf3\xc8\xc7k\x0b\xc6\xc3\xf1\xc9\xec\xcc/o\n\xbek6|2\x08wwC,\xe6\xdd\xfe\xfd\x9cW\xe5\xfd\x85?\xc4\xfdLW]\x18L>[\xaeOK\xae\x16\xb3\xbd\xb3\xd8\xec3\xdeo\x94s\xc8\xcd5\xfb\x8bvP\x97\x85y*\xfcr\x08\xf9h\x85\x96\\V\'\xaa#\xaf\xe5\xe7\xd0\x0c`\x98j-9\xc2\x17\xdf\x9b53\xfe\xa9\xbc\xf0\xcb\xc6&\xdfc\x15\xe4\xb6\xd6z\xcdEl\xac(\xbd\xe7vL\xd4\xff\xe4{\xfc\xd9\x9e%g\x97|oR\x9c\xcd\xa0\xd8\xc4m\xa6zU\x11\xad]\xcb\xff\xb2]\xa8\xb23\xbd|\xe4\xc3\xed\x8cO\xd4\xe7%cMV\x8a\xd7\xa6A]\xac\xe5\x9c\xdd\xf8\x077\xb5\xbf\x18\'\x8c\x8f\xcc/\xf2U>\xbaY-\xaf\xf5\xd4\xdax\x86\xeb\x19\xd7\x8cI9{c,\xc2\xaf\xe4\x82\xbf\x05\xed\xf08\xc9\xfc\xae\x85\x9d*\xf5\xd4\xe5@\xdd\xaa|\xd8\xb6\x05\x17}\xf1=2\xaf\xf8\xe6\x8e\x9fm/\xb0~\xearb\xac-\xafv<\x8e\x85\xaf\xe9\xbd\xe3{\x93\x8c\xaey\xbd\x9fN\x0e\x87n\xdf^\x1e7\x97\x8bq\xe82\xcd\xe9\xd3kwYN\xecs\xe2\xbb\x97\xac).\tw\xdae\xdc\xfc\x92\x08\xdd\xa3\xbe\xf2\x1f\x9aU\xa3\xed\xfbC\xbd\xd5\xd0%m\xed<V\xe7\x97\x98\x9dw\x89\x96\xce\r\xf6\xb8\xd0E!\xd7\xb5\xb1\xa4W\x994\xca)Z\xeb3]\\\xd6\x07}\xd7\x1cgy\xb9\x14\xba\xfc\xad\x8e\x11n\x14G\x0f\x18\xeba\xc3\x9c\x0c\x07\xd7=\xc7\xfeqU\xa2z\x15K\xdd\xaad\x9e\xb6\xdb\xb8\xd0\x9cK\xccyg\xbd\xec?\xf4\xef0\xcf\x91\xab\xcc\xa5\r3_\xae]\xb7\\\x95\xcb\xee\xb4\x0c\x9az\x1aT\x17c_WS\xadm:\x87\x81\xb9\xd4I\xa9\x1f\xc5Rx\xfbvu\xd26r\xb6\xb3\x99\xf9\xc3\x9a\x01\xe8\xd8w\xe5g\xdd\xe2\xf9G9S\xe7O\x91?\xfd<n}\xa3(\xda\xc7q\x97\xfa\xe39\x0e\x8amsW\xffb\xdc~UH.\xfba\xdc\x87<\t\xba.\xbc\xd6\xc5\xddS}L\xfe\xde\xb8\xb3\xc8\xf5\xd0\x87q\x7f\xd6\xed\xbf3ns\xa3X\xd2\xc7q\xaf\xf9j\x85\xc7\xed{\xc5\xd9\xdf\xed\xcf\x7fg\xdc\xee\xb3\xe3\x7f\x94\xf7\xe11\xb9\xedN\xb3\xdb\xc3\x99\xdf\xd4Ow\x97\xf7\xe3\x1eu\x82\x01\x7f\xc3\xb4\xe2\xb9"\x8eoSV\x88\xcb\x8b*\x0c\x9c:Sk\xd0\x0fr\xcf\xa6\xcds\x1f\x06\xc6\x15\xeeE.\x8f\xce\xc9\xc49Dm\x0b>\xcd\xba$>{I\x1a\x02\xd5\xef\xff\xa9\xf8\x87<\x94M\xfc\xd7\xd5\'\xfe\xd4\x16:\xec\x1bc\x19u\xc2\xa2\x104\x06\xed\x045\xc7>\xb2\xb3\xe19w\x14\xd3\xf2p/\xc4\x02\xf8\xc2uAK\xbf\x10\x02F\xcc\x04\xeb^\xe8L\x10.\x94\\\'\xefl\x87\x11&\xbd\x90\xf7\xca#\xd2\x18e\'\x889\nz(\x9d~\x01\xbe\xb2\xb3\x8d\xb9\xa0\xf5\x02\xf6%\x88\xe1g\x86_0\x99\x86\xae\xd8\x1e\xb3I6Y\x02\xdc&\xaawM|\xefq\xd9X\xe7\xe5$+b\xdf\x81\xf9(\x87\xa4\xe4\xfbX\x93b\xa4Z\x97H\xf5\x062#\x0b\xfc\xba\xaa0\xa1\xd7)\x89\xe6\xc1\xf3z&M\xdcI\xa4\x99\xe7tRq\xd6\x15J\xae\xb8\xa4"\xb8\xd2\xbc\x18\xa2@a\xa3\xc0b\xd2y\'E\x9c\xc7p\xb9\xf3\x98r\xf3s\x9a\xeb\xd0\x99\x14\x8b*\xd4\x9d8\xe7\xd0gk.\xcf\xa0>:\x86\xbeU/\xec(\x16\xfd\xfa\x9c55\x13y\xde\x90\x80WM\xebn\x994\xde\x04|\x1c\x93\xb6\xb5\x07\xeb\x11\x8b-*\xd2\xd6\xaa#e\x0e\xebs\x85\xb1\x92\xfe\xa0\xdf\xf9\x11\x9eu\xc9\xc4b\x1em4H9|\xee\xa1[\xb8ZurZ\xef\x1ar\n\x13e\xdd\x03\x1e\xd3\x06\xfa\\\x83\xdf\x8ca\xbd\xbd\xc08\x9a\x94\xf3\x10\xea#\xe5\xf2Jp\x04$\n\xb2*\xd8\x1d\x92\x05Y\x16\x02\x9d\xbc\xe3r\xf99\xb31y\x92\xaas$a\x9b\xae\xeb0\xa9\xdb)\x1f\xcbm6]I\xfas\xd4\xe8L$\xe5\x9c)9u$9\x95U\x025\xc9\xeb}\xac*g\x98\xcbq\xedob\x91\xb3\xba\xd0\xe7\xcf\x91\xff\xbc\xa2r\xf0\x8aTC\x87\x08\xe6l\xb6.\x19\xceg\xbb\xf7\x0bc\xb2\x95\xc2g\x933\x8a\x95\xea\x15V#\xf7\xa6d\x14\xe1f\x1f\x0b\x1b\x8b\x95p#\xb0\xf1\xd3v\x9bT+l\xef\xfe&\xf7\xbau6\xc9Yk#L\xa3\x8d\tc\x8b\xea\xd5\xc6\xe4\xacF\x9f\xc2\\\xd8q.\xc4\xce\xcb\xc5\xd3h\xe7\n\x99\x8b\xb5\xd7\x19sc\xf3\xe1>e\xcc\xbdy\r\xaf\x15\x1ff\xc0t\xc6\xf1}\xf6\tt|\xd5\xd5j\x94\xc2\xda\x98\xacu\xad\xae\xa6\xef\x0e\xe6>\x81\xf1e\xef\xc6\x87\xedz}\xdf\xe0\xf1A\x7f+m\x9c\xef\'\x9fM\xfaS\xb1\x0c\x8d\xda\xe2\\.\x92\xc2>\xf4\xcd\x1e\x9aA\x7f\xf5\xd8_s\xb8\xdc\x94\x93\xa7\x1b2\xdf\xcb\x99\xc5\xf3-\xeah\x83\xf6\xd1&\xbf\x86\xbe\xce\x84{\x9d\x8b\xf6\xf5~a\x171\x92\x9fM\x97\xb1\xa0$8\x0b%\xc1\xad\x18)\x07\xddf\xf1\xf3\xc2t]\xf2\xdc\xf4\xc9\xf3\xc2\xf4dh\xa7\xd4\xa6\xeb\x15\xfb/Y\xb3\xa0\xbfX\xbc\x90N\xb0<Q\r\\\x15\x11\xeeL\xb8\xef\x02sW\t8p\x85@\x8d\xfc\xdc\x01\x8e\x8b\x89\x1f\xf4\xef\xdbZ$\x94\xf8=p\xdc\xba\x020\x80\xf7\x19\x80\x8dm\xe2\xf7\xa2j[\x910\xc3\xef\x8dH\x98W2i\x7f\xa8d\xdf^\x93\xf7\xe0\xb1#\xb4\xc6\xef\xcd\x08y\x95B\xda\xb3\x98\xeb\x86\xf8=pc\xe0\xba\x8f\xf8\xfdC\x84N\x95\x86\xdb\x17\xa8\xd2<SX8w0/\x07\xb9\xcci/|\x8e\x07\xfa\x97H\x00\x111\xa7s2\xc7{\xc0+\xa4\xf4P*\xf7\xc2N\x80\x18\xa0\xa8\xa0\x04(\x0bz\xb1\xc3\xf7\x1c\xe0\x9cm\xe0\xf7\xd2NX\xe40\x7f\x88\t\xc4Bh{\xa8\xe2\xdc\x0b\x8f\x82\x18\t\x10\x1b,d\x11\xb7Cc;\x88\x11^\xda\xa9c;\xed\xad]6\xb6+^\xdb\x89\x1am\x07\xb1\xc0K;cl\xb7xkw\x18\xdb\x9d\xde\xdaMh;I}m\x87c\x08\\Zc\xfb\x15\xd4{\x94bZ_\xf2\xed\x07R6\xb6MJ\xcevp)kc\t\xdf\xc78+Ww\x07".\xc0J\xc2/\xb2n\xe9\xcb\xcf\xee\xfa\xd5/\x05\xb1\xc8\x10\x9dz\xf5\x91\\~Z\x02Wx\xf3\xd7\xd0\x06x\xa6\xe3\xb0\xef\xda\xb0D/\xdf\xb7\xd1|O\xb1\xdf\xb7\xd9\xc8\xcf\x1b\xfbC\x1b\xa2\xab\xef\xda\xf0\x13\xe0G,`t\x9d\xd6s\xea\x07O\x9d\tv\xd2g\x81\xd5E\x81\xb1\xcb\xfc\xba\nm\x88\xc5\x04d%@\xc3\x80R\x16\xcb\xab{6E\xa1\xdb\xa8\x80\xc9A~\xa7\xcb\xca9\xd2\x8cK\xec\xdb\xb9\xb91\xe1\x1eb\x11I\x1e\xd6W\xf9\xd9v\xcd\xdcn=hg_<\xf9\xe4\x98\xeb)\xd8\xbd05\x81\xf6\x9b\x920\xac\x064\xc9\xca*\xb7\x03\xd4\x83\xef\t"\xdfX\xc6\x81}\x01\x9c\x98,\xf7&\xa7\x8b\xc5r\xad8\xd6F\xec\xf3D\xad\x9f\xa25\xd2"\xdfzJ\x86*\xf7\x1aoH\xb9\xfa\x92\x94\xf7\xccr/\xe46W@\\\xc4\xd6K\xf8\xae5L{x\x06\xe3\x84qs\x06|\xdf\xcd]Ni\xc0g\x1f`\xfcWx\x7f\xb5J\x04\x147S\xec\xaa\x96\x97W\x9d\xb36r\xbe\xf1\xeb}\xda\xcc-\xf0S\xd7\xc8\xe7\xdb(\xd0/+\x11\xf7e\x0fK\xc0=k\x0f\x1eW\xcb\x87\x95$\xf4f%\xb3+\x11\xc6\xc1y\x12`8\xb3\xe4\x94!\xd9\x84\x8c\xaed5 \x19\xf8L\xb4\x8a\x02\xc7\xdd\x06\xa8^\xb2\x99\xe1TU\xbe\x01\xac\x8f&^\x11q\xee\x05\xf8Nn\xbb\x86\xf1\xd2\xee&?x)\xe7\rKWi\xe1\xdb\x8c_\xc27\xa4pb\xaaQiJ&\xbb\x92\x9c&lB\xc6R\xc1w4\xfa\xb3y\x8dj\x90\x13\x13\xedm\xde\xf2\xba\xdcTm\xce\xf2\xc3\x01\xde\x97\xd1\xc6(\xc3\xabRG\xaa\x0b\xf8l\xed#\xdf+W\x9b\xa8\x8e\xf6\xe9s\xd8\x183\xb5y\xf3\xfd\xd1$=\xc7\x9awH\x03\x0f\xe2\x1f\x18w#\xe38\xe8\xb4p\x96\x80C\xf5\x19\xfc\xfd4-\xa6\xd8\xce\x07\x91\xf8C}Gl\xbf$\x8cf \x1eP\xd3K\xfa\x8cp\x9b\xc1\xa0\xf5j\xfa,\xa4\xcfz\xf2\xac\xa3\xfe\xd2`\xc1g\x88\xb6{\x89\x85\xdaZ\x02\x17\xd07\xac\xe5B\xc9\xc4\xe0\xf7\x16\xf6C\x8c4\x0bb,\xf0\x11~\rxi=\xa59\x1d\x03\xf1\xdf\x9a\xfe@\xfb)v\x01W\x03\x93u\xa0\xcc\t\xaf"\xdf\x16:$b\x7fmO\x91\xf4e\x19b\xff\xad\xe2\x12\xe5\xf2B\x08:\xcb\x93\x95\xcdz\xe0\xdf\xf5g\x8a\x9f\xd0O|\xfd\x199\x9c9r\xb8\x0cs6\x80\xd3\x0e\xb0\x1cs\xb9\xa6G\x15\xc6\x9a8_\'\x10\xbfK\x18;Pt\x84x\x1e\xb0\x0e\xca\xd6\xdeJ\x82\x8d\xe3{\xb4\x11\xc4J\xd9@\xf4m\xb8\xf9\xccp\x99\x99\xe1Y,\xc2\xb2\x12%\x1c\x877\xe5r\xc7\x12\xdc]\xad\x84\xea\xc1%<r:\x15\x1d\x1c\xe3.\xec$F\x01\x1ab\xcc\x83r\x99\xf0(\x81\xe3/\xd9\xbc\xd3\x81\xfb\x0cQ\xeb\x1c\x80\xcf\r\x0b*\xb3-n\xbb\xb0\x8d\xc1\xa4\xfcMJ\x02\xab\xfdZ\xae\xd61\xe1\x00_\xf1\xfa\xf5:E\xfe\xa0\xd3G\x19\xe1w`q\xbf\xf0\r\x84%\x12\xdf\x00\xf3T\x15\x0c\xd3\x91\xa0\x07\xc0Aq\xde\xa7\x12t\x17\xdc\x98\x00\xf7\x0c`\xaa\x81\xe5 o\xce\x15i\xbb\xcd\xed\xc7E\xd9=\xcev\xd7\xdb\xdb\xdb9\x1d\x9bXI)\xf1\xb4\xe0\xbf4\xd4%\x1c_\x07\x1c\xcf&\xbe\x01\xf8\xd5Y\xb1ZW\xa0\xab\xe7\xd7g\xad\xbe"\xe3x\x99_O\xe6\xec\x90z\xde\xbc\x87\x98\xf0\x0c\xe59\xf3\xd9\x12\xb0\xee\x96\xce\x95\xd0\xb9\x14\xd0\x04m\x8b\xc8\xb5=k\xb9l\x8a\x03\xf4\xbbK\x81O\x02O\xdb%\xadw\n\x01{B*\x97w\xff\xc8=\x19?\xa1O#o\xc4k/,\xb03\x04\xd7\xfe\xb2\xe6\x8b\nAl\x01\xdc\xfe\x9e\xac\x19\n\xac#\xd8h\xffnm4\xc0\x82=\xcc\xb1J\'_\xceC\x811\x1d\xc3\xa0\x91\xdf\xad\x11H\xb3[\x8ckT\x01\x87\x840\xe9\x07\x1d&\xf5\x91\xfd\xa3\x0ew\xd8y\xab\x1d\xf8\xc1U\x81\xd7\x88\x96\xb6\x1c\xe7\x10oL\xf0\x1a-rL\x19 \xde`\xd0L\x00\x10X\xe1x\xc4\xe8l\x98\x8f\xa6\xcf\xa9n=a\xde}\n\xfd\x07\xac\x87u6\xd1OT\x9f\xa2:ip\xec\x10\xc4\x88+\n\xf09\xc7\xd8\x07|i\x81\xefnt\xd6:\x01\xcfQ\xeb\x16\xc7\x07P\xb7\x0c\x03\xab\xb6\xf6\xc0\x87}\xc0e\x15\xe3\xd2\xbc\x02\xdf\tu\xb0L\x1c\xc0\x07\xe7ENr\xd8\xcc\xabm\xd6\xe9\xb1\xca\x16!;\xbf\x84\xcdS,\x06\xd6!\xe2\xf8"\xd3<\x88#\xbe\x94\x9f\r\xbc\xff\x18N\xb0\x0c\x1d\xd0#\x88\xdf8\xef\x9a\xe9)\x91\t"P\xd2a\xae\xbf\x02\x99z\xa3L\xf7\xa1\xff\xbc\xcf@\xae\x19\xe8\xc3\xcbxC\xaa3\xef\xfe\xa5\xaf\xca@\xf5\xc0ZS=\x00\x8c\x00\xcaG\xb0\x01\xf8\xcd\x1bF\xa8\x18#@?V\xa4l\xedb\x8e4\x88\xffp|\xa7vr\x87\xe3=\xad\x1fK[\x8d\xf3-^\x0f\x88\xeb\xfc\x1c\xa7\x1fwv\xc4\x88\xb1\xb0\xd8\t1^\x8f%Y\x0f\xb0\x95\xcd\t\xc6\xdfv\xa2\x98w\x07\t\xf4%\x03\x1f\x0bz>\x90d\xaef\x10b\x9aV\x84\xbf\rK\x82\xe1\x06\xb5\xdb\x8a\xd8\xf0\xe0\xd0g*}F\xe42\xaci[\x83\xaeu\xf6\xb2\x06*`\x0c\x03\xf6T\x01n\x8c\xb1\x97\x83e\x14\x8b\x10s\x11n\xc1\xce\xaf\xb1\x9f\x9d\xd3\xeaH\xfa\xd9\x90~\xbe\\\x97\xcd\x87u\x99\xbc[G\x92\x9cFW\n\xc2:RsY\xc7x\xbe-\x8a\xd1N\xad"Q-6\x01_\x0cvM\xbe\x07}\xc0x\xbc\xfd\xe7`\x9c\x1a\x05\x8e\xf1G\xacb\xc8\x9c\x19l\xa7\x9d-b\xbe\x07\xa5\x02\xeb\xd0\x0bd\x1d`\xbdv8\xfe\x9e\x8cq\xb5\xd6K\xe4}c\xc3s\x0f\xaf\x93\x02\x98v\x8f\xda^&XO\xf8\xad\x9f\x8a\x1a\xa3\xed\x84\x0c\xaf\x87\n\x18\x1f\x19\xbe|\xd4E\xaf\x82\xab\x84+\x82K_\x95\x9e\x05\xd7F\x973\xcb\xd3@/\t\x17\xaa\xf70\xf6C\xc2M/qk]\x92\xb6[\x12\xfd\x1e\xd8k\xac\xca\x83\xb5\x89fr\x83c\xf6\x82\x8d!\xae\x06\xdb\xea\xc0\x07\x14K\x9c\x7fXW\xfa6\x7f\x96\x00;\x18\xcc#\x96\x9e\xc3\xa7\xaa7\x93\x95\xfc\xb4\x96Yd\x0f\xecf\xedf+\xdbs<\xb7\x82\xe7\xde\xebsd3\x96\xe2\xb2\xe6i\xcdx\xd1\xb6@\xe1\xd2-,\xe0p\'\xdb}\xd66\xaca@\xcccms\xf6\xf5\xb9#\xd7\x9a\xe3Y\xee6?\xbd=\xc3\xf2\x0f\xf4\x03\x91k\x89\xd7V8\xa0\x89\x8eF\x1c`3\xd5:\'\x93l\xb0\x88m\x18\x1b\xaa_\x0c\xd5C\xaa\x17OT\xbf\n\xaa_\x9aAA\xb9\x96\xa9\x0e\x12?e\xaci\xbb\x9e\xeajNtG\x8b!\xfe\xc5\xf9\x89\x9f`\xa6\x19\x12.\xea\xec^\xeaU\xa4/3\xc6u)/\xe8\x10\xc9\x1e\xd96\x942\x94:B\x02.\x93)\x12\x0e +\x1c\x17\x1d\xcf\x9f\xfb\t{\xf3\x93\x86\x11\xe7\xa8\xbdb\xc0\x83\xb5\xc0\x7fG\x822\x87XH\xdc\xd9N%Lz\x14c\x1d\n\xb0\x8e\xa1{\xacS\x84G\xb4\xbdB\xf2\xff\x13\x06b\x1e\xe3\x1e\xeb\xd2\x03\xd6M\x9c\xe3\xc1\xba\x15\xf4\x12\x8e\xb5\xa0\x84\xd8\xd0\xb7\xa0\x1e\xe8\xd86\x07\xdeAs;\x15?[\x0c\xf3\x06x\xec9\x13Y\xc0b\x1e\xf8&\xf0JN\xe9\xe3\xf5|\x0f\xdc\x9e\xc1<9-\xe7\xcf\x19p\x83\xadk\xf0k\xdf\xbe\xd0\x1c\x1c\xc4~8g:q\x80\xfb)}*\xd7\xd5M\xce\x87K_\xd9\x87\x80\x8f\xe9\xc0\xd28\xe1\x11|WN\xecg\xf0\xf0\xea,*5\xad)\xcf\x13i\xbc\xa3D\x9awJ5k@t\x9d\xc3\xf7\xfa j:a\x0b~\x1e\xe1\xfc\xc6.\x86\xd8\x1d\x054\x8f\xf7\xb2\xce.\xd5\x05\x8a?5\xbe\x03n3\x01\xbf\xfe\xf5\xdaZ8\x7f\x13L\xbc+\x8e[\xc0\x16\x9adF\xf2JW\xc2\x1d\x04\x1b\xaf\xa3.86\xc6t_\xb0s\xc0\rc\xc4\x8d\xac\xcep\xce\x08d\x84\xb9_\xd4\xcc\x7f\x88{)^\xa4oxQ\xa7T\xafA\xd6\xd6\xfa\xffK\xd6=\xd49\xe1<!\xb6i\xe0\xd9E\xd2\xf0u"+\xfbL\xadq\xbe\x89O\xeb\x9c\xce\xb1\xa9\xab\xb4\xa6\xb2\xf5\xa9\xae\'\x1f\xec\xc1\xea\x16\xaf\xed\x95\xf9\x01b\xaf\xec\xbd}\xfc(74\x04\x94\xdb}%7\x97\xc8\xed-\xef\xb4\x0b}\x8b\x89\x83\xe8\x90i\r\xb1\xc3\xb4\xc1\xbfh\xa6\x8e\xba\xff\xf3\xfa\xf5\x8f8k\x7f\x94\xdb=C\xec\x15\xfc\x1f\x03\xf8h`\xddG$_\xc0\x03\xbe\xda\xd1=\xe0\xaf\x80\xf1\x14\xfc\x1f\xf0\x0f\xd0\xfdG\x19p\xd8\x9a\xa3I\x0f\x1c:\xab\x10\x0c:\x13\xacG\x8c\xcbq\x0e\xf5P\n\xf5\xa3{\xc4\xd9\xca\x1e\xeaA\xfc\x0f\x01\x06\xd8\x8eb\x82\xbc\xa2\xd5\xb6d.Qk\x00~\xda\xa7\xc4W\xce\xa1\x9f\xe1\xb5(R\xb5\xba\x80\x8f\xb9\x82\xce\x9fp\x8c\x97B\xfc\x9a\xf8s\x88=\xe6g\xbcv\xa9:?$\xad3\x90\x1c\xed\xa2\x12\xfd\xfcP\x84\xb0v8\x07\xb9ua}\n\xea7}\xea#c*k\xec\xdb\xc4\x83\x18P\xdd\x86\x98\xfc\xad\x8dG\xd6\x89\xc6H5\xc5:\x97\xb6\xa5\x12\xca\xc37[\xd2\x8c\xed\x87u\xfa\xc0\xcb3l/\x17\xcc\xf7\t\xb1z0\xc9\x9a"\x9c\x8b\x04\xecR\x88\x8e\x87\xa0\xe3\xcaLRF\xac\xc2\xfe\x04\xf4:SM\xf9\xd3\xf2\x10?N\xec\x93r\xc1!"\x8bF|\xd5|\xc9E\x03\xf6!K\x9f\x05]SH,\x0c}\x1d\x96\x1c\xf8\xf8\t\xce\x0b\x83\x9eO\x10\x8e\xb9\x01;p\x1c>\xdf\x03\x1e\xeec\xe6\xed\xfd\xda\xe7\x9d\x18\xe4\x1eq\xd9%\x0bF\x0ch\xdc\x9f\xc8\x0e\xbe\xffs=\x8dA\xe7\xeb\x90;\xed\xde\xd6\x8d\xd8\xf9.\xf5k\x18_\xd6&\x13\x7fN\xfb\'\xb63\xd3\xd8q\xfe\xbfl\xe7\xfd`\xefTP\xcc\x9b\xbd\xdfN\xd1\xa8\xb7\xd2\xf6T\x8fz\xaa\x8cy\xaeE!\xb4\x0c`3`\xfa3\x8eq\x9c\'a\xa2w\x98\'@\xec\xa3\xe0z\xa8\xa8\x08\xef\x03=\x06\xbd\xcf\xc9\xb6y\x8bSu$\x1e\xa8\xef\x91j\xeb*\xde\x167\x18\xd1\xeb1\x9f\xc6\xf5:\x08\x9b\xec%PBl\'/\xf7&\xb9o\xb1\xcf0p\xbb\x05\xdcW\x12|\x9a\xf0\x11\xb0\x93\x08\xf3\x11\xdfVI\x7f*\xce[mq\xbf\xb2\xd5\xa39\xde\x1f |\xc6\xb7\x1f\xa0\xdd=\xc4\xac`w\xc5=\x04b\x12\xee\x07\xa9G)m\x1d<?\xf4c?1.m\xd2\x9f\x8a\xf3\\E%"\xb2\xed\x9f\x01\x0fE\x00\xb1\x95\xdc\xf6\xfa\xdb\xfc\x8c\x00\xdb!\xa9\x87c?dF\x10\xeb\x19o\xf76\xbe\x07\xdejUJ\xd0/\xb0|\x94\x03#\xbd\x8d\xd3\xb9\x17\x03\x1c+\xdeC\xbd^\xc48 N\xfae$\x98X\x0er\xdc[\xc3\x89\xd4\x03\xf9\x92z!\xf9n$\xf0\xf7\xe8\x00%\x02\x1f\xc9\xe32\xbb\x17\xc9=\xcc\x93{\x95\xf3\xa2\xb3e|\x86 \xda\t\xa7\xd7y\x08\x80\xeb.\xf8V\xa8\x87\xe5:\x07\xa1\xc4;\x9b\xbd\x97\xb4\x07s\xdcO1\xf0zJ\xcf\xe3\xbaO\x18\x90\x0bO\xda\xe3z\xe0\xdb\x93\x9d\xc0a\xf9\xf8\xadmN`~\x12\xd1\x83\x00\xf3E\xf8\x1e\xf8x\xb2\xbe\x02\xce\x19D\xfcm\x8e\xf9\xfb=<\xef\x82\xaf\xf4E\xd3l\xf0\xed7\x12\xce\x19D\x88\xcbPL\xe4\x1c`\xd5\x838r.M\xa6\x0f$\x9e\x84@zg\xcfo\xa4I\x8a2\xe0\x00Zu\x17\x83\x1d\xb9\xd4\x8e\xa8\xefD\x1b\xbc/ \xf4\xe9\x9e\xda\xbaLx\x89Kr9/\xf9\x84\x99>\x9b\xf0\xe1\x8d\xcf\xf3\xeb\x8e\xef\xca\t\xddSW/|2\x88|RNW\xa7N\x03\xbb\xbe\xa6\x1c\xe0\xc1\xce%p\xf1\xcb6-\xf5E>\xde\x03\xf2\x95\xe3\x86\xe6A\xf5\xa4\xa9\xf71p\xfb\xc4\x0fp\x0e\x83\xc4\xf3\xe9\x9e\xc6\x1e2\xc1\x01\x97\xd8\xde\xdd\x1d\x97f\x0e\x81\x8e\xd9\xeb\xb7\x9e\xd6w|\xf8\xd8\xbd|\x03\x8f=s\xc8<\xbb\xfd\xd3\xae\xde\xf3\xc9\xebY\x81\x8b\xbe\xac\xcf\xcb=\xde;\x1eB\x9a\xab"\xf8\x9a9\xf8W\xba\\\xa2\xebk\xddJ\x9f\xb4\x87;\x94\xdc\xe4J\x96\xd9\x84\xab\xcc^\xbf\x15\x89\x16?\xdb\xf6\xfe\xc4\xb5\xf0\x8b`\rLq\xe5\xdf\xe7g\x7fz^\xdd\xdc7\xadK\xfc4\xff(\x16\xb3\xf8\xd1\xe4\xbb\xc7\x92\xec\xcbN\x1f9\xbe\x13\xd1\xc7\xb1b\xbc{\xcd\xef\xd4\xa7\xbbe{\x9e\xde\x1e\xban\xd3\x9e\x1f\x93\xa64\xa4\xba<\xdc\x96\xad\xee\xb1\x04\x8bV7\xf3v\xd5\x94\xc5j;;\x9c\xb7w\xd5M\xbcm\x95\x13K\xe4\x84\xf3B\xdb\xf2\xb6Z\x95\xc5\xfe\xe3xF\xf9\xe1<Q1\x044\xff\xc6\x13\x9d\xd8S\xde\x1cRn\xf6Hq\x93\xf2\x0f\xd1\xf5\xa6\xc0\xf5z\x82\xe9\xa7N\xc2y\xa4\x85\x83^\xf3\x12\xd8\x9f\xac1\xbf\x9a\x8c\xbccO\x82e\xe0\x8d\xc0\xcd\xae\n\xc4\xdeF\rq\xf2\x8e\xe4\xbb\x03\x92\xf5\x13\xd2V~W\xc7\x18"\xfcT\xe9\xacw\xdc\x81\xd6\xf7:\x19\xe2\xb5\xab9\x19\xf9K3}\xd7n\x13\x0b\xe0S\xa4\x0f>\x82\xe6ODN\x81\xb8b\xbeK\'^\x99\xf85\xf3L\xeaX\xe3\x9e+\xf0w\x07\x03\xb9\xbc\x1dKSp ~\x14d[\xc8{\xb4\xc8\xa1\xb4{\xfc\xdc\xc6\xcf%\xecK\xd79B\x0f\xf7\xf0>\x17\x89o\x85\xe7"~\x0f>\x16\xe18a=E\xa2.\x88\xb7\x93\xce\x1es\x03E\x06\xfc\x15\xe2U6l\xd8\x03\xf8Z\xe9\x17\xbe\xf6\x8a\xb0\x97\xc1q\xbfm\x81\xb1\xdb\x80\xdbN\x85\xa2^$1\x81j\xab;\xdb{\xe5C\xc2d\xe4C\x8b\x91\x0f\xb58\x1e\x8d*t\xfd\xc8\x87\x84\xe7\x91\x0f\x81?\xd9S\xde\xa4\x11>\xa4\xda\x06\xc6w\xb1\x01|\xaf\x08\xcf\x82\xd8\xe1\x84\xf1\xdd\x1c\xf1\xddz\x89!"a\xfa\xc9?\xcd\xef\xd1\x0c\xc7\xc5\xe0g\x8a\x17\x9c\xc4\xb8N\xeb\x8f\xfe\xc3\x86\xfe\x87h\x02\xf8\x8fp\xba\xcfv\xc6{\xc0\xe7\xa8\x02\xdc\x06|\xee)>\xa3E&\xcc\xa8\xbf\xf8\xe19K\xfd\x85\x8cF\x7f\xa1\xdan\xdc;C\xae}\xd5\x8f\xff\xd2\xcf\xcb\xf7+\x05\xc6\xe7\xe2\xbc\n\xe6\x7fN\xb6\xda\xee\xf3\xff<\xff\x9b\xe0}j\x83\xdf\xa8s&\x83\xd8n\xeb\x81>s\xf3!R@7U\xc2\x83\x88\xde\xcfH\x82D8\x08u\xa7\x92\xe7.\x7f\x01\x8c\xeb\xf17\\\xae\x9eE/|\x87py\xa8\xd7\x1a\x1e\xd5Y\xca\xed\x11\xe5?GjC\xef0Y3N\xeft\x7fH\xa8\xdd\x12]\xe6r\xafN\x02\xc4l\x03\xb7}\xc1m~Y\x9e\xf8\x19w3[\xccz>\xe1<l\xef\xe4\x9c\xd6\xe3P\xcc\xc2\xd5\x9c\x7fZ\x14\xa4N\xb4\xda\xc1;\x04}0\x10\x87\x14\x89F\xf3\x97\x99K\xe2\xa4}nh\xd5y1i\x9f\x92\xbb\xee\xe9I\xaa/Q\x00\x98\xf9\xd4\xb7SQ\xbe\xbb+\x1f\xee\x8d\x9b\xba\xb8Y\xcf\x8a\x12\xde\xcd.\xf5\xfe\xe9\xd2\xb6:\xb9.\x17]+\xdbxs9\xeb\xb7\x9f\xcb\x18\xa9\xcf\x87tb\x1f\xd0\xc4\xf0\xdf\xcf?\x10\xc8\xbc4*#\x82!\xc32\x7f\xc3\xa8\x85]\xbf\xc4\xff,\xad\xf3\x9e7\xbf\xc47\xc4\xaa>\xf0f?7\x86\xf8\xeb\xdc\xef:\r\xbc:mk\x13\xe6\xcf\xe05v\x1bo\x0f8V\xcdh\x1e\xe0\xf1\x15/r\x1d\xc7\xff\xf2m\xbe\xb9EB\xe8\xe2xQ\xc18\xb1\xd6\x91\x9c\xd38\x92\xdc\x03\x9e@i\n\xf6\xe6f[d4\x9el\x7f\xa2?\xea\x0fgB\x14\xfc#\xe6o\x98\xd0\xe1\xbf\t&(\xc4\xf6#aA\xf6\x0fHi0#\x87 X\x00\\\xcdV\xc8\x99\x0e\xc2\x05\x81\xbb\xb54\xa7\x88\xf8\xd7zR\x87sV0\xcc`=O\x81\xa3J\xf8\x8c\x08\xce7\x8c\xb9F\xbd\xb5\x17\x12\xe8\xe5*\x03\xf4@x\x0f\x94r\x14\x849)|_\x07N\xfbc}\xe0\x8cJ/L\xe8Y\x152N\xe3g\xf5\x08\x97\x0b\xe4\x1d\xd4\xc39\xb0\xc5\xa65HL\xb9\xcd\x99\xf9\xc3\xe6\xe35\x9e9\x00\x7f-\xd5\x87\xe9\xa5\xbb\xf0R\xd7\x85\xcf\xc3\x8a\xf8\xb8\x8a\xc8\xea\xe5\\B\xd3\xdd6\xed\xf2\xa9\xba\x18Z\x93\xc7\xf3q\x7fd\xdbVu\xf7\xb6o\x1a\x18+\xaaG\x87aEs\x12j\xda@,\x026\x8f\xcf\x97@\xfcZ\xe18\x8a\xcb-\x88\xa9$\xbc\xd7\xc5D>{\x85w`\xe3N\x91i\xce@\xf3\xf3hx\xa0q\xf8\x84\xfa2\xe2\xd2\x0e(x\xc9adC\x06\xf1\x04\xdeK\xf1\xf3\xfa\x9a\xa8\xa0c\n\xdew\tb\x81;\xd5\xdb\xacS\xb2F9f?\xf1]\xc2\xc4`\x93\\\xc6\xf1\xc5U\x19s\x15\xca\xe8\xa3\xe4\xd1\xe7\xe8\x82\x9c\n9\x90r\x88\xeb\xc41\xaeK[\xef\xbc)+\x87\xee\x81a\x1e\xe5\xed\x82y\xb7\x08\xd8\xf9)\xe1\x1c\x16\xc6\x81\xefM\xb8\x7f\xce\x80wQ\xff\n>rOc\xd7\x15\xb5#\xba\xc7SQ;\xdaP;\xa29\xb91\x9fCy\x83\xb1\xa7\x98D\xed4\xfeA\x1eh(l\xe1\xc7\xd8\xed]\xec\x9a\x16\xa4\x1e\xc1\xad\xf4\x99p+\x18H\x8eDd\xebB\x9f+\xa2`\xea\xc8\xceUp\xb8\xbah\xe7\x86(T\xb8\xac$\x94\r\x04$\xacN\xc7s\x0b\xfd\xfa\x0c%{\xc5\xfeSbZ\xbf\x7fwf\xec\xe3\x99>z5X6\xf8\xfc\x97P\xf2\xf1Z\xe3\x9fV\xdd\xa7\xb3b\xf4\xaa\xc9\x99\x8e\x8fg\xec>\x9d=\xf9\xf9Y\xb5\xff\x863~\xf4\xcc\xdb\xc7\xbd\x7fr\xe6m{8\x9f\xe3\xe9\xd3\r>\xfb\xf6w\xcf\xea\x8dg\xee\xc8Y\x95\x8fg\xee>\x9d\xc9\xf9\xd5<~v\xe6\xef\xed,\xd0/\xe7\xf1\xf1<\x02=s\xf8\xf1\x0c\xd2/\xe7A\xce\xe4|\\\x8fO\xe7T\x7f9\x8f\xff\xca\x19@r\xa19\x9d\x13\xca\x8c\x01\x91\xb3i\xf8\x8ci\xac>O\xa2\x9bg\xe7\x8cf\xca\xecV\xbe\r\xfb\xcf)\x15\xf3\x15\xd7\xc7=@\xe2\x93"r6\x86Y\x06\x02\xe059\xbb\x87\xc8\x9eB\xde/\x08\x87\xaal\xe3\x19s*j7\x98+\x90\x8d(!\xed\\z?\xef\xc4\xe5\x1e\xd1}\\\x058\xb8o\x81\xdf\xf2\xce\xd9\xd7\xb9\x92\xc5\x03\xf1\xb9\xce>\xe1\xd8\xfe\xa1 \xb9\x8b+II\xa3)\xf4Ir-,q\xa08v \xe7\xae\xb7]y\xe3\xcf\xf6\x03ky\xab\xad{\xbc\xc1z\x06\xef\x02\x8a\xd7\x0b\xa7\x8d\x11;\xdf\x01v\xee\xc1\xf6\x06\x87b\x02\xdd{\xach\xdeQ\xa4\xd8qC\x9e\x8d\xb89\x9e}1\xb3\xc08&j].\xc73z\xf4\xcc\x1f\xa2\xb9a\xb27\x05x\xa9Y\x83@\xb9\x0e\xed\xb7\xa0\x98D3\xe9/\xf2 \x98\x04\xeb\x01s\xaf\x81\xaf\x05\xe8\xea\xe7\x11\xc6k%i#x\x8e\xf3\xd4s6i\x1d\xc0\xf1\xba\xc6{\xb5\xe0\x8b\xe9^\x14=\xebBp\x9a\xcb\x1d|\xbe\xa3\xc2g\x10qn\xec\x13^}\x8c-\xa4\xe7\x11O\xdd\x1b2\x1f\xcd\x1ay\x82\xa0\xeb\xc0\x0bD\x9cs\xa3\xa5\x89\xe3\x08Q\xd0q\xdc \t9C\xf7\x0f\x1e\x18\x11\xbd\xf0\t\x1bx\x0b\xd9W\xd8\xcc\x85<\xfc/\xbcOR\xa9\x04?\xdb\xe7\x07\xe0)+\t|\x04\xf0\x0f\xf9^\xf8\xe7\x7f\xfe\xcb_\xff\xc7\xf7\x7fl\xe2\xa7c\x11\xd7\xdf\x7f\xaf\xafM\xfc\xfd\xf7\xfcZ\x1e\xbe\xff1\xb9r\xdf\xff\x9c\x00!;\xa6e\xf9\xfd\xf7k]&\xdf\x7f\xdf>o\xd3\xef\x7f\xaa\xbb8;~\xffK\xcc%\xff;\x89\x8f\xdb\xd9\xf4\xff|{\xfa\xcb\xb7o\xf4\xe7\xdf\xff\xf20\xfc\x93r>\xa6\xf1i\xfb\xfd\xcf\xff\xb3\xe9\xb2s\xbd\xfd_\xbf\xe1\xff\x81\xf2\x07\xf8\xd1\xbe\xfd\x07\xc1\t\r\xe6')))
except KeyboardInterrupt:
	exit()