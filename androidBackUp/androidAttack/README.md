·中文版

检测的主要原理

首先获取被导出的组件，然后获得这个组件的action。
因为启动组件，比如activity和service都有两种启动方式，
一种通过设置component的显式启动，
另一种是通过设置action的隐式启动，
所以方法attack里覆盖了这两种方法，
一是直接启动组件名，不带action测试；
另外是只发送action测试无组件的情况。

插件的安装

安装drozer插件的命令为 module install 插件的绝对路径
比如我的就是"module install /home/drozer_module/drozer.attack.activity.py"，
文件名与插件中的path变量有关，比如path是['drozer','attack']，
我们的文件就要命名为drozer.attack.xxx，xxx是可以自定义的；
另外一种方式就是目录形式的，建立目录drozer，子目录attack，里面文件名就可以是xxx.py了。

·English

detection of test

First of all ,get expoeted provider,then get provider'saction.
because start provider's way:activity & service
own way:component others way setting action hidden started
and function attack way include two way.
otherwish only send action test without provider.

Installtion plugin

install plugin :
"module install /home/drozer_module/drozer.attack.activity.py"
setting path :
path['drozer','attack']
DIR:
mkdir drozer/attack/XXX.py

mail:to contant
yushan8603@gmail.com
yushan8603@163.com
