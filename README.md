# Medical-Image-Visualization

可视化.nii.gz格式的CT图像数据，对label中的各个类别伪彩色处理，并与image叠加。

## visualization1.py

visualization1.py文件是对image.shape为（97，512，512）形式的图像，即从第一个维度进行切片的图像进行可视化，通过修改 slice_index的数值，来可视化不同的切片。visualization1.py使用的数据集是kits19。

### Code: https://github.com/neheller/kits19

### Paper: https://arxiv.org/pdf/1904.00445

### visualization result

![image-20250613151828686](C:\Users\86150\AppData\Roaming\Typora\typora-user-images\image-20250613151828686.png)

## visualization2.py

visualization2.py文件是对image.shape为（512，512，549）形式的图像，即从第一个维度进行切片的图像进行可视化，通过修改 slice_index的数值，来可视化不同的切片。visualization2.py使用的数据集是Lits。

### data: https://competitions.codalab.org/competitions/17094

### Paper: https://www.sciencedirect.com/science/article/pii/S1361841522003085
