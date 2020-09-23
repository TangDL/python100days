
# 2.管道和重定向
 - 管道的使用： |
    - 查找当前目录下文件的个数：find ./ | wc -|
    - 输出当前目录下的文件和文件夹，给每一项加一个编号： ls | cat -n
    - 查找recode.log中包含AAA，但不包含BBB的记录的总： cat recode.log | grep AAA | grep -v BBB | wc -|
 总结： | 前面的命令用于生成输入，|后面的命令用于对输入进行操作
 
 - 输出重定向和错误重定向： > / >> / 2>
    - cat recode.log | sort | uniq > recode1.txt
 
 - 输入重定向
~~~
echo "hello, world!" > recode.txt                     # echo 实现字符串的输出
wall < recode.txt                                     # wall 命令将会将讯息传递给mesg设定为yes的使用者
"I wish you know I love you!" > recode.txt
wall < recode.txt 
~~~

 - 多重定向: tee 
    - 下面的命令除了将会在终端显示ls的结果外，还会把结果存储在ls.txt文件中： ls | tee -a ls.txt
    
 - 别名： alias 给已有的命令，设置一个别名
    - alias lss= 'ls -l' 
 - 去除别名：unalias 删除某个命令的别名
    - unalias lss
 
# 3.文本处理
 - 字符流文本编辑器：sed   是一个操作过滤和转换文本内容的工具
    - sed "2a banana" fruit.txt :                   # 在fruit.txt的第二行后面加入banana
    - sed "2i banana" fruit.txt :                   # 在fruit.txt的第二行前面加入banana
 
 - 模式匹配和处理语言：awk