import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('table_data_2025-04-12-09-44-57.csv')  # 假设CSV文件名为data.csv

# 假设我们要统计的列名为'Type'
column_name = '结果'

# 统计各种类型的数量
types_count = df[column_name].value_counts()

# 计算各种类型的比例
types_ratio = types_count / types_count.sum()
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# plt.pie(
#         slices,
#         labels=activities,
#         colors=cols,
#         startangle=90,  # 起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起
#         shadow=True,  # 是否设置阴影效果
#         explode=(0, 0.12, 0, 0),  # 每一块距离中心距离
#         autopct='%1.2f%%'  # 设置百分号显示格式
# )

# 设置标题

# 绘制饼状图
types_ratio.plot(kind='pie', autopct='%1.1f%%',shadow=True)  # autopct显示百分比

plt.legend(loc='upper right', bbox_to_anchor=[1.07, 0.01],ncol=3)



plt.title('学情统计饼状图')
plt.show()