import os
import csv
import xlrd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fname", type=str, help = ".xls filename to export to csv")
parser.add_argument('-s', '--sheetnum', type=int, default = 1, choices = [1, 2, 3, 4, 5, 6, 7, 8, 9], help= "sheet position, indexed from 1, to export")
parser.add_argument('-o', '--output', type=str , default='export_sheet_out.csv', help="output filename")

args = parser.parse_args()
print(args.fname)
#wb = openpyxl.load_workbook(fname)
#ws = wb.worksheets[sheetnum]
# ctrl v, shift I # esc
wb = xlrd.open_workbook(args.fname)
ws = wb.sheet_by_index(args.sheetnum - 1) 
print('Exporting sheet {} to csv'.format(ws.name))
output = 'out.csv'
# csv_file = open(output, 'wb')
csv_file = open(output, 'w', newline='')
wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
for row in range(ws.nrows):
 wr.writerow(ws.row_values(row))
csv_file.close()
