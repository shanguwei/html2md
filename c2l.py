'''
By Shangu
装系统hexo本地文件全没了，然后就诞生了这个脚本，顺便学学正则
脚本针对butterfly主题格式写的，主题不同需要看情况修改正则的特征值
'''
import re
import os


#top_img
RE_topimg = re.compile("background-image: url[(]'(.+)'[)]")
RE_cover = re.compile('''"og:image" content="(.+)">''')
RE_title = re.compile('''"og:title" content="(.+)">''')
RE_date = re.compile('''article:published_time" content="(.+)[.]''')
RE_tags = re.compile('''"article:tag" content="(.+)">''')
RE_blogtitle = re.compile(" (.+)")

# print(result)
md_list = os.listdir("./old_blog")
md_list = ["./old_blog/" + i for i in md_list]
title_list = [RE_blogtitle.search(open(i,"r",encoding="utf-8").read())[1] for i in md_list]

for root,dirs,files in os.walk("./cloud/"):
    for file in files:
        content = open(os.path.join(root,file),"r",encoding="utf-8").read()
        top_img = RE_topimg.search(content)[1]
        cover = RE_cover.search(content)[1]
        title = RE_title.search(content)[1].replace("。","")
        date = RE_date.search(content)[1].replace("T", " ")
        # print(os.path.join(root,file))
        if RE_tags.search(content) == None:
            tags = "unknown"
        else:
            tags = RE_tags.search(content)[1]
        standard = '''\ndate: {date}\ncover: {cover}\ntags: {tags}\ntop_img: {top_img}\n---'''
        result = standard.format(title=title, date=date, cover=cover, tags=tags, top_img=top_img)
        key = md_list[title_list.index(title)]
        blog = open(key,"r",encoding="utf-8").read()
        blog = blog.replace("\n---",result)
        new_blog = open(key,"w",encoding="utf-8").write(blog)

print("success!")