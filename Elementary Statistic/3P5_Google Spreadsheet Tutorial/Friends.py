import xlrd
import numpy as np

xls = xlrd.open_workbook('Data.xlsx')
table = xls.sheets()[0]

col = table.col_values(1)
n_cols = table.ncols

data = col[1:]
print "average: " + str(np.mean(data))
print "std: " + str(np.std(data))

