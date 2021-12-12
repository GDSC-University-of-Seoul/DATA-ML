# 전처리 라이브러리
import pandas as pd
import numpy as np

# 시각화 라이브러리
import plotly.graph_objects as go
# import plotly.offline as pyo
# pyo.init_notebook_mode() -- 주피터 노트북에서 보여지도록 하는 부분
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('데이터 셋/visitors_per_month_2014.csv', encoding = 'utf-8-sig', index_col = 0)
data = data.fillna(0)
data = data.astype('int32')
vertical = data.copy().T
vertical = vertical.drop('합계') # 인덱스 '합계'행 제거
Park_Name = '지리산'
Target_Park = Park_Name + '국립공원'

print(vertical.index)
# print(vertical.index)
# # plotly.graph_objs로 그래프 그리기
# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x = vertical.index, y = vertical[Park_Name]
#     )
# )

# fig.layout(
#     name = Target_Park+'방문자 수'
#     legend = True
# )
# fig.show()