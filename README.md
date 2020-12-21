
##首先说明
“学习强国”学习平台是由中共中央宣传部主管，以习近平新时代中国特色社会主义思想和党的十九大精神为主要内容，立足全体党员、面向全社会的优质平台。
本项目初衷是本人为了学习python和appium等自动化框架，本人也是非专业编程人员，所以还需要各路高手一起完善项目。
本项目遵守开源许可协议，严禁用于商业用途，禁止使用进行任何盈利活动，对使用本项目进行一切非法行为产生的后果，本人概不负责。

## 项目主要参考：
>#### <https://github.com/kessil/AutoXue> 和 <https://github.com/TechXueXi/AutoXue>
>####非常感谢以上项目作者！
>####我的修改主要基于kessil的项目，修改也是延续他的思路而成。
>####交流群 https://t.me/buxuebushuang，欢迎有兴趣的同好一起加入学习python。

>## 12.21更新
1. 修正启动以后有时候停留在首页不动的情况 
2. 修正逍遥模拟器启动后app后，app停留在后台
3. 增加背景广播静音
4. 题库更新
### <u>重要提示：推荐各位使用逍遥模拟器进行本项目学习，因为大量测试建立在该模拟器下。其他模拟器不能保证所有功能正常实现。</u>
  

>## 12.17更新
1. 修正雷电模拟器阅读学习错误
2. 增加多账号学习策略，现在可以选择是同时一起学（并行模式，适合配置较高的机器），或者是学完一个在学另外一个（队列模式）。

>## 12.15 代码上线
## 已实现功能
#### 1. 满分自动学习（除强国运动外），请注意如果升级到2.19版，订阅无法自动实现。
#### 2. 多个号同时一起学习
#### 3. 支持三种模拟器，可以任意在ini文件中选择切换使用。
#### 4. 模拟器设置好后，程序会自动启动模拟器，自行开始学习。多号同刷，请看后面的使用说明
#### 5. 为满足刷星、刷题（更新答题库）或者补学等要求，各个模块可以单独测试运行，可以设置测试次数。（挑战答题通关不是梦，本人没那么无聊，没测试过50次以上）
#### 6. 支持sqlite和mysql题库，在data目录下的数据文件已经由8000题题库，且基本经过本人几个月来不停更正错误答案，基本错误量已经非常少。
#### 7. 提供了帐号RSA加密功能。        
#### 8.提供由json题库转换到mysql数据库的脚本（json_to_mysql.py），提供从<https://124731.cn/>网上提供的题库转化到本地数据库的不成熟的脚本；update_packages.py是自动升级所有本机python模块的（供“版本不是最新就不爽”强迫症患者使用）
#### 9.程序使用的模块都是更新至最新版本，所有测试都是基于到目前为止的最新版本

>## 以下为服用指南
### 1. 本程序核心运行程序为autoxue.py，在config文件夹下的default.ini为本项目的配置文件
### 2. 安装python，或者安装vscode、pycharm等IDE直接在里面调试运行也行 
### 3. 安装JDK（我使用的jdk1.8.0_121）
### 4. 安装android sdk r24.4.1
### 5. 安装模拟器（逍遥、雷电、Nox三选一），推荐使用逍遥模拟器（本人大量测试在该模拟器下完成）。模拟器尽量设置较高的分辨率；并在default.ini文件里面设置安装目录（文件夹）信息。目录名称里面又没有含有空格没关系。
**ini文件内相应代码如下**
~~~
    注意ini文件设定项前有(;或者#)是注释行，相同的键值是N选一，选了一个注意注释掉另外的（前面加;或者#号，注意是英文符号）。
    [emu_args]
    # 是否采用真机进行答题，是（1），不是（0）
    true_machine = 0
    
    # Microvirt（逍遥模拟器）、雷电（leidian）和Nox（夜神模拟器）三选一
    emu_name = microvirt
    ;emu_name = nox
    ;emu_name = leidian
    microvirt_path = D:\Program Files\Microvirt\MEmu
    nox_path = D:\Program Files\Nox\bin
    leidian_path = D:\Program Files\leidian\LDPlayer4
~~~
### 6. 安装运行需要的模块，运行setup.cmd，或者直接在程序目录下运行以下命令。
~~~
    python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    或者
    python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
~~~
### 7.账号设置：可以多个号，同时一起刷（因为订阅耗时间较多，有单独为各个号设置的事先翻页页数：subscribed_pages_1）
**ini文件内相应代码如下**
~~~
# 用户名和密码
username1 = f6ycdByVgBkCHQwqC+qU00MzqtKtWvJDBJxg8LyY2vxC3dQ+c50xw7Fk2XiY+RIb4YnGrTFq4u+dZC5U9KA+vH40mkHOpWQnIZVSFvQse5Z0si9GilOA/9aNVjV1yz5A88/I2E/yZ0yQMpE7iiHWJPzfHB2vwKr9b0LHb0c9DAE=
password1 = j9zzXRpPOy6SIfTLijMXCldNEkmlR+H1jxXLjIo1preGIs26QyFPKZ+/gk5hktnoaT0n4jDJGAsi08s7swIv7ucvSXqBkAQt0WYqn7seIZ13Ow79f0kx6MalCRX3/AKtrOhBCcHPtyDbQbvhMWyTrS1PxEIOibz7tONogGDAgzw=
# 多开的话，分两种情况：逍遥模拟器为第一类，雷电和Nox为第二类情况。
# 第一类情况，因为逍遥模拟器是固定名字（'MEmu', 'MEmu_1', 'MEmu_2', 'MEmu_3',...）的，根据实际运行个数修改为emu_mv_1=MEmu, emu_mv_2=MEmu_1,emu_mv_3=MEmu_2等名称。可以参考ini里面
emu_mv_1 = MEmu
# 第二类情况：下面是设置夜神或者雷电模拟器，因为夜神和雷电启动模拟器是以多开器里命名的名字来启动的，所以要和多开器里面的命名相同。注意是键名是命名形式："emu_nox_"+数字，名字和多开器里面的名字相同即可。
emu_nox_1 = long
# 为提高订阅效率，设置事先翻过已经订阅的页面
# 在程序里面有提示上次翻动到第几页有订阅内容
# 设置为0表示订阅已经全部完成了，无须在订阅（这部分会在以后版本更新为根据上次翻页情况自动设置）
subscribed_pages_1 = 54   
~~~
### 8. 由于采用的是数据库，可以考虑安装一个Navicat进行数据库管理数据。注意在ini文件里面设定你喜欢用的数据库；默认是sqlite，data目录下已有相应的题库数据库。对“答题争上游”和“双人对战”胜负情况做简单统计。
**ini文件内相应代码如下**
~~~
    注意ini文件设定项前有(;或者#)是注释行，相同的键值是N选一，选了一个注意注释掉另外的
    # 选择数据库平台
    [database]
    # sqlite3数据库存储在/data文件夹下
    data_platform = sqlite3
    ;data_platform = mysql
~~~
### 9. APP版本版本更新到2.19以后，订阅页面变化会导致程序无法自动订阅，造成死循环。已经升级到2.19的，可以注释掉以下代码（目前是539行）
**python.py文件内相应代码如下**
~~~
    if module_name == '订阅' and (self.subscribe not in self.run_modules) \
            and 0 != cfg.getint('users', 'subscribed_pages_' + self.app_args['id']):
        self.run_modules.append(self.subscribe)
~~~
#### 10.其他无关运行的小知识
* **如果需要将pip源设置为国内源，阿里源、豆瓣源、网易源等**  
在windows操作如下：  
（1）打开文件资源管理器(文件夹地址栏中)  
（2）地址栏上面输入 %appdata%  
（3）在这里面新建一个文件夹 pip  
（4）在pip文件夹里面新建一个文件叫做 pip.ini ,内容写如下即可  
~~~
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
~~~

>#常见问题
---
* ### 运行python出现（NameError: name 'XXXXXXXX' is not defined）报错
解决方法：  
请安装python 3.7+以上版本，安装以后运行如下命令
~~~
pip install XXXXXXXX
~~~  
#### XXXXXXXX为错误提示中（NameError: name 'XXXXXXXX' is not defined）对应模块名。

---

### 本自动学习脚本的缺点：对电脑配置要求较高，且安装运行环境很麻烦，需要有少量python知识  

---

## 免责申明

`AutoXue`为本人`Python`学习交流的开源非营利项目，仅作为`Python`学习交流之用，使用需严格遵守开源许可协议。严禁用于商业用途，禁止使用`AutoXue`进行任何盈利活动。对一切非法使用所产生的后果，本人概不负责。

## 写在最后

+ 本人学习python时间较短（一个半月），有很多不懂的地方，只是对大神的项目作了些修补而已，错漏地方还有很多，在此再次感谢原项目作者，从中学习到很多python的知识。
+ 强烈建议需要自定义配置文件的用户下载使用vscode编辑器,[why vscode?](https://hacpai.com/article/1569745141957)，请一定不要使用系统自带记事本修改配置文件。
"# MyAutoXuexi" 
