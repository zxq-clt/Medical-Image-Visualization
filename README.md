# Medical-Image-Visualization

可视化.nii.gz格式的CT图像数据，对label中的各个类别伪彩色处理，并与image叠加。

## visualization1.py

visualization1.py文件是对image.shape为（132，512，512）形式的图像，即从第一个维度进行切片的图像进行可视化，通过修改 slice_index的数值，来可视化不同的切片。visualization1.py使用的数据集是kits19。

## Code https://github.com/neheller/kits19

## Paper https://arxiv.org/pdf/1904.00445
