```python
import pandas as pd
Popul_Seoul = pd.read_excel('C:/kcci_python/0506/01. population_in_Seoul.xls' , header=2 , usecols='B,D,G,J,N' ,encoding ='utf-8')
Popul_Seoul.head()
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
      <th>합계</th>
      <th>10197604</th>
      <th>9926968</th>
      <th>270636</th>
      <th>1321458</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>종로구</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>중구</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>용산구</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>성동구</td>
      <td>311244.0</td>
      <td>303380.0</td>
      <td>7864.0</td>
      <td>39997.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>광진구</td>
      <td>372164.0</td>
      <td>357211.0</td>
      <td>14953.0</td>
      <td>42214.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(Popul_Seoul)
```

         자치구           계        계.1       계.2   65세이상고령자
    0     합계  10197604.0  9926968.0  270636.0  1321458.0
    1    종로구    162820.0   153589.0    9231.0    25425.0
    2     중구    133240.0   124312.0    8928.0    20764.0
    3    용산구    244203.0   229456.0   14747.0    36231.0
    4    성동구    311244.0   303380.0    7864.0    39997.0
    5    광진구    372164.0   357211.0   14953.0    42214.0
    6   동대문구    369496.0   354079.0   15417.0    54173.0
    7    중랑구    414503.0   409882.0    4621.0    56774.0
    8    성북구    461260.0   449773.0   11487.0    64692.0
    9    강북구    330192.0   326686.0    3506.0    54813.0
    10   도봉구    348646.0   346629.0    2017.0    51312.0
    11   노원구    569384.0   565565.0    3819.0    71941.0
    12   은평구    494388.0   489943.0    4445.0    72334.0
    13  서대문구    327163.0   314982.0   12181.0    48161.0
    14   마포구    389649.0   378566.0   11083.0    48765.0
    15   양천구    479978.0   475949.0    4029.0    52975.0
    16   강서구    603772.0   597248.0    6524.0    72548.0
    17   구로구    447874.0   416487.0   31387.0    56833.0
    18   금천구    255082.0   236353.0   18729.0    32970.0
    19  영등포구    402985.0   368072.0   34913.0    52413.0
    20   동작구    412520.0   400456.0   12064.0    56013.0
    21   관악구    525515.0   507203.0   18312.0    68082.0
    22   서초구    450310.0   445994.0    4316.0    51733.0
    23   강남구    570500.0   565550.0    4950.0    63167.0
    24   송파구    667483.0   660584.0    6899.0    72506.0
    25   강동구    453233.0   449019.0    4214.0    54622.0
    26   NaN         NaN        NaN       NaN        NaN
    


```python
Popul_Seoul.rename(columns ={Popul_Seoul.columns[0]:'구별',
                              Popul_Seoul.columns[1]:'인구수',
                             Popul_Seoul.columns[2]:'한국인',
                             Popul_Seoul.columns[3]:'외국인',
                              Popul_Seoul.columns[4]:'고령자'}, inplace = True)
Popul_Seoul.head()
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
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>종로구</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>중구</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>용산구</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>성동구</td>
      <td>311244.0</td>
      <td>303380.0</td>
      <td>7864.0</td>
      <td>39997.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>광진구</td>
      <td>372164.0</td>
      <td>357211.0</td>
      <td>14953.0</td>
      <td>42214.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
Popul_Seoul
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
      <th>자치구</th>
      <th>계</th>
      <th>계.1</th>
      <th>계.2</th>
      <th>65세이상고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>합계</td>
      <td>10197604.0</td>
      <td>9926968.0</td>
      <td>270636.0</td>
      <td>1321458.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>162820.0</td>
      <td>153589.0</td>
      <td>9231.0</td>
      <td>25425.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>133240.0</td>
      <td>124312.0</td>
      <td>8928.0</td>
      <td>20764.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>244203.0</td>
      <td>229456.0</td>
      <td>14747.0</td>
      <td>36231.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>성동구</td>
      <td>311244.0</td>
      <td>303380.0</td>
      <td>7864.0</td>
      <td>39997.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>광진구</td>
      <td>372164.0</td>
      <td>357211.0</td>
      <td>14953.0</td>
      <td>42214.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>동대문구</td>
      <td>369496.0</td>
      <td>354079.0</td>
      <td>15417.0</td>
      <td>54173.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>중랑구</td>
      <td>414503.0</td>
      <td>409882.0</td>
      <td>4621.0</td>
      <td>56774.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>성북구</td>
      <td>461260.0</td>
      <td>449773.0</td>
      <td>11487.0</td>
      <td>64692.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>강북구</td>
      <td>330192.0</td>
      <td>326686.0</td>
      <td>3506.0</td>
      <td>54813.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>도봉구</td>
      <td>348646.0</td>
      <td>346629.0</td>
      <td>2017.0</td>
      <td>51312.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>노원구</td>
      <td>569384.0</td>
      <td>565565.0</td>
      <td>3819.0</td>
      <td>71941.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>은평구</td>
      <td>494388.0</td>
      <td>489943.0</td>
      <td>4445.0</td>
      <td>72334.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>서대문구</td>
      <td>327163.0</td>
      <td>314982.0</td>
      <td>12181.0</td>
      <td>48161.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>마포구</td>
      <td>389649.0</td>
      <td>378566.0</td>
      <td>11083.0</td>
      <td>48765.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>양천구</td>
      <td>479978.0</td>
      <td>475949.0</td>
      <td>4029.0</td>
      <td>52975.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>강서구</td>
      <td>603772.0</td>
      <td>597248.0</td>
      <td>6524.0</td>
      <td>72548.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>구로구</td>
      <td>447874.0</td>
      <td>416487.0</td>
      <td>31387.0</td>
      <td>56833.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>금천구</td>
      <td>255082.0</td>
      <td>236353.0</td>
      <td>18729.0</td>
      <td>32970.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>영등포구</td>
      <td>402985.0</td>
      <td>368072.0</td>
      <td>34913.0</td>
      <td>52413.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>동작구</td>
      <td>412520.0</td>
      <td>400456.0</td>
      <td>12064.0</td>
      <td>56013.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>관악구</td>
      <td>525515.0</td>
      <td>507203.0</td>
      <td>18312.0</td>
      <td>68082.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>서초구</td>
      <td>450310.0</td>
      <td>445994.0</td>
      <td>4316.0</td>
      <td>51733.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>강남구</td>
      <td>570500.0</td>
      <td>565550.0</td>
      <td>4950.0</td>
      <td>63167.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>송파구</td>
      <td>667483.0</td>
      <td>660584.0</td>
      <td>6899.0</td>
      <td>72506.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>강동구</td>
      <td>453233.0</td>
      <td>449019.0</td>
      <td>4214.0</td>
      <td>54622.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


