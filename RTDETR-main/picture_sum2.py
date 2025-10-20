import matplotlib.pyplot as plt
import numpy as np

# 1. 准备数据 (这部分保持不变)
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

# 计算每个物种的总数，并按总数升序排序
species_names = list(data.keys())
totals = {name: sum(counts) for name, counts in data.items()}
sorted_species = sorted(species_names, key=lambda name: totals[name], reverse=False)

# 根据排序后的顺序重新组织数据
small_counts = np.array([data[name][0] for name in sorted_species])
medium_counts = np.array([data[name][1] for name in sorted_species])
large_counts = np.array([data[name][2] for name in sorted_species])

# 2. 开始绘图
# 创建一个图形和坐标轴
fig, ax = plt.subplots(figsize=(12, 6.5))

# --- 修改：更换为新的配色方案 ---
# 一套由 紫-青-黄 组成的专业调色板
colors = {
    'small': '#5E4FA2',
    'medium': '#47969E',
    'large': '#FEE08B'
}

# --- 修改：在barh函数中添加 height 参数使柱子变细 ---
bar_height = 0.65  # 定义柱子的高度（粗细），默认是0.8

# 绘制水平堆叠柱状图
bar_s = ax.barh(sorted_species, small_counts, height=bar_height, color=colors['small'], label='Small (s)')
bar_m = ax.barh(sorted_species, medium_counts, height=bar_height, left=small_counts, color=colors['medium'],
                label='Medium (m)')
bar_l = ax.barh(sorted_species, large_counts, height=bar_height, left=small_counts + medium_counts,
                color=colors['large'], label='Large (L)')

# 3. 美化和自定义图表
# 添加标题和坐标轴标签
ax.set_title('Distribution of Object Sizes by Species', fontsize=16, pad=20)
ax.set_xlabel('Total Count', fontsize=12)
ax.set_ylabel('Species', fontsize=12)


# 在每个色块上添加数量标签（此函数无需修改）
def add_labels_to_bars(bars, base_values=None):
    if base_values is None:
        base_values = np.zeros(len(bars))

    for i, bar in enumerate(bars):
        width = bar.get_width()
        # 为了避免标签过于拥挤，可以设置一个阈值
        if width > sum(totals.values()) * 0.01:  # 只为宽度大于总数1%的块添加标签
            label_x = base_values[i] + width / 2
            label_y = bar.get_y() + bar.get_height() / 2

            # 判断颜色深浅以决定文字颜色
            # FFE08B(黄)颜色较浅，用深色文字
            text_color = 'black' if bar.get_facecolor() == tuple(
                int(colors['large'][i:i + 2], 16) / 255 for i in (1, 3, 5)) + (1,) else 'white'

            ax.text(label_x, label_y, f'{int(width)}', ha='center', va='center', color=text_color, fontsize=9,
                    fontweight='bold')


add_labels_to_bars(bar_s)
add_labels_to_bars(bar_m, small_counts)
add_labels_to_bars(bar_l, small_counts + medium_counts)

# 添加图例
ax.legend(title='Size Category', bbox_to_anchor=(1.02, 1), loc='upper left')

# 移除顶部和右侧的边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 确保Y轴标签和图例不会被裁剪
plt.tight_layout()

# 4. 显示或保存图形
plt.show()