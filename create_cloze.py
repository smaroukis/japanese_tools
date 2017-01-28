import os
import pandas as pd
import argparse
'''Adds {{c1::<content>}} tags around specified columns in an excel sheet,
exports as csv. For usage with Anki cloze deletion'''


parser = argparse.ArgumentParser()
parser.add_argument("fname", type=str, help="name of existing file to edit")
parser.add_argument("columns", type=int, nargs='+')
parser.add_argument('-s', '--sheetnum', type=int, default = 1, choices = [1, 2, 3, 4, 5, 6, 7, 8, 9], help= "sheet position, indexed from 1, to export")
parser.add_argument('-o', '--output', default='create_close_out.csv')

args = parser.parse_args()

# Take in .csv adjectives table and convert to .csv with cloze
readdata = pd.read_excel(fname)
data = readdata
beg = ['{{c' + str(i+1) + '::' for i in range(len(args.columns))]
end = '}}'

# Debugging
data = pd.read_excel('adjectives-table-anki-import.xlsx')
beg = ['{{c' + str(i+1) + '::' for i in range(4)]
end = '}}'
columns = [3, 4, 5, 6]
for i in range(len(columns)):
    data[[columns[i]]] = data[[columns[i]]].apply(lambda x: beg[i] + str(x) + end)

# TODO: for some reason, indexing here doesn't work, but it does in l33
data[[columns[0]]] = data[[columns[0]]].apply(lambda x: beg[0] + str(x) + end)

data['aff-pres'] = data['aff-pres'].apply(lambda x: beg[0] + str(x) + end)
# data['aff-past'] = data['aff-past'].apply(lambda x: beg[1] + str(x) + end)
# data['neg-pres'] = data['neg-pres'].apply(lambda x: beg[2] + str(x) + end)
# data['neg-past'] = data['neg-past'].apply(lambda x: beg[3] + str(x) + end)
#
# write to csv
data.to_csv("adjectives-table-anki-import_out.csv", index=False)
