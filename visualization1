import nibabel as nib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

# 设置中文字体
plt.rcParams["font.family"] = ["SimHei"]

def visualize_image_with_label(image_path, label_path, slice_index, figsize=(10, 5)):
    """
    可视化单个矢状面切片的原始图像、标签图像及其叠加效果
    修复颜色映射问题，让标签正确显示 label_config 中的颜色
    """
    # 标签配置：{标签值: (器官名称, 颜色编码)}
    label_config = {
        0: ('Background', '#000000'),  # 背景（黑色，默认不显示在图例）
        1: ('Kidney', '#0000FF'),     # 肾脏
        2: ('Tumor', '#FF0000'),   # 肿瘤
    }

    # 加载原始图像
    img = nib.load(image_path)
    image_data = img.get_fdata()
    print(f"原始图像维度: {img.shape}")

    # 加载标签图像
    lbl = nib.load(label_path)
    label_data = lbl.get_fdata()
    print(f"标签图像维度: {lbl.shape}")

    # 检查数据维度（确保是3D）
    if len(image_data.shape) != 3 or len(label_data.shape) != 3:
        raise ValueError("数据需为3D格式 (C, H, W)")

    # 验证切片索引有效性
    if slice_index < 0 or slice_index >= image_data.shape[0]:
        raise ValueError(f"无效切片索引: {slice_index}，有效范围 0~{image_data.shape[0]-1}")

    # 提取指定切片
    image_slice = image_data[slice_index, :, :]  # 矢状面切片 (H, W)
    label_slice = label_data[slice_index, :, :]  # 标签切片 (H, W)
    # 打印切片中的唯一标签
    unique_labels = np.unique(label_slice)
    print("切片中的唯一标签:", unique_labels)
    # -------------------- 关键修复：构建正确颜色映射 --------------------
    # 1. 获取所有可能的标签值（0,1,2）
    all_labels = list(label_config.keys())
    # 2. 按标签值顺序提取颜色
    colors = [label_config[lb][1] for lb in all_labels]
    # 3. 创建颜色映射（标签值直接对应颜色索引）
    cmap = ListedColormap(colors)

    # 构建图例（排除背景 0）
    legend_patches = []
    for lb in all_labels:
        if lb == 0:
            continue  # 背景不显示在图例
        name, color = label_config[lb]
        legend_patches.append(Patch(color=color, label=name))

    # 创建子图
    fig, axes = plt.subplots(1, 3, figsize=figsize)
    # 1. 显示原始图像（修复发白：手动窗宽窗位）
    # 以软组织窗为例：窗位=40，窗宽=400（可根据需求调整）
    window_center = 80
    window_width = 800
    vmin = window_center - window_width / 2
    vmax = window_center + window_width / 2
    # 1. 显示原始图像
    axes[0].imshow(image_slice.T, cmap='gray', origin='lower', vmin=vmin, vmax=vmax)
    axes[0].set_title(f'原始图像 (切片 {slice_index})')
    axes[0].axis('off')

    # 2. 显示标签图像（应用自定义颜色映射）
    # 关键：通过 norm 固定标签值范围，确保颜色映射正确
    im_label = axes[1].imshow(
        label_slice.T,
        cmap=cmap,
        origin='lower',
        interpolation='nearest',
        norm=plt.Normalize(vmin=min(all_labels), vmax=max(all_labels))
    )
    axes[1].set_title(f'标签图像 (切片 {slice_index})')
    axes[1].axis('off')

    # 3. 显示叠加图像（同样应用自定义颜色映射）
    axes[2].imshow(image_slice.T, cmap='gray', origin='lower', vmin=vmin, vmax=vmax)
    axes[2].imshow(
        label_slice.T,
        cmap=cmap,
        origin='lower',
        alpha=0.5,
        interpolation='nearest',
        norm=plt.Normalize(vmin=min(all_labels), vmax=max(all_labels))
    )
    axes[2].set_title(f'图像与标签叠加 (切片 {slice_index})')
    axes[2].axis('off')

    # 显示图例
    fig.legend(
        handles=legend_patches,
        loc='upper center',
        bbox_to_anchor=(0.5, 0.98),
        fontsize=15,
        frameon=False,
        ncol=len(legend_patches)
    )

    plt.tight_layout()
    plt.show()


# 主程序调用
if __name__ == "__main__":
    # 替换为实际路径
    image_path = r"C:\Users\86150\Desktop\kits19\case_00019\imaging.nii.gz"
    label_path = r"C:\Users\86150\Desktop\kits19\case_00019\segmentation.nii.gz"
    slice_index = 52 # 自定义切片索引

    visualize_image_with_label(image_path, label_path, slice_index)
