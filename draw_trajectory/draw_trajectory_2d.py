# 读取一个csv文件，根据x,y坐标绘制图片
# 横轴z， 纵轴x
import csv
import matplotlib.pyplot as plt
import numpy as np

# 第一步，读取csv文件， 获得x，y数组
def read_csv_xy(filepath, field_x, field_y):
    x = []
    y = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            x.append(float(row[field_x]))
            y.append(float(row[field_y]))
    return x, y
    
def read_csv_lonlat(filepath):
    lon = []
    lat = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            lon.append(float(row["lon"]))
            lat.append(float(row["lat"]))
    return lon, lat


if __name__ == "__main__":
    filepath = input("请拖入原始文件： ")
    if filepath[0] == '"' or filepath[0] == "'":
        filepath = filepath[1: len(filepath)-1]
    elif filepath[0] == "&":
        filepath = filepath[3: len(filepath)-1]

    # 先画个背景
    fig, ax = plt.subplots()
    img = plt.imread(r"C:\Users\Zeyuan\Pictures\KBL1.png")
    ax.imshow(img, extent=[603035, 676011, -344751, -305597], alpha = 0.7)

    # 第一步，读取csv文件， 获得x，z数组
    x, y = read_csv_xy(filepath,"z", "x")
    target_x, target_y = read_csv_xy(filepath,"target_z", "target_x")

    # 第二步，画散点图
    ax.plot(target_x, target_y, linewidth=4)
    ax.plot(x, y, linewidth=3)
    ax.legend(["planned","actual"])
    ax.set(xlabel='z (m)', ylabel='x (m)',
        title='2D Trajectory (L1 guidance)')

    plt.show()