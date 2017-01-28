import os
import csv
import xlrd
import argparse

'''python export_sheet.py -h for arguments. Converts a specified sheet in an excel
file to a csv file. For use with Anki's import csv feature.'''

parser = argparse.ArgumentParser()
parser.add_argument("fname", type=str, help = ".xls filename to export to csv")
parser.add_argument('-s', '--sheetnum', type=int, default = 1, choices = [1, 2, 3, 4, 5, 6, 7, 8, 9], help= "sheet position, indexed from 1, to export")
parser.add_argument('-o', '--output', type=str , default='export_sheet_out.csv', help="output filename")

args = parser.parse_args()
wb = xlrd.open_workbook(args.fname)
ws = wb.sheet_by_index(args.sheetnum - 1)

print('Exporting sheet {} to {}'.format(ws.name, args.output))

# Open this way for python3
csv_file = open(args.output, 'w', newline='')
wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

for row in range(ws.nrows):
    wr.writerow(ws.row_values(row))
csv_file.close()
