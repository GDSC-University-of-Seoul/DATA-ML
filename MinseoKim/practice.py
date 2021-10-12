from numpy import int16, int32
import pandas as pd
import matplotlib as plt

data = pd.read_csv("visitors_per_year.csv", header = 0, index_col = 0)
# 어떤 국립공원이 결측치를 가지고 있는지를 확인하기 위해 data를 전치시킨 후 isna메서드와 sum 속성으로 
# 결측치를 확인하였다. 그 결과 태백산이 2013년 ~ 2016년에 결측치를 가지고 있었음.
data['2013'] = data['2013'].str.replace(',', '')
data['2014'] = data['2014'].str.replace(',', '')
data['2015'] = data['2015'].str.replace(',', '')
data['2016'] = data['2016'].str.replace(',', '')
data['2017'] = data['2017'].str.replace(',', '')
data['2018'] = data['2018'].str.replace(',', '')
data['2019'] = data['2019'].str.replace(',', '')
data['2020'] = data['2020'].str.replace(',', '')
data = data.fillna(0)
data = data.astype(int32) # 최대값이 47277955이므로, 최대 214783647까지 표현할 수 있는 int32를 사용하여 메모리
                          # 절감
print(data.sort_values('2013', ascending= False))