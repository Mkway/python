```python
import pandas as pd
CCTV_Seoul = pd.read_csv('C:/kcci_python/0506/01. CCTV_in_Seoul.csv',  encoding='utf-8')
# print(CCTV_Seoul.head())
# print(CCTV_Seoul)


CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)


Popul_Seoul = pd.read_excel('C:/kcci_python/0506/01. population_in_Seoul.xls' , header =2  , usecols='B,D,G,J,N' ,encoding ='utf-8')
Popul_Seoul.rename(columns ={Popul_Seoul.columns[0]:'구별',
                              Popul_Seoul.columns[1]:'인구수',
                             Popul_Seoul.columns[2]:'한국인',
                             Popul_Seoul.columns[3]:'외국인',
                              Popul_Seoul.columns[4]:'고령자'}, inplace = True)
data_result = pd.merge(CCTV_Seoul, Popul_Seoul , on ='구별')
data_result.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>2780</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>773</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
      <td>453233.0</td>
      <td>449019.0</td>
      <td>4214.0</td>
      <td>54622.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>748</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>884</td>
      <td>388</td>
      <td>258</td>
      <td>184</td>
      <td>81</td>
      <td>603772.0</td>
      <td>597248.0</td>
      <td>6524.0</td>
      <td>72548.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>1496</td>
      <td>846</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
      <td>525515.0</td>
      <td>507203.0</td>
      <td>18312.0</td>
      <td>68082.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
del data_result['2013년도 이전']
data_result.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>2780</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>773</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
      <td>453233.0</td>
      <td>449019.0</td>
      <td>4214.0</td>
      <td>54622.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>748</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>884</td>
      <td>258</td>
      <td>184</td>
      <td>81</td>
      <td>603772.0</td>
      <td>597248.0</td>
      <td>6524.0</td>
      <td>72548.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>1496</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
      <td>525515.0</td>
      <td>507203.0</td>
      <td>18312.0</td>
      <td>68082.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
del data_result['2014년']

```


```python
data_result
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>2780</td>
      <td>584</td>
      <td>932</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>773</td>
      <td>155</td>
      <td>377</td>
      <td>453233.0</td>
      <td>449019.0</td>
      <td>4214.0</td>
      <td>54622.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>748</td>
      <td>138</td>
      <td>204</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>884</td>
      <td>184</td>
      <td>81</td>
      <td>603772.0</td>
      <td>597248.0</td>
      <td>6524.0</td>
      <td>72548.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>1496</td>
      <td>390</td>
      <td>613</td>
      <td>525515.0</td>
      <td>507203.0</td>
      <td>18312.0</td>
      <td>68082.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>광진구</td>
      <td>707</td>
      <td>53</td>
      <td>174</td>
      <td>372164.0</td>
      <td>357211.0</td>
      <td>14953.0</td>
      <td>42214.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>구로구</td>
      <td>1561</td>
      <td>246</td>
      <td>323</td>
      <td>447874.0</td>
      <td>416487.0</td>
      <td>31387.0</td>
      <td>56833.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>금천구</td>
      <td>1015</td>
      <td>269</td>
      <td>354</td>
      <td>255082.0</td>
      <td>236353.0</td>
      <td>18729.0</td>
      <td>32970.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노원구</td>
      <td>1265</td>
      <td>451</td>
      <td>516</td>
      <td>569384.0</td>
      <td>565565.0</td>
      <td>3819.0</td>
      <td>71941.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>도봉구</td>
      <td>485</td>
      <td>42</td>
      <td>386</td>
      <td>348646.0</td>
      <td>346629.0</td>
      <td>2017.0</td>
      <td>51312.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>동대문구</td>
      <td>1294</td>
      <td>198</td>
      <td>579</td>
      <td>369496.0</td>
      <td>354079.0</td>
      <td>15417.0</td>
      <td>54173.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>동작구</td>
      <td>1091</td>
      <td>103</td>
      <td>314</td>
      <td>412520.0</td>
      <td>400456.0</td>
      <td>12064.0</td>
      <td>56013.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>마포구</td>
      <td>574</td>
      <td>169</td>
      <td>379</td>
      <td>389649.0</td>
      <td>378566.0</td>
      <td>11083.0</td>
      <td>48765.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>서대문구</td>
      <td>962</td>
      <td>68</td>
      <td>292</td>
      <td>327163.0</td>
      <td>314982.0</td>
      <td>12181.0</td>
      <td>48161.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>서초구</td>
      <td>1930</td>
      <td>336</td>
      <td>398</td>
      <td>450310.0</td>
      <td>445994.0</td>
      <td>4316.0</td>
      <td>51733.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>성동구</td>
      <td>1062</td>
      <td>241</td>
      <td>265</td>
      <td>311244.0</td>
      <td>303380.0</td>
      <td>7864.0</td>
      <td>39997.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>성북구</td>
      <td>1464</td>
      <td>360</td>
      <td>204</td>
      <td>461260.0</td>
      <td>449773.0</td>
      <td>11487.0</td>
      <td>64692.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>송파구</td>
      <td>618</td>
      <td>68</td>
      <td>463</td>
      <td>667483.0</td>
      <td>660584.0</td>
      <td>6899.0</td>
      <td>72506.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>양천구</td>
      <td>2034</td>
      <td>30</td>
      <td>467</td>
      <td>479978.0</td>
      <td>475949.0</td>
      <td>4029.0</td>
      <td>52975.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>영등포구</td>
      <td>904</td>
      <td>195</td>
      <td>373</td>
      <td>402985.0</td>
      <td>368072.0</td>
      <td>34913.0</td>
      <td>52413.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>용산구</td>
      <td>1624</td>
      <td>112</td>
      <td>398</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>은평구</td>
      <td>1873</td>
      <td>278</td>
      <td>468</td>
      <td>494388.0</td>
      <td>489943.0</td>
      <td>4445.0</td>
      <td>72334.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>종로구</td>
      <td>1002</td>
      <td>211</td>
      <td>630</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>중구</td>
      <td>671</td>
      <td>72</td>
      <td>348</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>중랑구</td>
      <td>660</td>
      <td>177</td>
      <td>109</td>
      <td>414503.0</td>
      <td>409882.0</td>
      <td>4621.0</td>
      <td>56774.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_result.set_index('구별', inplace =True)
data_result.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>2780</td>
      <td>584</td>
      <td>932</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>773</td>
      <td>155</td>
      <td>377</td>
      <td>453233.0</td>
      <td>449019.0</td>
      <td>4214.0</td>
      <td>54622.0</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>748</td>
      <td>138</td>
      <td>204</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>884</td>
      <td>184</td>
      <td>81</td>
      <td>603772.0</td>
      <td>597248.0</td>
      <td>6524.0</td>
      <td>72548.0</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>1496</td>
      <td>390</td>
      <td>613</td>
      <td>525515.0</td>
      <td>507203.0</td>
      <td>18312.0</td>
      <td>68082.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_result
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>2780</td>
      <td>584</td>
      <td>932</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>773</td>
      <td>155</td>
      <td>377</td>
      <td>453233.0</td>
      <td>449019.0</td>
      <td>4214.0</td>
      <td>54622.0</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>748</td>
      <td>138</td>
      <td>204</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>884</td>
      <td>184</td>
      <td>81</td>
      <td>603772.0</td>
      <td>597248.0</td>
      <td>6524.0</td>
      <td>72548.0</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>1496</td>
      <td>390</td>
      <td>613</td>
      <td>525515.0</td>
      <td>507203.0</td>
      <td>18312.0</td>
      <td>68082.0</td>
    </tr>
    <tr>
      <th>광진구</th>
      <td>707</td>
      <td>53</td>
      <td>174</td>
      <td>372164.0</td>
      <td>357211.0</td>
      <td>14953.0</td>
      <td>42214.0</td>
    </tr>
    <tr>
      <th>구로구</th>
      <td>1561</td>
      <td>246</td>
      <td>323</td>
      <td>447874.0</td>
      <td>416487.0</td>
      <td>31387.0</td>
      <td>56833.0</td>
    </tr>
    <tr>
      <th>금천구</th>
      <td>1015</td>
      <td>269</td>
      <td>354</td>
      <td>255082.0</td>
      <td>236353.0</td>
      <td>18729.0</td>
      <td>32970.0</td>
    </tr>
    <tr>
      <th>노원구</th>
      <td>1265</td>
      <td>451</td>
      <td>516</td>
      <td>569384.0</td>
      <td>565565.0</td>
      <td>3819.0</td>
      <td>71941.0</td>
    </tr>
    <tr>
      <th>도봉구</th>
      <td>485</td>
      <td>42</td>
      <td>386</td>
      <td>348646.0</td>
      <td>346629.0</td>
      <td>2017.0</td>
      <td>51312.0</td>
    </tr>
    <tr>
      <th>동대문구</th>
      <td>1294</td>
      <td>198</td>
      <td>579</td>
      <td>369496.0</td>
      <td>354079.0</td>
      <td>15417.0</td>
      <td>54173.0</td>
    </tr>
    <tr>
      <th>동작구</th>
      <td>1091</td>
      <td>103</td>
      <td>314</td>
      <td>412520.0</td>
      <td>400456.0</td>
      <td>12064.0</td>
      <td>56013.0</td>
    </tr>
    <tr>
      <th>마포구</th>
      <td>574</td>
      <td>169</td>
      <td>379</td>
      <td>389649.0</td>
      <td>378566.0</td>
      <td>11083.0</td>
      <td>48765.0</td>
    </tr>
    <tr>
      <th>서대문구</th>
      <td>962</td>
      <td>68</td>
      <td>292</td>
      <td>327163.0</td>
      <td>314982.0</td>
      <td>12181.0</td>
      <td>48161.0</td>
    </tr>
    <tr>
      <th>서초구</th>
      <td>1930</td>
      <td>336</td>
      <td>398</td>
      <td>450310.0</td>
      <td>445994.0</td>
      <td>4316.0</td>
      <td>51733.0</td>
    </tr>
    <tr>
      <th>성동구</th>
      <td>1062</td>
      <td>241</td>
      <td>265</td>
      <td>311244.0</td>
      <td>303380.0</td>
      <td>7864.0</td>
      <td>39997.0</td>
    </tr>
    <tr>
      <th>성북구</th>
      <td>1464</td>
      <td>360</td>
      <td>204</td>
      <td>461260.0</td>
      <td>449773.0</td>
      <td>11487.0</td>
      <td>64692.0</td>
    </tr>
    <tr>
      <th>송파구</th>
      <td>618</td>
      <td>68</td>
      <td>463</td>
      <td>667483.0</td>
      <td>660584.0</td>
      <td>6899.0</td>
      <td>72506.0</td>
    </tr>
    <tr>
      <th>양천구</th>
      <td>2034</td>
      <td>30</td>
      <td>467</td>
      <td>479978.0</td>
      <td>475949.0</td>
      <td>4029.0</td>
      <td>52975.0</td>
    </tr>
    <tr>
      <th>영등포구</th>
      <td>904</td>
      <td>195</td>
      <td>373</td>
      <td>402985.0</td>
      <td>368072.0</td>
      <td>34913.0</td>
      <td>52413.0</td>
    </tr>
    <tr>
      <th>용산구</th>
      <td>1624</td>
      <td>112</td>
      <td>398</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
    </tr>
    <tr>
      <th>은평구</th>
      <td>1873</td>
      <td>278</td>
      <td>468</td>
      <td>494388.0</td>
      <td>489943.0</td>
      <td>4445.0</td>
      <td>72334.0</td>
    </tr>
    <tr>
      <th>종로구</th>
      <td>1002</td>
      <td>211</td>
      <td>630</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
    </tr>
    <tr>
      <th>중구</th>
      <td>671</td>
      <td>72</td>
      <td>348</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
    </tr>
    <tr>
      <th>중랑구</th>
      <td>660</td>
      <td>177</td>
      <td>109</td>
      <td>414503.0</td>
      <td>409882.0</td>
      <td>4621.0</td>
      <td>56774.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_result.sort_values(by='소계', ascending=False).head(5)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>2780</td>
      <td>584</td>
      <td>932</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
    </tr>
    <tr>
      <th>양천구</th>
      <td>2034</td>
      <td>30</td>
      <td>467</td>
      <td>479978.0</td>
      <td>475949.0</td>
      <td>4029.0</td>
      <td>52975.0</td>
    </tr>
    <tr>
      <th>서초구</th>
      <td>1930</td>
      <td>336</td>
      <td>398</td>
      <td>450310.0</td>
      <td>445994.0</td>
      <td>4316.0</td>
      <td>51733.0</td>
    </tr>
    <tr>
      <th>은평구</th>
      <td>1873</td>
      <td>278</td>
      <td>468</td>
      <td>494388.0</td>
      <td>489943.0</td>
      <td>4445.0</td>
      <td>72334.0</td>
    </tr>
    <tr>
      <th>용산구</th>
      <td>1624</td>
      <td>112</td>
      <td>398</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_result.sort_values(by='인구수', ascending=False).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>송파구</th>
      <td>618</td>
      <td>68</td>
      <td>463</td>
      <td>667483.0</td>
      <td>660584.0</td>
      <td>6899.0</td>
      <td>72506.0</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>884</td>
      <td>184</td>
      <td>81</td>
      <td>603772.0</td>
      <td>597248.0</td>
      <td>6524.0</td>
      <td>72548.0</td>
    </tr>
    <tr>
      <th>강남구</th>
      <td>2780</td>
      <td>584</td>
      <td>932</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
    </tr>
    <tr>
      <th>노원구</th>
      <td>1265</td>
      <td>451</td>
      <td>516</td>
      <td>569384.0</td>
      <td>565565.0</td>
      <td>3819.0</td>
      <td>71941.0</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>1496</td>
      <td>390</td>
      <td>613</td>
      <td>525515.0</td>
      <td>507203.0</td>
      <td>18312.0</td>
      <td>68082.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
