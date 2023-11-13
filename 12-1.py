""" from bs4 import BeautifulSoup as bs
import requests as rq

url =  "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

res_html.select_one("body > div.container-doc > main > section > div > div.content-article > div.box_g.box_news_issue > ul > li:nth-child(1) > div > div > strong > a")

print(item)
print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt)
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods)
print(goods.get_text()) """

# select

""" from bs4 import BeautifulSoup as bs
import requests as rq

url =  "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss = res_html.select("a.wrap_thumb")
print(iss)
print("\n--------------------------------------\n")


print("\n--------------------------------------\n")
ct = res_html.select("a.wrap_thumb")
for j in ct :
    c = j.attrs["data-tiara-id"]
    print(c + "\n") """
    
# 이미지 저장
""" from bs4 import BeautifulSoup as bs
import requests as rq
import os
from urllib.request import urlretrieve as rl

url =  "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

imgs = res_html.select("img")
print(imgs)


linkimgs = []

for i in imgs:
    irs = i.attrs["src"]
    linkimgs.append(irs)
    
folder = "imgs/"
if not os.path.isdir(folder) :
    os.mkdir(folder)
    
i = 0
for ln in linkimgs :
    if str(ln).find("//t") == False :
        print(ln)
        continue
    else :
        pass
    
    i += 1
    rl(ln, folder + f"{i}.jpg")
    
    print(ln)
    linkimgs.append(img.attrs['src']) """
    
# 시리즈 생성
""" from pandas import Series as sr

data = [10, 20,30, 40]
sdata = sr(data)

print(sdata) """

# numpy 시리즈 생성
""" from pandas import Series as sr
import numpy as np

data = np.arange(1, 5)
sdata = sr(data)

print(sdata) """

# 인덱스 확인
""" from pandas import Series as sr

data = [10, 20,30, 40]
sdata = sr(data)

print(sdata.index) """

# 인덱스 설정
""" from pandas import Series as sr

data = [10, 20,30, 40]
sdata = sr(data)

sdata.indesx = ["a", "b", "c", "d"]
print(sdata) """

# 인덱스 생성1
""" from pandas import Series as sr

data = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]

sdata = sr(data, idx) """

# 인덱스 생성2

""" from pandas import Series as sr

data = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]

# sdata = sr(data = dt, index = idx)
# sdata = sr(data = idx, index = dt)
# sdata = sr(dt, idx)
# sdata = sr(index = idx, data = dt)
# sdata = sr(index = dt, data = idx)
print(sdata)  """

# 인덱스 생성3

""" from pandas import Series as sr

dt = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]

sdata = sr(data = dt, index = idx)
# print(sdata)

# sd = sdata.reindex(["a", "j", "c"])
# sd = sdata.reindex(["a", "c"])
# print(sd)

sd = sdata.reindex(["b"])
print(sd)
print("\n--------------------\n")
print(sdata["b"])
print("\n--------------------\n")

print(sdata.iloc[0])
print(sdata.iloc[2])
print("\n--------------------\n")

print(sdata.loc["a"])
print(sdata.loc["d"])

print(sdata[0]) """

# 인덱스 슬라이싱

""" from pandas import Series as sr

dt = ["alpha", "beta", "charlie", "delta"]
idx = ["ab", "bc", "cd", "de"]

sdata = sr(data = dt, index = idx)

sdata.loc["bc" : "cd"]
print("\n--------------------\n")
sdata.loc["bc" : ]
print("\n--------------------\n")
sdata.loc[:"bc"]
print("\n--------------------\n") """


# 인덱스 행번호
""" from pandas import Series as sr

dt = ["사과", "바나나", "수박", "참외"]
idx = ["가", "나", "다", "라"]

sdata.iloc[1:2]
print("\n--------------------\n")
sdata.iloc[2:]
print("\n--------------------\n")
sdata.iloc[:2]
print("\n--------------------\n") """

# 수정/추가/삭제

""" from pandas import Series as sr

dt = ["alpha", "beta", "charlie", "delta"]
idx = ["ab", "bc", "cd", "de"]

sdata = sr(data = dt, index = idx)

sdata.loc["cd"] = "echo"
print(sdata)
print("\n--------------------\n")
sdata.iloc[1] = "fox"
print(sdata) """

# 추가
""" sdata.loc["ef"] = "golf"
print(sdata) """

# 삭제
""" print("\n--------------------\n")
print(sdata.drop("bc"))
print("\n--------------------\n")
sd = sdata.drop("cd")
print(sd) """


# 연산
""" from pandas import Series as sr

s1 = sr([100, 200, 300], index=["a", "b", "c"])
s2 = sr([100, 200, 300], index=["b", "c", "a"])

sum = s1 + s2
print(sum_res)
print(sum_res.max())
print(sum_res.mean())
print(sum_res.min())
print("\n--------------------\n")

sub = s1 - s2
print(sum_res)
print(sum_res.max())
print(sum_res.mean())
print(sum_res.min())
print("\n--------------------\n")

mul_res = s1 * s2
print(mul_res)

div = s1 / s2
print(dv_res) """

# 연산

""" from pandas import Series as sr

data = {
    "삼성전자": "전기,전자",
    "LG전자": "전기,전자",
    "현대차": "운수장비",
    "NAVER": "서비스업",
    "카카오": "서비스업"
}

sdata = sr(data)
uniq = sdata.unipue()
sdata.unique()

# # 
# print(sc)

sv = sdata.value_counts()
print(sv) """


# 필터링
""" from pandas import Series as sr

idx = ["a", "b", "c", "d", "e"]
s1 = sr([1100, 270, 30, 450, 50], index=idx)
s2 = sr([150, 740, 810, 40, 25], index=idx)

fil = s1 > 300
print(fil)

print("\n--------------------\n")
print(s1[fil])
print(s1[fil].index)

print("\n--------------------\n")
fil1 = s2 > s1
print(fil)

print(s2[fil1])
print(s2[fil1].index)

print("\n--------------------\n")
print(s2[s2 > s1].index) """

# 정렬
from pandas import Series as sr

idx = ["a", "b", "c", "d", "e"]
dt = [1100, 270, 30, 450, 50]
s1 = sr(data=dt, index=idx)

sv = s1.sort_values()
print(sv)

# sv1 = s1.sort_values(ascending=False)
# print(sv1)