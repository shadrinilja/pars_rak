import xlsxwriter
import pickle

with open ('sort_rusfond_data_dict', 'rb') as fp:
    l = pickle.load(fp)

row = 0
col = 0
workbook = xlsxwriter.Workbook('../Pars_rak/rusfond.xlsx')
worksheet = workbook.add_worksheet()
for i in l:
    for key in i:
        for value in i.values():
            row += 1
            worksheet.write(row, col, key)
            worksheet.write(row, col + 1, value[0])
            worksheet.write(row, col + 2, value[1])
            worksheet.write(row, col + 3, value[2])
            worksheet.write(row, col + 4, value[3])
            worksheet.write(row, col + 5, value[4])
            worksheet.write(row, col + 6, value[5])
workbook.close()