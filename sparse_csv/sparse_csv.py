

import os
import csv

filename_dense= r"C:\Users\Zeyuan\Desktop\sparse csv\trajactory_log.csv"
filename_sparse = r"C:\Users\Zeyuan\Desktop\sparse csv\trajactory_log_sparse.csv"

with open(filename_dense, newline='') as densefile:
    reader = csv.reader(densefile, delimiter=',')
    with open(filename_sparse, 'w', newline='') as sparsefile:
        writer = csv.writer(sparsefile, delimiter=',')
        
        i = 0
        for row in reader:
            if i % 500 == 0:
                print(i)
                writer.writerow(row)
            i +=1
            

            
                
