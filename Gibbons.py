import pandas as pd
import os
from shutil import copy

def txtEdit(bad):
    with open(bad, 'r') as ff:
            datas = ff.read().split(",")
            ff.close()
    with open('GOOD.txt', 'w') as gg:
        for i in datas:
            gg.write(""+ i + "\n")
    print("All Done! :D")

def CSVMachine(pt, dst, head):
    for i in os.listdir(pt):
        copy((pt + i),dst)
        try:
            os.rename((dst + i), (dst + i[:-4] + '.csv'))
        except:
            continue
    for j in os.listdir(dst):
        try:
            cc = pd.read_csv(dst + j, names = head)
            #cc = cc[['Year','Time','Products', 'MIS Accounts']]
            cc.to_csv(dst + j, index = False)
        except:
            print("Failed on "+ j)



pt = 'C:\\Users\\NILYSO\\P&L Dashboard Extracts\\CMA\\'
dst = 'C:\\Users\\NILYSO\\P&L Dashboard Extracts\\CSV\\'
head = ['Cube','Currency','NULL','Time','Year','NULL2','Products', 'MIS Accounts','Amt']
CSVMachine(pt, dst, head)