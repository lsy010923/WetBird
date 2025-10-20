import matplotlib.pyplot as plt
import numpy as np

# 应用一个新的、具有网格的学术风格
# 'seaborn-v0_8-whitegrid' 是 matplotlib 3.6+ 的风格，如果您的版本更老，可以使用 'seaborn-whitegrid'
plt.style.use('seaborn-v0_8-whitegrid')

# 1. 准备您的数据
epochs = [0, 20, 40, 60, 80, 110, 120, 140, 160, 180, 200]
data = {
    'RTDETR-R18': [7.04, 80.02, 86.26, 88.50, 88.74, 89.96, 90.05, 89.83, 90.90,90.13, 89.54],
    'YOLOv8': [1.93, 75.97, 85.25, 86.69, 87.81, 88.02, 89.53, 89.81, 89.86,90.00, 89.35],
    'YOLOv9': [0.59, 77.82, 84.67, 88.60, 90.79, 90.98, 91.45, 90.71, 90.60,90.68, 90.32],
    'YOLOv10': [0.00, 75.23, 84.55, 85.93, 85.90, 88.50, 88.38, 88.92, 88.96,88.78, 89.91],
    'YOLOv11': [0.05, 76.66, 85.58, 87.76, 89.39, 90.15, 90.68, 91.12, 91.41,91.45, 91.46],
    'YOLOv12': [0, 76.55, 83.933, 86.233, 88.239, 89.498, 89.585, 89.668, 89.587,89.71, 90.024],
    #'FCOS': [0,71.18, 82.00,83.22,86.19, 85.52, 84.42, 85.06, 86.53, 85.50,84.95],
    'WetBird-DETR':[10.03,87.168,89.759,91.714,91.71,92.154,92.158,92.331,92.404,92.431,92.86],
}

# 2. 定义一套全新的样式
# 使用 plt.get_cmap() 的推荐替代方案，直接从 matplotlib.colors 获取颜色循环
from matplotlib import cycler

prop_cycle = plt.rcParams['axes.prop_cycle']
colors_from_cycle = prop_cycle.by_key()['color']

model_colors = {}
for i, model_name in enumerate(data.keys()):
    if model_name != 'LiteDETR-wetbird':
        model_colors[model_name] = colors_from_cycle[i % len(colors_from_cycle)]
model_colors['WetBird-DETR'] = '#000000'  # 强制您的模型为黑色

markers = {
    'RTDETR-R18': 'v',
    'YOLOv8': '^',
    'YOLOv9': '<',
    'YOLOv10': '>',
    'YOLOv11': 's',
    'YOLOv12': 'p', # 注释掉未使用的标记
    #'FCOS': 'h',    # 注释掉未使用的标记
    'WetBird-DETR': 'D',  # 您的模型使用钻石标记
}

linestyles = {
    'RTDETR-R18': '-',
    'YOLOv8': '--',
    'YOLOv9': ':',
    'YOLOv10': '-.',
    'YOLOv11': '-',
    'YOLOv12': '--', # 注释掉未使用的线型
     #'FCOS': ':',     # 注释掉未使用的线型
    'WetBird-DETR': '-',
}

# 3. 开始绘图
fig, ax = plt.subplots(figsize=(9, 7))

# 遍历数据并绘制每一条线
for model_name, mAP_values in data.items():
    # 对您的模型进行特殊处理，使其突出
    is_our_model = (model_name == 'WetBird-DETR')

    ax.plot(epochs, mAP_values,
            label=model_name,
            color=model_colors.get(model_name),
            marker=markers.get(model_name),
            linestyle=linestyles.get(model_name),
            linewidth=3.5 if is_our_model else 2,  # 加粗您的模型线条
            markersize=8 if is_our_model else 6,
            zorder=10 if is_our_model else 5  # 确保您的模型线条在最上层
            )

# 4. 自定义图表的细节
ax.set_xlabel('Epochs', fontsize=14, fontweight='bold')
ax.set_ylabel('mAP@0.5', fontsize=14, fontweight='bold')
#ax.set_title('Model Performance Comparison', fontsize=16, fontweight='bold')  # 添加标题

ax.set_xlim(0, 200)
ax.set_ylim(0, 100)
ax.set_xticks(np.arange(0, 201, 20))
ax.set_yticks(np.arange(0, 101, 10))

ax.tick_params(axis='both', which='major', labelsize=12)
ax.legend(loc='lower right', fontsize=11, frameon=True, shadow=True)

plt.tight_layout()

# 5. 保存图形
plt.savefig("mAP_curve_new_style.png", dpi=300)
plt.show()