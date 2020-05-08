#!/usr/bin/env python
# coding: utf-8

# In[96]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
get_ipython().run_line_magic('matplotlib', 'inline')
CCTV_Seoul = pd.read_csv('C:/kcci_python/0506/01.CCTV_in_Seoul.csv',  encoding='utf-8')

#rename 을 이용한 컬럼명 변경  
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
#CCTV_Seoul.head()

#read_excel() 를 이용한 컬럼 인덱스 이름 지정
pop_Seoul = pd.read_excel('C:/kcci_python/0506/01.population_in_Seoul.xls', 
                          header = 2,
                          usecols = 'B, D, G, J, N',   #불러올 컬럼의 인덱스 번호나 이름을 지정
                          encoding='utf-8')
#pop_Seoul.head()

#컬럼 목록 inplace 
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별', 
                          pop_Seoul.columns[1] : '인구수', 
                          pop_Seoul.columns[2] : '한국인', 
                          pop_Seoul.columns[3] : '외국인', 
                          pop_Seoul.columns[4] : '고령자'}, inplace=True)
#pop_Seoul.head()	

#CCTV_Seoul , pop_Seoul     구별 
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
data_result.head()   #head(self, n=?)   head(n=?)

#2013년도 이전
#2014년  ~ 2016년
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head()

# '구별'을 기준으로 index 선언
data_result.set_index('구별', inplace=True)
data_result.head()

data_result.sort_values(by='소계', ascending=False).head(5)
data_result.sort_values(by='인구수', ascending=False).head(5)



# In[99]:


import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "C:/Windows/Fonts/HMFMPYUN.TTF"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') 
data_result.head()


# In[100]:


plt.figure()
data_result['소계'].sort_values().plot(kind='barh',grid=True,figsize=(10,10))
plt.show()


# In[101]:


data_result['CCTV비율']=data_result['소계']/data_result['인구수']*100
data_result['CCTV비율'].sort_values().plot(kind='barh',grid=True,figsize=(10,10))
plt.show()


# In[102]:


plt.figure(figsize=(6,6))
plt.plot(data_result['인구수'],data_result['소계'],'or' )
plt.xlabel('인구수')
plt.ylabel('CCTV 갯수')
plt.title('인구수 / CCTV 갯수')
plt.grid()
plt.show()


# In[94]:


plt.figure(figsize=(10,10))
plt.scatter(data_result['인구수'],data_result['소계'],s=50 )
plt.xlabel('인구수')
plt.ylabel('CCTV 갯수')
plt.title('인구수 / CCTV 갯수')
plt.grid()
fp1 =np.polyfit(data_result['인구수'], data_result['소계'],1 )
fp1 # 다항식 구성   기울기 , 절편 
f1=np.poly1d(fp1)  # 방정식 구성 
fx = np.linspace(100000,700000,100)
plt.plot(fx,f1(fx),ls='dashed',lw=3,color='g')
plt.show()


# In[95]:


fp1 =np.polyfit(data_result['인구수'], data_result['소계'],1 )# 다항식 구성   기울기 , 절편 
f1=np.poly1d(fp1)  # 방정식 구성 
fx = np.linspace(100000,700000,100)
data_result['오차']= (data_result['소계']-f1(data_result['인구수']))
df_sort =data_result.sort_values(by='오차',ascending=False)
df_sort

