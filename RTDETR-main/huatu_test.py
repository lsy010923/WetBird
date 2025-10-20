import matplotlib.pyplot as plt
import numpy as np

# 1. 准备您的数据
# 请将下面的示例数据替换为您自己的数据
epochs = [0, 20, 40, 60, 80, 110, 120, 140, 160,180,200]
data = {
    'RTDETR-R18': [7.04, 80.02, 86.26, 88.50, 88.74, 89.96, 90.05, 89.83, 90.90,90.13, 89.54],
    'YOLOv8': [1.93, 75.97, 85.25, 86.69, 87.81, 88.02, 89.53, 89.81, 89.86,90.00, 89.35],
    'YOLOv9': [0.59, 77.82, 84.67, 88.60, 90.79, 90.98, 91.45, 90.71, 90.60,90.68, 90.32],
    'YOLOv10': [0.00, 75.23, 84.55, 85.93, 85.90, 88.50, 88.38, 88.92, 88.96,88.78, 89.91],
    'YOLOv11': [0.05, 76.66, 85.58, 87.76, 89.39, 90.15, 90.68, 91.12, 91.41,91.45, 91.46],
    # 'YOLOv12': [8, 33, 63, 71, 71, 74, 76, 78, 79.5,91, 90],
    # 'RTDETR-DIMB': [10.41, 80.67, 86.44, 89.13, 88.50, 89.99, 89.47, 97, 96,91, 90],
}

# 2. 定义样式 (颜色、标记等)，以匹配您的示例图
# 颜色值是从原图中提取的十六进制代码
# colors = {
#     'RTDETR-R18': '#f08080',
#     'YOLOv8': '#e0d0a0',
#     'YOLOv9': '#e8b983',
#     'YOLOv10': '#a2d9a7',
#     'YOLOv11': '#87c8b4',
#     # 'YOLOv12': '#84b8b8',
#     # 'RTDETR-DIMB': '#468484',
# }

colors = {
    'RTDETR-R18': '#FF6B35',
    'YOLOv8': '#F7931E',
    'YOLOv9': '#FFD23F',
    'YOLOv10': '#06D6A0',
    'YOLOv11': '#118AB2',
    # 'YOLOv12': '#84b8b8',
    # 'RTDETR-DIMB': '#468484',
}

#colors = {'#FF6B35', '#F7931E', '#FFD23F', '#06D6A0', '#118AB2', '#073B4C', '#8B5A3C'}
markers = {
    'RTDETR-R18': '+',
    'YOLOv8': 'o',
    'YOLOv9': 's',
    'YOLOv10': 'o',
    'YOLOv11': 'o',
    # 'YOLOv12': 'o',
    # 'RTDETR-DIMB': 'o',
}

# 3. 开始绘图
# 创建一个图形和坐标轴，设置图形大小
fig, ax = plt.subplots(figsize=(9, 7))

# 遍历数据并绘制每一条线
for model_name, mAP_values in data.items():
    ax.plot(epochs, mAP_values,
            label=model_name,
            color=colors.get(model_name, 'black'),  # 使用预定义的颜色
            marker=markers.get(model_name, 'o'),  # 使用预定义的标记
            linestyle='--' if model_name == 'YOLOv7' else '-',  # YOLOv7 使用虚线
            linewidth=2,  # 线条宽度
            markersize=8  # 标记大小
            )

# 4. 自定义图表的细节
# 设置坐标轴标签和字体大小
ax.set_xlabel('Epochs', fontsize=14)
ax.set_ylabel('mAP@.5', fontsize=14)

# 设置坐标轴的范围和刻度
ax.set_xlim(0, 201)
ax.set_ylim(0, 101)
ax.set_xticks(np.arange(0, 201, 20))
ax.set_yticks(np.arange(0, 101, 20))

# 设置刻度标签的字体大小
ax.tick_params(axis='both', which='major', labelsize=12)

# 添加图例
ax.legend(loc='lower right', fontsize=11)

# 确保布局整洁
plt.tight_layout()

# 5. 显示或保存图形
plt.savefig("my_plot_style.png", dpi=300) # 如果需要保存成文件，可以取消这行注释
plt.show()
