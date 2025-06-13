import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

plt.rcParams["font.family"] = ["SimHei"]


def visualize_axial_slice_with_label(image_path, label_path, slice_index, figsize=(10, 5)):
    """
    可视化单个横断面切片的原始图像、标签图像及其叠加效果

    参数:
        image_path (str): 原始图像文件路径
        label_path (str): 标签文件路径
        slice_index (int): 要显示的切片索引
        figsize (tuple): 图形大小
    """
    # 标签配置
    label_config = {
        0: ('背景', '#000000'),
        1: ('Liver', '#0000FF'),  # 蓝色
        2: ('Tumor', '#FF0000'),  # 红色
    }

    # 加载原始图像
    img = nib.load(image_path)
    image_data = img.get_fdata()
    print(f"原始图像维度: {img.shape}")
    # 加载标签图像
    lbl = nib.load(label_path)
    label_data = lbl.get_fdata()

    # 检查数据维度
    if len(image_data.shape) < 3 or len(label_data.shape) < 3:
        raise ValueError("数据维度不足，需要至少3D数据")

    # 获取横断面切片数量
    num_axial_slices = image_data.shape[2]

    # 验证切片索引是否有效
    if slice_index < 0 or slice_index >= num_axial_slices:
        raise ValueError(f"无效的切片索引: {slice_index}。有效范围是 0 到 {num_axial_slices - 1}")

    # 获取指定索引的横断面切片
    image_slice = image_data[:, :, slice_index]
    label_slice = label_data[:, :, slice_index]
    unique_labels = np.unique(label_slice)
    print("切片中的唯一标签:", unique_labels)
    # 软组织窗设置（可根据需要调整）
    window_center = 40
    window_width = 400
    vmin = window_center - window_width / 2
    vmax = window_center + window_width / 2

    # 创建自定义颜色映射
    all_colors = [label_config[i][1] for i in range(len(label_config))]
    cmap = ListedColormap(all_colors)

    # 构建图例（排除背景 0）
    legend_patches = []
    for label_val in range(1, len(label_config)):
        # if label_val in np.unique(label_slice):  # 只显示当前切片中存在的标签
        name, color = label_config[label_val]
        legend_patches.append(Patch(color=color, label=name))

    # 创建图形，包含3个子图
    fig, axes = plt.subplots(1, 3, figsize=figsize)

    # 显示原始图像
    axes[0].imshow(image_slice.T, cmap='gray', origin='lower', vmin=vmin, vmax=vmax)
    axes[0].set_title(f'原始图像 (切片 {slice_index})')
    axes[0].axis('off')

    # 显示标签图像
    axes[1].imshow(label_slice.T, cmap=cmap, origin='lower', interpolation='nearest',
                   norm=plt.Normalize(vmin=0, vmax=len(label_config) - 1))
    axes[1].set_title(f'标签图像 (切片 {slice_index})')
    axes[1].axis('off')

    # 显示叠加图像
    axes[2].imshow(image_slice.T, cmap='gray', origin='lower', vmin=vmin, vmax=vmax)
    axes[2].imshow(label_slice.T, cmap=cmap, origin='lower', alpha=0.5, interpolation='nearest',
                   norm=plt.Normalize(vmin=0, vmax=len(label_config) - 1))
    axes[2].set_title(f'图像与标签叠加 (切片 {slice_index})')
    axes[2].axis('off')

    # 显示图例
    if legend_patches:
        fig.legend(
            handles=legend_patches,
            loc='upper center',
            bbox_to_anchor=(0.5, 0.95),
            borderaxespad=0,
            fontsize=20,
            frameon=False,
            ncol=min(len(legend_patches), 4)
        )

    plt.tight_layout()
    plt.show()


# 使用示例
if __name__ == "__main__":
    # 替换为实际的文件路径
    image_path = r"C:\Users\86150\Desktop\LITS\volume-7.nii"
    label_path = r"C:\Users\86150\Desktop\LITS\segmentation-7.nii"  # 替换为实际的标签文件路径

    # 选择要显示的切片索引
    slice_index = 420

    # 可视化图像、标签及其叠加效果
    visualize_axial_slice_with_label(image_path, label_path, slice_index)
