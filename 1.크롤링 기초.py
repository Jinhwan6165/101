#!/usr/bin/env python
# coding: utf-8

# In[ ]:


impoert 라이브러리명


# In[ ]:


아나콘다 = 파이썬 + 주요 라이브럴리 + 쥬피터 노트북


# In[2]:


# 라이브러리 설치
# ! pip install 라이브러리명
get_ipython().system(' pip install selenium')


# In[3]:


# from 라이브러리명 import 함수명
from selenium import webdriver   # selenium 라이브러리에서 webdriver


# In[ ]:


selenium --> 브라우저 조작 라이브러리 (브라우저: IE, 사파리, 크롬, 엣지 와 같은 것)
selenium -->(브라우저 열기/ 사이트 접속하기/ 클릭하기/ 입력하기/ 삭제하기) 등의 명령어를 할 수 있다.

BeautifulSoup ("HTML안에서... 부분 찾아줘..."라는 명령 실행가능)


# In[ ]:


#webdriver.브라우저()
webdriver.Chrome() #C 대문자


# c;/infroms/chromdriver.exe # 윈도우 경우
#  ./chromedriver Mac 의 경우 현재 폴더에 저정

# In[10]:


browser=webdriver.Chrome('C:/informs/chromedriver.exe')  # 브라우저 창에 url을 직접 입력해도 된다.


# In[11]:


# 접속하기 get(url)
url = 'https://naver.com'
browser.get(url)


# In[9]:


#브라우저 닫기
browser.close()


# In[14]:


url='https://daum.net'
browser.get(url)


# url에는 한글이 들어가 못한다. --> 자음과 모음을 다따로 뗴서 바꿈... %DD %AA 와 같이
# 

# In[15]:


url = "https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=부동산"
browser.get(url)


# https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=부동산

# URL = URL은 '?'를 기준으로 앞은 주소, 뒤는 파라미터 부분으로 나뉜다. 
# 파라미터는 한개 또는 여러개를 사용할 수 있으며, 여러개 사용하기 위해서는 '&'으로 구분한다
# 파라미터 : 속성명=값&속셩명=값&속성명=값

# In[18]:


search_list=['부동산','파이썬','삼성','입시']
for word in search_list:
    print(word)
    url = f"https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q={word}"
    print(url)
    browser.get(url)


# In[ ]:





# In[19]:


# 웹페이지 정보 다운받기
html = browser.page_source
html


# HTML --> 브라우저가 화면에 보여주는 약속과 같은 것이다.

# # HTML & BeautifulSoup

# In[ ]:


# HTML 특징
<태그명> </태그명> # 시작 ~ 끝을 알 수 있음.

<태그명 속성 = 값> </태그명> # 속성이 들어갈 수 있음
<태그명 속성 = 값 소속성=값 속성=값> </태그명> # 속성이 여러개 들어갈 수 있음

<태그1>
    <태그2><.태그2>
    <태그3>
        <태그4>/<태그4>
    </태그3>
</태그1>

<태그> 장남수 </태그>  # --> 화면에는 "장남수"만 뜬다. 명령시에는 태그를 기준으로 명령어를 입력한다.
<p>
    <span class = 'name'> 장남수 <span> 
    #  태그명이 span인거 찾아줘.... -> 결과 값이 너무 많은 경우, 속성에 정보를 추가한다.
    # 태그명이 span & class 속성값이 name인거 찾아줘
    # 사용할 속성값을 다 사용하엿을 경우에는 상위 부모테그를 입력해준다.
    # 태그명이 span & class속성값이 name인거...그러면서 부모태그가 p인거
</p>


# In[20]:


from bs4 import BeautifulSoup # B, S 대문자


# In[ ]:


html = browser.page_source
html


# In[25]:


#say = '''

#say = '안녕하세요 \n 반갑습니다.' 여러줄을 쓰지 못하고 여러줄을 쓰려면 \n을 넣어줘야 하는데, 이를 쉽게 하기 위해서 ''' 을 쓴다.

say = ''' 안녕하세요
반갑습니다.
보리꼬리 하이'''
print(say)


# In[21]:


#예시) 러닝스푼즈 데이터분석입문 강의 
html = '''
<h1> HTML예시 
    <span> 파이썬 입문부터 시작하는 데이터 분석 마스터</span>
    <p id="weeks1" class="seminar" title="first"> 1주차
        <span class = "title"> 파이썬 맛보기 </span>
        <span class = "presenter"> 장남수 </span>
        <span class = "date"> 1월1일 </span>
        <span class = "point"> 파이썬 설치 사전 안내 </span>
        <a href = "https://kiddwannabe.blog.me/221154599192">네이버 블로그-아나콘다설치</a>
    </p>
    <p id="weeks2" class="seminar" title="second"> 2주차
        <span class = "title"> 크롤링 해보기 </span>
        <span class = "presenter"> 장남수 </span>
        <span class = "date"> 1월2일 </span>
        <span class = "point"> selenium / html </span>
        <a href = "https://kiddwannabe.blog.me/221177292446">네이버 블로그-크롤링</a>
    </p>
    <p id="weeks3" class="seminar" title="third"> 3주차
        <span class = "title"> 크롤링 실습 </span>
        <span class = "presenter"> 장남수 </span>
        <span class = "date"> 1월3일 </span>
        <span class = "point"> 노래순위, 베스트셀러 </span>
        <a href = "https://kiddwannabe.blog.me/">네이버 블로그</a>
    </p>
    <p id="weeks4" class="seminar" title="fourth"> 4주차
        <span class = "title"> 판다스 살펴보기 </span>
        <span class = "presenter"> 장남수 </span>
        <span class = "date"> 1월4일 </span>
        <span class = "point"> pandas </span>
        <a href = "https://kiddwannabe.blog.me/">네이버 블로그</a>
    </p>
    <p id="weeks5" class="seminar" title="fifth"> 5주차
        <span class = "title"> 상가 업력 분석하기 </span>
        <span class = "presenter"> 장남수 </span>
        <span class = "date"> 1월5일 </span>
        <span class = "point"> 공공데이터 분석 </span>
        <a href = "https://kiddwannabe.blog.me/">네이버 블로그</a>
    </p>            
    <p id="weeks6" class="seminar" title="sixth"> 6주차
        <span class = "title"> 데이터 시각화 </span>
        <span class = "presenter"> 장남수 </span>
        <span class = "date"> 1월6일 </span>
        <span class = "point"> seaborn </span>
        <a href = "https://kiddwannabe.blog.me/221728411362">네이버 블로그-seaborn</a>
    </p>  
    <p id="weeks7" class="seminar" title="seventh"> 7주차
        <span class = "title"> 네이버 쇼핑몰 수집/분석 </span>
        <span class = "presenter"> 장남수 </span>
        <span class = "date"> 1월7일 </span>
        <span class = "point"> youtube </span>
        <a href = "https://kiddwannabe.blog.me/">네이버 블로그</a>
    </p> 
</h1>
'''


# In[22]:


html


# In[26]:


from bs4 import BeautifulSoup


# In[29]:


#어떤 데이터를, 어떤 기준으로 읽어야하는지 알아야 한다.
soup= BeautifulSoup(html, 'html.parser')   #html.parser  의 . parser 은 고정값이다. parser은 찾는다는 의미
soup


# In[34]:


#soup.select('태그조건')  #()안에 해당하는 내용을 다 찾아줘  --> 인덱스 번호를 이용해서 태그 1개를 선택한다. 
#    --> tag.text (태그 기호를 빼달라는것)
#soup.select('태그명')

#soup.select('a')[2]   # <a href="https://kiddwannabe.blog.me/">네이버 블로그</a>
soup.select('a')[2].text


# select의 경우는 보통 리스트 형태로 수집된다.

# In[37]:


for tag in soup.select('a'):
    print(tag.text)


# In[43]:


#soup.select('태그조건')  #()안에 해당하는 내용을 다 찾아줘  --> 인덱스 번호를 이용해서 태그 1개를 선택한다. 
#    --> tag.text (태그 기호를 빼달라는것)
#soup.select('태그명')
#soup.select('span')
#soup.select('.class속성값')

#soup.select('.title')   # class 속성값이 title 인것 추출  (태그명 상관없이)
soup.select('span.title')   # 태그명이 span & class 속성값이 title 인것 추출 


# In[46]:


#soup.select('#id속성값') # Id 속성값이 weeks1인것 찾기

soup.select('#weeks1')


# In[50]:


#soup.select('상위태그정보 > 하위태그정보')

soup.select('#weeks1 > span.title')
#"id속성값이 weeks1인 태그 파로 아래에 있는"
# "태그명이 span이면서 class속성값이 title인것 모두 찾기"


# In[51]:


soup


# In[53]:


week_list = soup.select('p')
#태그명이 'p' 인 개수 찾기
len(week_list)


# In[101]:


# 1주차 정보만 선택
week = week_list[0]

# 정보(제목, 날짜, ......) 찾기 
#title = week.select('span') # week 내 태그명이 span 찾기
title = week.select('span.title')[0].text # 위에 조건 + class 속성값이 title인 것 
presenter = week. select('span.presenter')[0].text
date = week.select('span.date')[0].text
point = week.select('span.point')[0].text
link = week.select('a')[0]['href']
link
print(title, presenter, date, point, link)


# select의 경우 무조건 리스트의 형태로 나옴 태그는 리스트 안에 들어있으므로 index번호를 적어야 원하는 tag가 선택된다.
# 
# link 
# 보통 원하는 정보는 화면에 나타나는 부분을 추출하지만, 링크와 같이 속성정보가 필요할 떄가 있다.
# soup.select() --> [태그1, 태그2,...] --> 태그1 []--> 태그1.text
#                                                  --> 태그1['속성명']

# In[102]:


# 1주차 정보만 선택
#week = week_list[0]
for week in week_list:
    # 정보(제목, 날짜, ......) 찾기 
    #title = week.select('span') # week 내 태그명이 span 찾기
    title = week.select('span.title')[0].text # 위에 조건 + class 속성값이 title인 것 
    presenter = week. select('span.presenter')[0].text
    date = week.select('span.date')[0].text
    point = week.select('span.point')[0].text
    link = week.select('a')[0]['href']
    print(title, presenter, date, point, link)


# ### 저장하기

# In[107]:


results = []
for week in week_list:
    # 정보(제목, 날짜, ......) 찾기 
    #title = week.select('span') # week 내 태그명이 span 찾기
    title = week.select('span.title')[0].text # 위에 조건 + class 속성값이 title인 것 
    presenter = week. select('span.presenter')[0].text
    date = week.select('span.date')[0].text
    point = week.select('span.point')[0].text
    link = week.select('a')[0]['href']
    print(title, presenter, date, point, link)
    data = [title, presenter, date, point, link]
    results.append(data)  # results 리스트에 마지막 원소로 data 추가해줘


# In[108]:


print(results)


# In[110]:


results


# In[106]:


data


# In[111]:


import pandas as pd


# In[117]:


df = pd.DataFrame(results) # 표형태 데이터  # D과 F는 대문자
df.columns = ['주제','강사','날짜','주요내용','링크']  #컬럼멸 바꾸기
df.to_excel('./test.xlsx')


# In[ ]:




