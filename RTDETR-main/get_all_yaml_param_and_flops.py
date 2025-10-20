import warnings
import torch
from ultralytics import RTDETR
from ultralytics.utils.torch_utils import model_info
# 添加之前缺少的 check_yaml 导入，以防止 'check_yaml is not defined' 错误
from ultralytics.utils.checks import check_yaml

# 忽略不必要的警告
warnings.filterwarnings('ignore')

if __name__ == '__main__':


    yaml_file_path = 'D:/paper/RTDETR-main/RTDETR-20250622-ssj/RTDETR-20250622/RTDETR-main/ultralytics/cfg/models/rt-detr/rtdetr-SOEP-MFM-RFPN.yaml'

    print(f"正在处理文件: {yaml_file_path}")

    try:
        # 2. 直接加载模型
        model = RTDETR(yaml_file_path)
        model.fuse()

        # 3. 计算FLOPs和参数量
        # 注意: model.model 用于传入底层的Pytorch模型
        n_l, n_p, n_g, flops = model_info(model.model)

        # 4. 直接打印结果，不再需要字典和排序
        print("-" * 50)
        print(f"模型: {yaml_file_path.split('/')[-1]}")
        print(f"GFLOPs: {flops:.2f}")
        print(f"参数量 (Params): {n_p:,}")
        print("-" * 50)

    except Exception as e:
        # 如果发生错误，打印详细信息
        print(f"处理过程中发生错误!")
        print(f"错误信息: {e}")