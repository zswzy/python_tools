
import os
import csv


if __name__ == "__main__":
    # filepath_dense= r"C:\Users\Zeyuan\Desktop\sparse csv\trajactory_log.csv"
    filepath_dense = input("请拖入原始文件： ")
    if filepath_dense[0] == '"' or filepath_dense[0] == "'":
        filepath_dense = filepath_dense[1: len(filepath_dense)-1]
    elif filepath_dense[0] == "&":
        filepath_dense = filepath_dense[3: len(filepath_dense)-1]

    dir = os.path.dirname(filepath_dense)  # 获取文件夹名称
    filename_dense = os.path.basename(filepath_dense)  # 获取文件名称
    name_dense, ext= os.path.splitext(filename_dense)  # 文件名和扩展名
    filename_sparse = name_dense + "_sparse" + ext
    filepath_sparse = os.path.join(dir, filename_sparse)  # 在原始路径下生成sparse文件

    with open(filepath_dense, newline='') as densefile:
        reader = csv.reader(densefile, delimiter=',')
        with open(filepath_sparse, 'w', newline='') as sparsefile:
            writer = csv.writer(sparsefile, delimiter=',')
            
            i = 0
            for row in reader:
                if i % 500 == 0:
                    print(i)
                    writer.writerow(row)
                i +=1
            

            
                
