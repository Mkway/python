```python
import pandas as pd
CCTV_Seoul = pd.read_csv('C:/kcci_python/0506/01. CCTV_in_Seoul.csv',  encoding='utf-8')
CCTV_Seoul.head()

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
      <th>기관명</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
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
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>773</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>748</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>884</td>
      <td>388</td>
      <td>258</td>
      <td>184</td>
      <td>81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>1496</td>
      <td>846</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(CCTV_Seoul)

print( CCTV_Seoul.columns)
print( CCTV_Seoul.columns[0])
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)

print( CCTV_Seoul.columns)
```

          구별    소계  2013년도 이전  2014년  2015년  2016년
    0    강남구  2780       1292    430    584    932
    1    강동구   773        379     99    155    377
    2    강북구   748        369    120    138    204
    3    강서구   884        388    258    184     81
    4    관악구  1496        846    260    390    613
    5    광진구   707        573     78     53    174
    6    구로구  1561       1142    173    246    323
    7    금천구  1015        674     51    269    354
    8    노원구  1265        542     57    451    516
    9    도봉구   485        238    159     42    386
    10  동대문구  1294       1070     23    198    579
    11   동작구  1091        544    341    103    314
    12   마포구   574        314    118    169    379
    13  서대문구   962        844     50     68    292
    14   서초구  1930       1406    157    336    398
    15   성동구  1062        730     91    241    265
    16   성북구  1464       1009     78    360    204
    17   송파구   618        529     21     68    463
    18   양천구  2034       1843    142     30    467
    19  영등포구   904        495    214    195    373
    20   용산구  1624       1368    218    112    398
    21   은평구  1873       1138    224    278    468
    22   종로구  1002        464    314    211    630
    23    중구   671        413    190     72    348
    24   중랑구   660        509    121    177    109
    Index(['구별', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')
    구별
    Index(['구별', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')
    


```python
CCTV_Seoul.head()
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
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>773</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>748</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>884</td>
      <td>388</td>
      <td>258</td>
      <td>184</td>
      <td>81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>1496</td>
      <td>846</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
