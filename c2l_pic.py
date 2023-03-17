import re
import requests
import os

RE_pic = re.compile("(https://cdn.jsdelivr.net/gh/shanguwei/CDN@latest/)")
new_pic = "http://image.shangu127.top/"
c_list = os.listdir("./posts")
old_dir = ["./posts/" + i for i in c_list]
new_dir = ["./new/" + i for i in c_list]

for name in c_list:
    files = "./posts/" + name
    content = open(files,"r",encoding='utf-8').read()
    result = content.replace("https://cdn.jsdelivr.net/gh/shanguwei/CDN@latest/", new_pic)
    new = "./new/" + name
    w = open(new,"w",encoding='utf-8')
    w.write(result)
    w.close()
