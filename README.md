# html2md

应该不会有多少人遇到这种情况

hexo搭建的博客本地文件丢失后，只能从服务器的html文件转换回来。
目前脚本只是实现了butterfly主题的文章页面配置恢复，后续看情况补充正文（文章不多可以直接手动复制）

# 使用教程

将服务器中文章html文件下载下来，存放到一个文件夹内

将需要恢复的md文件放置于old_blog文件夹，如图：

![](https://github.com/shanguwei/html2md/blob/main/image/1.png)

直接运行脚本即可。

如果主题不同，需要看情况修改正则表达式和脚本中 `standard `变量内容。

# 图床迁移

就是一个简单的替换文本的脚本，根据自己图床来调整变量即可。

# 效果

我这里是直接爬下来的，所以自带title，后续补上脚本

![](https://github.com/shanguwei/html2md/blob/main/image/2.png)

恢复后：



![](https://github.com/shanguwei/html2md/blob/main/image/3.png)
