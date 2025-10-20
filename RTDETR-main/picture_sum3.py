import matplotlib.pyplot as plt
import numpy as np

# 数据准备
categories = [
    'Gallinula chloropus', 'Epretta garzetta', 'Anas zonorhyncha',
    'Hydrophasianus chirurgus', 'Chlidonias hybrida', 'Charadrius dubius',
    'Mycticorax nycticorax', 'Aredeola bacchus', 'Anas platyrhynchos',
    'Tachybaptus ruficollis', 'All'
]

small = [2287, 1128, 936, 443, 150, 27, 840, 1160, 612, 534, 8117]
medium = [1061, 1485, 966, 85, 809, 440, 260, 778, 33, 158, 6075]
large = [91, 220, 140, 2, 274, 61, 23, 74, 0, 10, 895]
totals = [3439, 2833, 2042, 530, 1233, 528, 1123, 2012, 645, 702, 15087]

# 计算百分比
small_percent = [s / t * 100 for s, t in zip(small, totals)]
medium_percent = [m / t * 100 for m, t in zip(medium, totals)]
large_percent = [l / t * 100 for l, t in zip(large, totals)]

# 创建图表
plt.figure(figsize=(14, 8), dpi=100)
plt.rcParams['font.family'] = 'DejaVu Sans'

# 绘制堆叠柱状图
p1 = plt.bar(categories, small, color='#66c2a5', edgecolor='white', label='Small')
p2 = plt.bar(categories, medium, bottom=small, color='#fc8d62', edgecolor='white', label='Medium')
p3 = plt.bar(categories, large, bottom=np.array(small) + np.array(medium),
             color='#8da0cb', edgecolor='white', label='Large')

# 添加总数标签
for i, total in enumerate(totals):
    plt.text(i, total + 50, f'{total}', ha='center', fontsize=9, fontweight='bold')

# 添加百分比标签（只显示大于5%的部分）
for i in range(len(categories)):
    if small_percent[i] > 5:
        plt.text(i, small[i] / 2, f'{small_percent[i]:.1f}%',
                 ha='center', va='center', fontsize=8, color='white', fontweight='bold')

    if medium_percent[i] > 5:
        y_pos = small[i] + medium[i] / 2
        plt.text(i, y_pos, f'{medium_percent[i]:.1f}%',
                 ha='center', va='center', fontsize=8, color='white', fontweight='bold')

    if large_percent[i] > 5:
        y_pos = small[i] + medium[i] + large[i] / 2
        plt.text(i, y_pos, f'{large_percent[i]:.1f}%',
                 ha='center', va='center', fontsize=8, color='white', fontweight='bold')

# 装饰图表
plt.title('Object Size Distribution by Category', fontsize=16, pad=20)
plt.ylabel('Number of Objects', fontsize=12)
plt.xlabel('Bird Species', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(fontsize=9)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Size Category', title_fontsize=11, fontsize=10)

# 调整布局
plt.tight_layout()
plt.show()