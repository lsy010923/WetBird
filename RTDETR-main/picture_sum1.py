# import matplotlib.pyplot as plt
# import numpy as np
#
# # 1. 准备数据 (数据部分不变)
# data = {
#     'Gallinula chloropus': [2287, 1061, 91],
#     'Egretta garzetta': [1128, 1485, 220],
#     'Anas zonorhyncha': [936, 966, 140],
#     'Hydrophasianus chirurgus': [443, 85, 2],
#     'Chlidonias hybrida': [150, 809, 274],
#     'Charadrius dubius': [27, 440, 61],
#     'Nycticorax nycticorax': [840, 260, 23],
#     'Ardeola bacchus': [1160, 778, 74],
#     'Anas platyrhynchos': [612, 33, 0],
#     'Tachybaptus ruficollis': [534, 158, 10]
# }
#
# # 计算总数并按总数降序排序
# species_names = list(data.keys())
# totals = {name: sum(counts) for name, counts in data.items()}
# # CHANGED: reverse=True to have the tallest bar on the left
# sorted_species = sorted(species_names, key=lambda name: totals[name], reverse=True)
#
# # 根据排序后的顺序重新组织数据
# small_counts = np.array([data[name][0] for name in sorted_species])
# medium_counts = np.array([data[name][1] for name in sorted_species])
# large_counts = np.array([data[name][2] for name in sorted_species])
#
# # 2. 开始绘图
# fig, ax = plt.subplots(figsize=(14, 8))  # 调整画布大小以适应竖直布局
#
# # CHANGED: 使用更美观的配色方案
# colors = {'small': '#368A9A', 'medium': '#F28E2B', 'large': '#A9A9A9'}
#
# # CHANGED: 绘制竖直堆叠柱状图 (使用 ax.bar 和 bottom 参数)
# # 首先绘制 'Small'
# bar_s = ax.bar(sorted_species, small_counts, color=colors['small'], label='Small (s)')
# # 然后在 'Small' 的基础上绘制 'Medium'
# bar_m = ax.bar(sorted_species, medium_counts, bottom=small_counts, color=colors['medium'], label='Medium (m)')
# # 最后在 'Small' + 'Medium' 的基础上绘制 'Large'
# bar_l = ax.bar(sorted_species, large_counts, bottom=small_counts + medium_counts, color=colors['large'],
#                label='Large (L)')
#
# # 3. 美化和自定义图表
# # 添加标题和坐标轴标签
# ax.set_title('Distribution of Object Sizes by Species', fontsize=18, pad=20, weight='bold')
# ax.set_ylabel('Total Count', fontsize=14)
# # ax.set_xlabel('Species', fontsize=14) # X轴标签可以省略，因为刻度已经很清晰
#
# # CHANGED: 旋转X轴的刻度标签以防重叠
# ax.tick_params(axis='x', rotation=45, labelsize=12, ha='right')
# ax.tick_params(axis='y', labelsize=12)
#
#
# # CHANGED: 更新函数以在竖直柱状图上添加标签
# def add_labels_to_vertical_bars(bars, base_values=None):
#     if base_values is None:
#         base_values = np.zeros(len(bars))
#
#     for i, bar in enumerate(bars):
#         height = bar.get_height()
#         # 只为高度大于总数1%的色块添加标签，避免过小的色块标签重叠
#         if height > sum(totals.values()) * 0.01:
#             label_x = bar.get_x() + bar.get_width() / 2
#             label_y = base_values[i] + height / 2
#             ax.text(label_x, label_y, f'{int(height)}', ha='center', va='center', color='white', fontsize=10,
#                     fontweight='bold')
#
#
# add_labels_to_vertical_bars(bar_s)
# add_labels_to_vertical_bars(bar_m, small_counts)
# add_labels_to_vertical_bars(bar_l, small_counts + medium_counts)
#
# # 添加图例
# ax.legend(title='Size Category', fontsize=12, title_fontsize=13)
#
# # 移除顶部和右侧的边框，设置网格线
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
#
# # 确保布局整洁，防止标签被裁剪
# plt.tight_layout()
#
# # 4. 显示或保存图形
# # plt.savefig("species_distribution_vertical.png", dpi=300)
# plt.show()



import matplotlib.pyplot as plt
import numpy as np

# --- 1. 数据准备 ---
# 将您的数据结果整理成Python字典格式
# 键 (key) 是物种名称，值 (value) 是一个包含 [小, 中, 大] 计数的列表
species_data = {
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

# --- 2. 数据处理与排序 ---
# 为了让图表更清晰，按总数从高到低对物种进行排序
category_names = list(species_data.keys())
totals = {name: sum(counts) for name, counts in species_data.items()}
sorted_category_names = sorted(category_names, key=lambda name: totals[name], reverse=True)

# 根据排序后的列表，准备S, M, L三组数据
small_counts = np.array([species_data[name][0] for name in sorted_category_names])
medium_counts = np.array([species_data[name][1] for name in sorted_category_names])
large_counts = np.array([species_data[name][2] for name in sorted_category_names])


# --- 3. 绘图设置 ---
# 创建画布和坐标轴，并指定尺寸
fig, ax = plt.subplots(figsize=(14, 8))

# 定义一套专业且美观的配色方案
color_palette = {
    'small': '#368A9A',   # 水鸭蓝
    'medium': '#F28E2B',  # 暖橙色
    'large': '#A9A9A9'    # 中性灰
}

# --- 4. 核心绘图 ---
# 绘制竖直方向的堆叠柱状图
# 使用 `ax.bar` 函数，并通过 `bottom` 参数实现堆叠效果
ax.bar(sorted_category_names, small_counts, color=color_palette['small'], label='Small (s)')
ax.bar(sorted_category_names, medium_counts, bottom=small_counts, color=color_palette['medium'], label='Medium (m)')
ax.bar(sorted_category_names, large_counts, bottom=small_counts + medium_counts, color=color_palette['large'], label='Large (L)')


# --- 5. 图表美化与细节调整 ---
# 设置图表标题和坐标轴标签
ax.set_title('Distribution of Object Sizes by Species', fontsize=18, pad=20, weight='bold')
ax.set_ylabel('Total Count', fontsize=14)

# 将X轴的标签旋转45度，以防止文字重叠
ax.tick_params(axis='x', rotation=45, labelsize=12, ha='right')
ax.tick_params(axis='y', labelsize=12)

# 在每个色块中心添加对应的数值标签
base_values = np.zeros(len(small_counts))
for counts, base in [(small_counts, base_values), (medium_counts, small_counts), (large_counts, small_counts + medium_counts)]:
    for i, count in enumerate(counts):
        # 为了避免标签过于拥挤，只显示数值较大的标签
        if count > 0:
            label_x = i
            label_y = base[i] + count / 2
            ax.text(label_x, label_y, f'{int(count)}', ha='center', va='center', color='white', fontsize=10, fontweight='bold')

# 添加并设置图例
ax.legend(title='Size Category', fontsize=12, title_fontsize=13, loc='upper right')

# 优化视觉效果：移除顶部和右侧的边框，并添加水平网格线
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.25)


# --- 6. 显示与保存 ---
# 自动调整布局，确保所有元素都能完整显示
plt.tight_layout()

# 显示图表
plt.show()

# 如果需要将图表保存为文件，可以取消下面这行代码的注释
# plt.savefig("species_distribution_vertical.png", dpi=300)