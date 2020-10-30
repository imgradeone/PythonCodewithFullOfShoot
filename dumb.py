# 瞎几把乱写的学习 Python 代码 1 - 2020/10/30

# print
m = "f@ck"
d = "you"

print(m + " " + d)

n = "你 X"
s = "死了"

print(n + s)

# str vs num
homo = "114514"
ass = 114514

if homo == ass:
    print("恶臭")
else:
    print("栽楞")

# os path
import os.path
a = os.path.isfile("monika.chr")

if a:
    print("Just Monika.")
else:
    print("你删你 X 的 Monika？？？？？？？？")

# 多重赋值
w, d, n, m = "我", "带", "你们", "打"
print(w + d + n + m)

# 浏览器
import webbrowser

webbrowser.open_new("https://insaneryuri.cn")

# MARENOL BGA
ren = "MARENOL"

if ren == "MARENOL":
    maren = "https://weibo.com/"
    link = "652868"
    link2 = "6715/Idt6a1J1X"
    sure = input("即将打开 MARENOL BGA，打开请输 https://insaneryuri.cn：")
    if sure == "https://insaneryuri.cn":
        print("晚安，好梦。")
        webbrowser.open_new(maren + link + link2)
    else:
        print("AHAHAHAHA")

# 小学生 while
bass = 0
while (bass < 1919810):
    print (bass)
    bass += 114
