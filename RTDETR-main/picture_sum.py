import matplotlib.pyplot as plt
import numpy as np

# 1. 准备数据
# 从您的图片结果中提取的数据
# 格式: '物种名称': [小, 中, 大]
data = {
    'Gallinula chloropus': [2287, 1061, 91],
    'Egretta garzetta': [1128, 1485, 220],
    'Anas zonorhyncha': [936, 966, 140],
    'Hydrophasianus chirurgus': [443, 85, 2],
    'Chlidonias hybrida': [150, 809, 274],
    'Charadrius dubius': [27, 440, 61],
    'Nycticorax nycticorax': [840, 260, 23],
    'Ardeola bacchus': [1160, 778, 74],
    'Anas platyrhynchos': [612, 33, 0],
    'Tachybaptus ruficollis': [534, 158, 10]
}

# 计算每个物种的总数，并按总数降序排序
species_names = list(data.keys())
totals = {name: sum(counts) for name, counts in data.items()}
sorted_species = sorted(species_names, key=lambda name: totals[name], reverse=False)

# 根据排序后的顺序重新组织数据
small_counts = np.array([data[name][0] for name in sorted_species])
medium_counts = np.array([data[name][1] for name in sorted_species])
large_counts = np.array([data[name][2] for name in sorted_species])
# small_counts = np.array([data[name][0] for name in species_names])
# medium_counts = np.array([data[name][1] for name in species_names])
# large_counts = np.array([data[name][2] for name in species_names])




# 2. 开始绘图
# 创建一个图形和坐标轴，设置一个较大的图形尺寸以容纳所有内容
fig, ax = plt.subplots(figsize=(12, 8))

# 定义颜色
#colors = {'small': '#4c72b0', 'medium': '#55a868', 'large': '#c44e52'}
colors = {'small': '#8da0cb', 'medium': '#fc8d62', 'large': '#66c2a5'}

#绘制水平堆叠柱状图
#首先绘制 'Small'
bar_s = ax.barh(sorted_species, small_counts, color=colors['small'], label='Small (s)')
# 然后在 'Small' 的基础上绘制 'Medium'
bar_m = ax.barh(sorted_species, medium_counts, left=small_counts, color=colors['medium'], label='Medium (m)')
# 最后在 'Small' + 'Medium' 的基础上绘制 'Large'
bar_l = ax.barh(sorted_species, large_counts, left=small_counts + medium_counts, color=colors['large'],
                label='Large (L)')





# 3. 美化和自定义图表
# 添加标题和坐标轴标签
#ax.set_title('Distribution of Object Sizes by Species', fontsize=16, pad=20)
ax.set_xlabel('Total Count', fontsize=12)
#ax.set_ylabel('Species', fontsize=12)


# 在每个色块上添加数量标签
def add_labels_to_bars(bars, base_values=None):
    if base_values is None:
        base_values = np.zeros(len(bars))

    for i, bar in enumerate(bars):
        width = bar.get_width()
        # 只为大于0的数值添加标签，避免图表混乱
        if width > 0:
            label_x = base_values[i] + width / 2
            label_y = bar.get_y() + bar.get_height() / 2
            ax.text(label_x, label_y, f'{int(width)}', ha='center', va='center', color='white', fontsize=9,
                    fontweight='bold')


add_labels_to_bars(bar_s)
add_labels_to_bars(bar_m, small_counts)
add_labels_to_bars(bar_l, small_counts + medium_counts)

# 添加图例
# ax.legend(title='Size Category', bbox_to_anchor=(1.02, 1), loc='upper left')
ax.legend(title='Size Category', fontsize=11, loc='lower right')

# 移除顶部和右侧的边框，使图表更简洁
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 确保Y轴标签和图例不会被裁剪
plt.tight_layout()

# 4. 显示或保存图形
plt.savefig("species_distribution.png", dpi=300, bbox_inches='tight')
plt.savefig("species_distribution.svg", format='svg', bbox_inches='tight')
plt.show()
