·English

requires:

openssl with zlib support
star (apt-get install star)
Simple Python scripts to perform:

an adb backup of a specific application and uncompress it to a directory structure
recompress a directory structure back into a valid adb restore file
Example:

./ab_unpacker.py -p com.app.android -b app.ab

Creates an adb backup of com.app.android called app.ab and uncompresses it into ./com.app.android
./ab_packer.py -d ./com.app.android -b app_edit.ab -o app.ab -r

Repacks the contents of ./com.app.android into app_new.ab and attempts to restore it via adb

·中文版

测试环境：

openssl和slib组件
star（使用sudo apt-get install star）
python

特定的应用程序的备份/恢复备份→目录结构

例子：

命令：
./ab_unpacker.py -p com.app.android -b app.ab

创建一个名为app.ab的com.app.android的adb备份，并将其解压缩到./com.app.android
./ab_packer.py -d ./com.app.android -b app_edit.ab -o app.ab -r

将./com.app.android的内容重新打包到app_new.ab中，并尝试通过adb恢复它
